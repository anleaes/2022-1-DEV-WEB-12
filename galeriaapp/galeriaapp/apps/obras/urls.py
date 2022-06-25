from django.urls import path
from . import views

app_name = 'obras'

urlpatterns = [
    path('', views.list_obras, name='list_obras'),
    path('adicionar/', views.add_obra, name='add_obra'),
    path('editar/<int:id_obra>/', views.edit_obra, name='edit_obra'),
    path('excluir/<int:id_obra>/', views.delete_obra, name='delete_obra'),
]