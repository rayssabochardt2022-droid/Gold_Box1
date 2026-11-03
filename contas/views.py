from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CadastroForm


class CadastroView(CreateView):
    form_class = CadastroForm
    template_name = 'contas/cadastro.html'
    success_url = reverse_lazy('contas:conta')

    def dispatch(self, request, *args, **kwargs):
        # quem já está logado não precisa se cadastrar de novo
        if request.user.is_authenticated:
            return redirect('contas:conta')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # já entra logado depois de cadastrar
        return response


class GoldBoxLoginView(LoginView):
    template_name = 'contas/login.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('contas:conta')


class GoldBoxLogoutView(LogoutView):
    next_page = reverse_lazy('contas:login')


class ContaView(LoginRequiredMixin, TemplateView):
    """Página simples da conta: mostra o usuário logado e o botão Sair."""
    template_name = 'contas/conta.html'
    login_url = reverse_lazy('contas:login')
