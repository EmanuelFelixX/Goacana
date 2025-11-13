from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

#Classes dos pratos
class TB_PRATOS(models.Model):
    Nome = models.CharField(max_length=45, null=False)
    Disponibilidade = models.BooleanField(default=True)
    Destaque = models.BooleanField(default=False)
    Preco = models.DecimalField(null=False, decimal_places=2, max_digits=6)
    Imagem = models.ImageField(upload_to='pratos/', null=True, blank=True)
    Categoria = models.ForeignKey('TB_CATEGORIAS', on_delete=models.PROTECT, null=False)

class TB_ACOMPANHAMENTOS(models.Model):
    Nome = models.CharField(max_length=45, null=False)
    Quantidade = models.IntegerField(null=False)
    ID_Prato = models.ForeignKey('TB_PRATOS', on_delete=models.CASCADE, null=False)

class TB_CATEGORIAS(models.Model):
    Nome = models.CharField(max_length=45)
    Ordem = models.IntegerField()
    def __str__(self):
        return self.Nome

#Classes dos usuários
class TB_USUARIOS(AbstractUser):
    Nome =  models.CharField(max_length=45, null=False)
    CPF = models.CharField(max_length=11, null=False, primary_key=True)
    Login = models.CharField(max_length=45, null=False)
    Senha = models.CharField(max_length=45, null=False)

#Classes das publicações
class TB_PUBLICACOES(models.Model):
    Titulo = models.CharField(max_length=45)
    Texto = models.TextField()
    Data = models.DateField(auto_now_add=True)

class TB_IMAGENS(models.Model):
    Imagem = models.ImageField(upload_to='publi/')
    ID_Publicacao = models.ForeignKey('TB_PUBLICACOES', on_delete=models.CASCADE)

#Demais classes
class TB_HISTORICO(models.Model):
    Usuario = models.ForeignKey('TB_USUARIOS', on_delete=models.PROTECT)
    Acao = models.CharField(max_length=50)
    Data = models.DateTimeField()

class TB_NEWSLETTER(models.Model):
    Email = models.EmailField(max_length=254)
    Status = models.BooleanField(default=True)

# Funções para apagar imagens associadas aos pratos e publicações quando seus respectivos registros forem apagados
@receiver(post_delete, sender=TB_PRATOS)
def apagar_im_prato(sender, instance, **kwargs):
    if instance.Imagem:
        instance.Imagem.delete(False)

@receiver(post_delete, sender=TB_IMAGENS)
def apagar_im_pub(sender, instance, **kwargs):
    if instance.Imagem:
        instance.Imagem.delete(False)