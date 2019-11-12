from django.contrib import admin
from pruebas.models import Productos, Periodos, Paises

# Register your models here.
class ProdAdmin(admin.ModelAdmin): # Listado de campos que se veran en el admin del modelo Productos
    list_display= (
        'id',
        'nombre',
        'periodo',
        'pais',
        'PrecioCompra',
        'PrecioRenovacion',
    )
    search_fields=('nombre','pais__pais','periodo__periodo') # Filtra registros por estos campos indicados
    list_filter=('nombre','periodo__periodo','pais__pais')
class PeriodoAdmin(admin.ModelAdmin): # Listado de campos que se veran en el admin del modelo Periodos
    list_display=(
        'id',
        'periodo',
    )
    search_fields=('periodo',)

class PaisesAdmin(admin.ModelAdmin): # Listado de campos que se veran en el admin del modelo Paises
    list_display=(
        'id',
        'pais',
    )
    search_fields=('pais',)


admin.site.register(Productos, ProdAdmin)
admin.site.register(Periodos,PeriodoAdmin)
admin.site.register(Paises, PaisesAdmin)