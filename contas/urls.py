from django.urls import path

from .views import CadastroView, ContaView, GoldBoxLoginView, GoldBoxLogoutView

app_name = 'contas'

urlpatterns = [
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('login/', GoldBoxLoginView.as_view(), name='login'),
    path('logout/', GoldBoxLogoutView.as_view(), name='logout'),
    path('conta/', ContaView.as_view(), name='conta'),
]
