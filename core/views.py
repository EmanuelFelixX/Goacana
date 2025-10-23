from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def index(request):
    dest = TB_PRATOS.objects.filter(Destaque=True)
    acomp =  TB_ACOMPANHAMENTOS.objects.all()
    contexto = {'lista_destaques': dest, 'acomps': acomp}

    return render(request, 'index.html', contexto)

def contato(request):
    return render(request, 'contato.html')

def publicacao (request):
    return render(request, 'publicacao.html')

def perfil(request):
    return render(request, 'perfil.html')

def cardapio(request):
    return render(request, 'cardapio.html')

def cardv2 (request):
    lista_pratos = TB_PRATOS.objects.filter(Disponibilidade=True)
    lista_cat_pratos = TB_PRATOS.objects.all().values_list('Categoria_id', flat=True)
    lista_cat = TB_CATEGORIAS.objects.all()
    acomp = TB_ACOMPANHAMENTOS.objects.all

    contexto = {'lista_pratos': lista_pratos, 'lista_cat': lista_cat, 'acomp': acomp, 'active': lista_cat_pratos}

    return render (request, 'cardv2.html', contexto)

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
    
    contexto = {'formcar': formcar, 'sit': 'False'}
    return render (request, 'newprato.html', contexto)


def edit_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    
    if request.method == 'POST':
        formcar = TB_PRATOS_FORMS(request.POST, request.FILES, instance=prato)
        if formcar.is_valid():
            formcar.save()
            return redirect('editordecadarpio')
        
        formacomp = TB_ACOMPANHAMENTOS_FORMS(request.POST)
        if formacomp.is_valid():
            acomp = formacomp.save(commit=False)
            acomp.ID_Prato_id = id
            acomp.save()
            return redirect('edit_prato', id=id)
        
        lista_acomp = TB_ACOMPANHAMENTOS.objects.filter(ID_Prato_id=id)
        
    else:
        formcar = TB_PRATOS_FORMS(instance=prato)
        formacomp = TB_ACOMPANHAMENTOS_FORMS()
        if formacomp.is_valid():
            acomp = formacomp.save(commit=False)
            acomp.ID_Prato_id = id
            acomp.save()
            return redirect('edit_prato', id)
        
        lista_acomp = TB_ACOMPANHAMENTOS.objects.filter(ID_Prato_id=id)
    
    contexto = {'formcar': formcar, 'formacomp': formacomp, 'lista_acomp': lista_acomp}
    return render (request, 'newprato.html', contexto)

def diponibilidade_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    if prato.Disponibilidade == True:
        prato.Disponibilidade = False
    else:
        prato.Disponibilidade = True
    prato.save()

    return redirect('editordecadarpio')

def destaque_prato (request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    if prato.Destaque == True:
        prato.Destaque = False
    else:
        prato.Destaque = True
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

def rem_acomp (request, id):
    acomp = TB_ACOMPANHAMENTOS.objects.get(pk=id)
    prato_id = acomp.ID_Prato_id
    acomp.delete()
    return redirect('edit_prato', prato_id)

def login(request):
    return render(request, 'login.html')