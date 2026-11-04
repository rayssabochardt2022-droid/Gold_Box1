from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_dicas, name='lista_dicas'),
    path('cadastrar/', views.cadastrar_dica, name='cadastrar_dica'),
    path('<int:pk>/editar/', views.editar_dica, name='editar_dica'),
    path('<int:pk>/excluir/', views.excluir_dica, name='excluir_dica'),
]