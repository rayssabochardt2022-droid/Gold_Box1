from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_dicas, name='lista_dicas'),
    path('cadastrar/', views.cadastrar_dica, name='cadastrar_dica'),
    path('editar/<int:pk>/', views.editar_dica, name='editar_dica'),
]