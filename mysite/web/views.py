from django.shortcuts import render, redirect
from .models import Gallery, QuoteRequest, QuotePhoto
from .forms import QuoteRequestForm
from django.contrib import messages
from .services.email_service import (
    send_customer_confirmation,
    send_admin_notification,
)


# Create your views here.

# Homepage 
    # Display generic informaiton about the company and their services
def index(request):
    return render(request, 'homepage/index.html')
    
    
def about(request):
    return render(request, 'about/about.html')

def services(request):
    return render(request, 'services/service.html')


def basement(request):
    return render(request, 'services/basement.html')
    
def kitchen(request):
    return render(request, 'services/kitchen.html')

def bathroom(request):
    return render(request, 'services/bathroom.html')

def tv(request):
    return render(request, 'services/tv.html')
    
def interlock(request):
    return render(request, 'services/interlock.html')
    
def quote_request(request):
    if request.method == "POST":
        form = QuoteRequestForm(request.POST, request.FILES)
        
        if form.is_valid():
            quote = form.save()
            for file in request.FILES.getlist('photos'):
                QuotePhoto.objects.create(quote_request=quote, image=file)
             #Send Emails   
            send_admin_notification(quote)
            send_customer_confirmation(quote)
            
            return redirect('web:thank_you')
        else:
            # Store field-specific errors and submitted values in the session
            request.session['quote_form_errors'] = form.errors
            request.session['quote_form_data'] = request.POST.dict()
            messages.error(request, "Please correct the errors below and resubmit.")

    referer = request.META.get('HTTP_REFERER')
    return redirect(referer or 'web:index')

def thank_you(request):
    return render(request, 'partials/thank_you.html')

def gallery(request):
    galleries = Gallery.objects.prefetch_related("photos")
    return render(request, "gallary/gallery.html", {"galleries": galleries})


def form(request):
    form_errors = request.session.pop('quote_form_errors', None)
    form_data = request.session.pop('quote_form_data', None)
    return render(request, 'partials/form.html', {
        'form_errors': form_errors,
        'form_data': form_data,
    })

def privacy_policy(request):
    return render(request, "partials/privacy_policy.html")

def terms_of_service(request):
    return render(request, "partials/terms_of_service.html")
