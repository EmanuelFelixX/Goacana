from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse
import random
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    formnew = TB_NEWSLETTER_FORMS(request.POST or None)
    dest = TB_PRATOS.objects.filter(Destaque=True)
    acomp =  TB_ACOMPANHAMENTOS.objects.all()
    publi = TB_PUBLICACOES.objects.all()
    if formnew.is_valid():
        formnew.save()
        return redirect('index')

    contexto = {'lista_destaques': dest, 'acomps': acomp, 'publi': publi, 'newsform': formnew}

    return render(request, 'index.html', contexto)

def contato(request):
    return render(request, 'contato.html')

def publiview(request, id):
    publi = TB_PUBLICACOES.objects.get(pk=id)
    imgs = TB_IMAGENS.objects.filter(ID_Publicacao_id = id)
    contexto = {'publi': publi, 'imgs': imgs}

    return render(request, 'publiview.html', contexto)

@login_required(login_url='login')
def lista_publi(request):
    publicacoes = TB_PUBLICACOES.objects.all()
    contexto = {'publis': publicacoes}

    return render(request, 'lista_publi.html', contexto)

@login_required(login_url='login')
def publicacao (request):
    publiform = TB_PUBLICACOES_FORMS(request.POST or None)
    if publiform.is_valid():
        publiform.save()
        return redirect('lista_publi')

    contexto = {'publiform': publiform, 'disp': 'none'}
    return render(request, 'publicacao.html', contexto)

@login_required(login_url='login')
def edit_publi(request, id):
    publi = TB_PUBLICACOES.objects.get(pk=id)
    fotos = TB_IMAGENS.objects.filter(ID_Publicacao_id = id)

    if request.method == 'POST':
        img_form = TB_IMAGENS_FORMS(request.POST, request.FILES)
        if img_form.is_valid():
            inst = img_form.save(commit=False)
            inst.ID_Publicacao_id = id
            inst.save()
            return redirect('edit_publi', id)

        publiform = TB_PUBLICACOES_FORMS(request.POST, instance=publi)
        if publiform.is_valid():
            publiform.save()
            return redirect('lista_publi')

    else:
        publiform = TB_PUBLICACOES_FORMS(instance=publi)
        img_form = TB_IMAGENS_FORMS()

    contexto = {'publiform': publiform, 'img_form': img_form, 'fotos': fotos, 'disp': 'flex'}
    return render(request, 'publicacao.html', contexto)

@login_required(login_url='login')
def rem_publi(request, id):
    publi = TB_PUBLICACOES.objects.get(pk=id)
    publi.delete()
    return redirect('lista_publi')

@login_required(login_url='login')
def rem_img(request, id):
    imagem = TB_IMAGENS.objects.get(pk=id)
    pgid = imagem.ID_Publicacao.id
    imagem.delete()
    return redirect ('edit_publi', pgid)   

def cardv2 (request):
    lista_pratos = TB_PRATOS.objects.filter(Disponibilidade=True)
    lista_cat_pratos = TB_PRATOS.objects.filter(Disponibilidade=True).values_list('Categoria_id', flat=True)
    lista_cat = TB_CATEGORIAS.objects.all().order_by('Ordem')
    acomp = TB_ACOMPANHAMENTOS.objects.all
    randomn = []
    for cat in lista_cat:
        randomn.append(random.randint(1,3))
    
    contexto = {'lista_pratos': lista_pratos, 'lista_cat': lista_cat, 'acomp': acomp, 'active': lista_cat_pratos, 'aleatorio': randomn}

    return render (request, 'cardv2.html', contexto)

@login_required(login_url='login')
def admins(request):
    return render(request, 'admins.html', {'user': request.user})

@login_required(login_url='login')
def editordecadarpio(request):
    lista_pratos = TB_PRATOS.objects.all()
    lista_categorias = TB_CATEGORIAS.objects.all().order_by('Ordem')
    categoria_ids = TB_PRATOS.objects.filter(pk__in=[p.pk for p in lista_pratos]).values_list('Categoria_id', flat=True)
    act_cat = TB_CATEGORIAS.objects.filter(pk__in=categoria_ids)

    if request.method == 'POST':
        formcat = TB_CATEGORIAS_FORMS(request.POST or None)
        if formcat.is_valid():
            formcat.save()
            return redirect('editordecadarpio')
    
    if request.method == 'GET':
        formcat = TB_CATEGORIAS_FORMS()
    
    contexto = {'lista_pratos': lista_pratos, 'lista_categorias': lista_categorias, 'formcat': formcat, 'active': act_cat, 'sit': 'none'}
    return render(request, 'editorcardv2.html', contexto)

