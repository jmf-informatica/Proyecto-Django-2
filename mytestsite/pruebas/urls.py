from django.urls import path
from pruebas.views import ListaProductos, ListaProductosID, ProductoAdd, ProductoEdit, ProductoDel



urlpatterns = [

    path('productos', ListaProductos.as_view(), name='lista_productos'),
    path('productos/detalles/<int:pk>', ListaProductosID.as_view(), name='detalle_producto'),
    path('productos/create', ProductoAdd.as_view(), name='producto_create'),
    path('productos/edit/<int:pk>', ProductoEdit.as_view(), name='producto_edit'),
    path('productos/del/<int:pk>', ProductoDel.as_view(), name='producto_del'),

]