from django.shortcuts import render


# Create your views here.

# Homepage 
    # Display generic informaiton about the company and their services
def index(request):
    return render(request, 'homepage/index.html')
    
    
def about(request):
    return render(request, 'About/about.html')

def services(request):
    return render(request, 'services/service.html')


def basement(request):
    return render(request, 'services/basement.html')

def kitchen(request):
    return render(request, 'services/kitchen.html')

def bathroom(request):
    return render(request, 'services/bathroom.html')
