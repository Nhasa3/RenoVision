from django.shortcuts import render, redirect
from .models import QuoteRequest, QuotePhoto
from .forms import QuoteRequestForm

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
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote = form.save()
            for file in request.FILES.getlist('photos'):
                QuotePhoto.objects.create(quote_request=quote, image=file)
            return redirect('web:thank_you')
    else:
        form = QuoteRequestForm()
    return render(request, 'form.html', {'form': form})

def thank_you(request):
    return render(request, 'partials/thank_you.html')
