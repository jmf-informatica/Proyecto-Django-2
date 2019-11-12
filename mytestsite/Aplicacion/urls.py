from django.urls import path
from django.contrib.auth import views as auth_views
from Aplicacion.views import Home,PageForbidden


urlpatterns = [
    path('', Home.as_view() , name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html') , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/login.html') , name='logout'),
    path('prohibido/', PageForbidden.as_view() , name='prohibido'),
]

