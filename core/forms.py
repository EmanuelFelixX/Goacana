from django import forms
from .models import *

class TB_PRATOS_FORMS(forms.ModelForm):
    class Meta:
        model = TB_PRATOS
        fields = ['Nome', 'Preco', 'Categoria', 'Imagem']

class TB_CATEGORIAS_FORMS(forms.ModelForm):
    class Meta:
        model = TB_CATEGORIAS
        fields = ['Nome']

class TB_ACOMPANHAMENTOS_FORMS(forms.ModelForm):
    class Meta:
        model = TB_ACOMPANHAMENTOS
        fields = ['Nome', 'Quantidade']