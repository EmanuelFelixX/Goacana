from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def publicacao (request):
    return render(request, 'publicacao.html')

def perfil(request):
    return render(request, 'perfil.html')

def cardapio(request):
    return render(request, 'cardapio.html')

def admins(request):
    return render(request, 'admins.html')

def editordecadarpio(request):
    formcar = TB_PRATOS_FORMS(request.POST or None)
    formcat = TB_CATEGORIAS_FORMS(request.POST or None)
    contexto = {'formcar': formcar, 'formcat': formcat}
    if formcat.is_valid():
        formcat.save()
        redirect('editordecadarpio')

    return render(request, 'editordecadarpio.html', contexto)

def login(request):
    return render(request, 'login.html')