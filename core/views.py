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
    lista_pratos = TB_PRATOS.objects.all()
    contexto = {'lista_pratos': lista_pratos}

    return render(request, 'editorcardv2.html', contexto)

def add_prato(request):
    formcar = TB_PRATOS_FORMS(request.POST or None, request.FILES)
    contexto = {'formcar': formcar}

    if formcar.is_valid():
        formcar.save()
        return redirect('editordecadarpio')

    return render (request, 'newprato.html', contexto)

def edit_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    formcar = TB_PRATOS_FORMS(request.POST or None, request.FILES ,instance=prato)
    contexto = {'formcar': formcar}

    if formcar.is_valid():
        formcar.save()
        return redirect('editordecadarpio')

    return render (request, 'newprato.html', contexto)

def diponibilidade_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    if prato.Disponibilidade == True:
        prato.Disponibilidade = False
    else:
        prato.Disponibilidade = True
    prato.save()

    return redirect('editordecadarpio')

def rem_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    prato.delete()
    return redirect('editordecadarpio')

def login(request):
    return render(request, 'login.html')