from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class ContasTests(TestCase):
    def test_cadastro_cria_usuario_e_entra_logado(self):
        dados = {
            'username': 'joao', 'first_name': 'João', 'email': 'joao@exemplo.com',
            'password1': 'SenhaForte!2026', 'password2': 'SenhaForte!2026',
        }
        resposta = self.client.post(reverse('contas:cadastro'), dados)
        self.assertRedirects(resposta, reverse('contas:conta'))
        self.assertTrue(User.objects.filter(username='joao').exists())

    def test_login_correto_e_errado(self):
        User.objects.create_user('maria', 'maria@exemplo.com', 'SenhaForte!2026')
        errado = self.client.post(reverse('contas:login'), {'username': 'maria', 'password': 'x'})
        self.assertEqual(errado.status_code, 200)
        certo = self.client.post(reverse('contas:login'), {'username': 'maria', 'password': 'SenhaForte!2026'})
        self.assertRedirects(certo, reverse('contas:conta'))

    def test_logout_encerra_a_sessao(self):
        usuario = User.objects.create_user('maria', 'maria@exemplo.com', 'SenhaForte!2026')
        self.client.force_login(usuario)
        resposta = self.client.post(reverse('contas:logout'))
        self.assertRedirects(resposta, reverse('contas:login'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_pagina_da_conta_exige_login(self):
        resposta = self.client.get(reverse('contas:conta'))
        self.assertRedirects(resposta, reverse('contas:login') + '?next=' + reverse('contas:conta'))
