from django import forms
from .models import *

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