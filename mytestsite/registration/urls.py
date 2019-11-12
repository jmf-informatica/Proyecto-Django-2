from django.urls import path, include
from .views import ProfileUpdate, EmailUpdate


urlpatterns = [

    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email', EmailUpdate.as_view(), name='profile_email'),
    
]