from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('<int:id>/editar/', views.editar_produto, name='editar_produto'),
    path('<int:id>/excluir/', views.excluir_produto, name='excluir_produto'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'
    ),


]
