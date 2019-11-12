from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from datetime import date
from django.views.defaults import page_not_found
from django.shortcuts import render


# Create your views here.

class PermisoDenegado(PermissionRequiredMixin): # Responde al template de la clase PageForbidden
    login_url="Aplicacion:prohibido"
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(LoginRequiredMixin,TemplateView):
    template_name = "Aplicacion/index.html"
    login_url = "login"

""" Esta clase responde a PermisoDenegado que a su vez se invoca en las clases
que se desee prohibir acceso como por ejemplo un delete. """
class PageForbidden(TemplateView):
    template_name="Aplicacion/prohibido.html"


    
    