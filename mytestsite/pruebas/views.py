from django.shortcuts import render
from .models import Productos,Paises, Periodos
from django.views.generic import ListView, TemplateView, CreateView, UpdateView,DeleteView
#from django.core import serializers
#from django.http import JsonResponse
#from pruebas.serializers import ProductoSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from pruebas.forms import FormProductos,FormPeriodos,FormPaises,FormCreate
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.urls import reverse_lazy
from Aplicacion.views import PermisoDenegado

# Create your views here.

class ListaProductos(LoginRequiredMixin,ListView): # Listado de todos los productos
    template_name='pruebas/lista_productos.html'
    model=Productos
    context_object_name='productos'
    login_url='Aplicacion:login'

class ListaProductosID(LoginRequiredMixin,ListView): #Filtro de producto por ID
    template_name='pruebas/producto_detalle.html'
    context_object_name='productos'
    login_url='Aplicacion:login'

    def get_queryset(self):
        id=self.kwargs['pk']
        Lista=Productos.objects.filter(id=id)
        return Lista


class ProductoAdd(SuccessMessageMixin,PermisoDenegado,CreateView):
    permission_required="pruebas.add_productos"
    model=Productos
    template_name = "pruebas/producto_create.html"
    form_class=FormCreate
    context_object_name='producto'
    success_url=reverse_lazy('pruebas:lista_productos')
    success_message = "El producto %(nombre)s fue creado exitosamente!"


class ProductoEdit(SuccessMessageMixin,PermisoDenegado, UpdateView):
    permission_required="pruebas.change_productos"
    model=Productos
    template_name = "pruebas/producto_create.html"
    context_object_name='producto'
    form_class=FormCreate
    success_url= reverse_lazy('pruebas:lista_productos')
    success_message = "El producto %(nombre)s fue modificado exitosamente!"


class ProductoDel(SuccessMessageMixin,PermisoDenegado, DeleteView):
        permission_required = "pruebas.delete_productos"
        model=Productos
        template_name = "pruebas/producto_del.html"
        context_object_name='producto'
        success_url= reverse_lazy('pruebas:lista_productos')
        success_message = "El producto %(nombre)s fue eliminado exitosamente!"


 
