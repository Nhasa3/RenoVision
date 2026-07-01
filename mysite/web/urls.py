from django.urls import path
from web import views

app_name='web'

urlpatterns = [
    path('', views.index, name="index"),
    path('services',views.services, name="services"),
    path('basement', views.basement,name="basement"),
    path('kitchen', views.kitchen, name="kitchen"),
    path('bathroom', views.bathroom, name="bathroom"),
    path('tv', views.tv, name="tv"),
    path('interlock', views.interlock, name="interlock"),
    path('about', views.about,name="about"),
    
]
