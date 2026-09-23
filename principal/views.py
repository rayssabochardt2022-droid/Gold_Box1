from django.shortcuts import render


def home(request):
    return render(request, 'principal/index.html')
def contato(request):
    return render(request, 'principal/contato.html')