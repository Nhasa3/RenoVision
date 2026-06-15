from django.shortcuts import render


# Create your views here.

# Homepage 
    # Display generic informaiton about the company and their services
def index(request):
    return render(request, 'homepage/index.html')
    