"""mytestsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import mi_error_404
from django.conf.urls import handler404

urlpatterns = [
    path('',include(('Aplicacion.urls', 'Aplicacion'), namespace='Aplicacion')),
    path('pruebas/', include(('pruebas.urls', 'pruebas'), namespace='pruebas')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'mytestsite.views.mi_error_404' # Para mostrar el 404 personalizado (Debe estar en la raiz)

admin.site.site_header = 'Sitio Administrador' # Titulo del admin
admin.site.index_title = 'Panel administrador' # Cambia el subtitulo del sitio de administracion
admin.site.site_title = 'JMF-INFORMATICA'