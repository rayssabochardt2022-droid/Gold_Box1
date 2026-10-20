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
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class GoldBoxLoginView(LoginView):
    template_name = 'contas/login.html'
    redirect_authenticated_user = True


class GoldBoxLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class PerfilView(LoginRequiredMixin, TemplateView):
        template_name = "contas/perfil.html"