@login_required(login_url='login')
def edit_cat(request, id):
    categoria = TB_CATEGORIAS.objects.get(pk=id)

    if request.method == 'POST':
        formcat = TB_CATEGORIAS_FORMS(request.POST, instance=categoria)
        if formcat.is_valid():
            formcat.save()
            return redirect('editordecadarpio')
    
    else:
        formcat = TB_CATEGORIAS_FORMS(instance=categoria)

    contexto = {'formcat': formcat, 'sit': 'block'}
    return render(request, 'editorcardv2.html', contexto)

@login_required(login_url='login')
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

@login_required(login_url='login')
def edit_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    img_prato = TB_PRATOS.objects.filter(pk=id)
    
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
        
        lista_acomp = TB_ACOMPANHAMENTOS.objects.filter(ID_Prato_id=id)
    
    contexto = {'formcar': formcar, 'formacomp': formacomp, 'lista_acomp': lista_acomp, 'img_prato': img_prato}
    return render (request, 'newprato.html', contexto)

def acompage(request, id):
    return render(request, 'acompage.html')

@login_required(login_url='login')
def diponibilidade_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    if prato.Disponibilidade == True:
        prato.Disponibilidade = False
    else:
        prato.Disponibilidade = True
    prato.save()

    return redirect('editordecadarpio')

@login_required(login_url='login')
def destaque_prato (request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    if prato.Destaque == True:
        prato.Destaque = False
    else:
        prato.Destaque = True
    prato.save()

    return redirect('editordecadarpio')

@login_required(login_url='login')
def rem_prato(request, id):
    prato = TB_PRATOS.objects.get(pk=id)
    prato.delete()
    return redirect('editordecadarpio')

@login_required(login_url='login')
def rem_cat(request, id):
    cat = TB_CATEGORIAS.objects.get(pk=id)
    cat.delete()
    return redirect('editordecadarpio')

@login_required(login_url='login')
def rem_acomp (request, id):
    acomp = TB_ACOMPANHAMENTOS.objects.get(pk=id)
    prato_id = acomp.ID_Prato_id
    acomp.delete()
    return redirect('edit_prato', prato_id)


def logins (request):
    if request.user.is_authenticated:
        return redirect('admins')

    else:
        if request.method == 'POST':
            username = request.POST.get('login')
            password = request.POST.get('senha')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admins')
            else:
                return render(request, 'login.html')

        else:
            return render(request, 'login.html')

@login_required(login_url='login')       
def logoff (request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def cad_user(request):
    if request.method == 'POST':
        form = TB_USUARIOS_FORMS(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    
    else: 
        form = TB_USUARIOS_FORMS()

    contexto = {'form': form}
    return render(request, 'cad_user.html', contexto)

@login_required(login_url='login')
def edit_user(request, id):
    user = TB_USUARIOS.objects.get(pk=id)

    if request.method == 'POST':
        form = TB_USUARIOS_FORMS_EDIT(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = TB_USUARIOS_FORMS_EDIT(instance=user)

    contexto = {'form': form}
    return render(request, 'cad_user.html', contexto)

@login_required(login_url='login')
def edit_password(request, id):
    user = TB_USUARIOS.objects.get(pk=id)

    if request.method == '`POST':
        form = TB_USUARIOS_FORMS_PASS(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = TB_USUARIOS_FORMS_PASS(instance=user)

    contexto = {'form': form}
    return render(request, 'change_password.html', contexto)

@login_required(login_url='login')
def rem_user (request, id):
    user = TB_USUARIOS.objects.get(pk=id)
    user.delete()
    return redirect('users')


@login_required(login_url='login')
def lista_users(request):
    users = TB_USUARIOS.objects.all()
    contexto = {'users': users}

    return render(request, 'users.html', contexto)

@login_required(login_url='login')
def send_my_email(request): #função desativada de email -> ativar apenas no computador final
    send_mail(
        'This is the Subject',                         # subject
        'This is the plain-text message body.',        # message
        'goacanarestauranteregional@gmail.com',        # from_email
        ['emanuellvitor500@gmail.com'],                # recipient_list
        fail_silently=False,
    )

    return redirect('contato')