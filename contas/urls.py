from django.urls import path

from .views import CadastroView, GoldBoxLoginView, GoldBoxLogoutView

urlpatterns = [
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('login/', GoldBoxLoginView.as_view(), name='login'),
    path('logout/', GoldBoxLogoutView.as_view(), name='logout'),
]
