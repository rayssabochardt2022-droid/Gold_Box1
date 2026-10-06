from django.urls import path
from . import views

urlpatterns = [
    path('', views.produtos, name='produtos'),
    path('', views.produtos, name='produtos'),
    path('cadastro/', views.cadastro, name='cadastro'),
]