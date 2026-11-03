from django.shortcuts import render


def home(request):
    return render(request, 'institucional/index.html')
def contato(request):
    return render(request, 'institucional/contato.html')