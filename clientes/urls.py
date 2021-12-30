from django.urls import path
from .views import borrar, editar, obtenerTodo, guardar, obtenerPorId

urlpatterns = [
    path('clientes/', obtenerTodo, name = 'index'),
    path('clientes/guardar/', guardar),
    path('clientes/<int:pk>/', obtenerPorId),
    path('clientes/editar/<int:pk>/', editar),
    path('clientes/borrar/<int:pk>/', borrar),
]
