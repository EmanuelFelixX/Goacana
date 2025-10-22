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
    lista_categorias = TB_CATEGORIAS.objects.all()
    categoria_ids = TB_PRATOS.objects.filter(pk__in=[p.pk for p in lista_pratos]).values_list('Categoria_id', flat=True)
    act_cat = TB_CATEGORIAS.objects.filter(pk__in=categoria_ids)
    formcat = TB_CATEGORIAS_FORMS(request.POST or None)
    contexto = {'lista_pratos': lista_pratos, 'lista_categorias': lista_categorias, 'formcat': formcat, 'active': act_cat}
    
    if formcat.is_valid():
        formcat.save()
        return redirect('editordecadarpio')
    
    return render(request, 'editorcardv2.html', contexto)

def add_prato(request):
    if request.method == 'POST':
        formcar = TB_PRATOS_FORMS(request.POST, request.FILES)
        if formcar.is_valid():
            formcar.save()
            return redirect('editordecadarpio')
    else:
        formcar = TB_PRATOS_FORMS() 
    
    contexto = {'formcar': formcar}
    return render (request, 'newprato.html', contexto)


def edit_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    
    if request.method == 'POST':
        formcar = TB_PRATOS_FORMS(request.POST, request.FILES, instance=prato)
        if formcar.is_valid():
            formcar.save()
            return redirect('editordecadarpio')
        
    else:
        formcar = TB_PRATOS_FORMS(instance=prato) 
    
    contexto = {'formcar': formcar}
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

def rem_cat(request, id):
    cat = TB_CATEGORIAS.objects.get(pk=id)
    cat.delete()
    return redirect('editordecadarpio')

def login(request):
    return render(request, 'login.html')