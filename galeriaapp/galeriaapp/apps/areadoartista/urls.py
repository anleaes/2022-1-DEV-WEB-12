from django.urls import path
from . import views

app_name = 'areadoartista'

urlpatterns = [
    path('', views.list_areadoartista, name='list_areadoartista'),
    path('adicionar/', views.add_areadoartista, name='add_areadoartista'),
    path('editar/<int:id_areadoartista>/', views.edit_areadoartista, name='edit_areadoartista'),
    path('excluir/<int:id_areadoartista>/', views.delete_areadoartista, name='delete_areadoartista'),
]