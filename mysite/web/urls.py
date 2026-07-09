from django.urls import path
from web import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('quote/', views.quote_request,name="quote_request"),
    path('thank_you/', views.thank_you, name="thank_you"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
