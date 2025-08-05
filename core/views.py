from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def perfil(request):
    return render(request, 'perfil.html')

def cardapio(request):
    return render(request, 'cardapio.html')

def admins(request):
    return render(request, 'admins.html')

def editordecadarpio(request):
    return render(request, 'editordecadarpio.html')