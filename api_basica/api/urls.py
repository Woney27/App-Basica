from django.urls import path
from .views import obtener_agregar_items, modificar_item, eliminar_item, obtener_item

urlpatterns = [
    
    path('items/', obtener_agregar_items, name='obtener_agregar_items'),
    path('items/<int:item_id>/', obtener_item, name='obtener_item'),
    path('items/modificar/<int:item_id>/', modificar_item, name='modificar_item'),
    path('items/eliminar/<int:item_id>/', eliminar_item, name='eliminar_item'),
]

