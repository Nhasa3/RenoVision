from django.urls import path
from web import views

app_name='web'

urlpatterns = [
    path('', views.index, name="index"),
    path('services',views.services, name="services"),
    path('basement', views.basement,name="basement"),
    path('about', views.about,name="about"),
    
]
