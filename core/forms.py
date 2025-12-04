from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class TB_USUARIOS_FORMS_EDIT(UserChangeForm):
    class Meta:
        model = TB_USUARIOS
        fields = ['Nome', 'email', 'Telefone', 'username', 'password']

class TB_USUARIOS_FORMS_PASS(UserCreationForm):
    class Meta:
        model = TB_USUARIOS
        fields = ['password1', 'password2']

class TB_USUARIOS_FORMS(UserCreationForm):
    class Meta:
        model = TB_USUARIOS
        fields = ['Nome', 'CPF', 'Telefone', 'Data_Nascimento', 'username', 'email', 'password1', 'password2']

        widgets = {
            'Data_Nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

class TB_PRATOS_FORMS(forms.ModelForm):
    class Meta:
        model = TB_PRATOS
        fields = ['Nome', 'Preco', 'Categoria', 'Imagem']

class TB_CATEGORIAS_FORMS(forms.ModelForm):
    class Meta:
        model = TB_CATEGORIAS
        fields = ['Nome', 'Ordem']

class TB_ACOMPANHAMENTOS_FORMS(forms.ModelForm):
    class Meta:
        model = TB_ACOMPANHAMENTOS
        fields = ['Nome', 'Quantidade']

class TB_NEWSLETTER_FORMS(forms.ModelForm):
    class Meta:
        model = TB_NEWSLETTER
        fields = ['Email']

class TB_PUBLICACOES_FORMS(forms.ModelForm):
    class Meta:
        model = TB_PUBLICACOES
        fields = ['Titulo', 'Texto']

class TB_IMAGENS_FORMS(forms.ModelForm):
    class Meta:
        model = TB_IMAGENS
        fields = ['Imagem']