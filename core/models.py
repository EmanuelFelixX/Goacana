from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

#Classes dos pratos
class TB_PRATOS(models.Model):
    Nome = models.CharField(max_length=45, null=False)
    Disponibilidade = models.BooleanField(default=True)
    Preco = models.FloatField(null=False)
    Imagem = models.ImageField(upload_to='pratos/', null=True, blank=True)
    Categoria = models.ForeignKey('TB_CATEGORIAS', on_delete=models.PROTECT, null=False)

class TB_ACOMPANHAMENTOS(models.Model):
    Nome = models.CharField(max_length=45, null=False)
    Quantidade = models.IntegerField(null=False)
    ID_Prato = models.ForeignKey('TB_PRATOS', on_delete=models.PROTECT, null=False)

class TB_CATEGORIAS(models.Model):
    Nome = models.CharField(max_length=45)
    def __str__(self):
        return self.Nome

#Classes dos usuários
class TB_USUARIOS(models.Model):
    Nome =  models.CharField(max_length=45, null=False)
    CPF = models.CharField(max_length=11, null=False, primary_key=True)
    Email = models.CharField(max_length=45, null=False)
    Login = models.CharField(max_length=45, null=False)
    Senha = models.CharField(max_length=45, null=False)
    # Permissões para os pratos
    ADD_PRATO = models.BooleanField(default=False)
    MOD_PRATO = models.BooleanField(default=False)
    REM_PRATO = models.BooleanField(default=False)

    # Permissões para as publicações
    ADD_PUBLI = models.BooleanField(default=False)
    MOD_PUBLI = models.BooleanField(default=False)
    REM_PUBLI = models.BooleanField(default=False)

    # Permissões para os destaques
    ADD_DESTA = models.BooleanField(default=False)
    REM_DESTA = models.BooleanField(default=False)

#Classes das publicações
class TB_PUBLICACOES(models.Model):
    Titulo = models.CharField(max_length=45)
    Texto = models.TextField()

class TB_IMAGENS(models.Model):
    Imagem = models.ImageField(upload_to='publi/')
    ID_Publicacao = models.ForeignKey('TB_PUBLICACOES', on_delete=models.PROTECT)

#Demais classes
class TB_HISTORICO(models.Model):
    Usuario = models.ForeignKey('TB_USUARIOS', on_delete=models.PROTECT)
    Acao = models.CharField(max_length=50)
    Data = models.DateTimeField()

# Funções para apagar imagens associadas aos pratos e publicações quando seus respectivos registros forem apagados
@receiver(post_delete, sender=TB_PRATOS)
def apagar_im_prato(sender, instance, **kwargs):
    if instance.Imagem:
        instance.Imagem.delete(False)

@receiver(post_delete, sender=TB_IMAGENS)
def apagar_im_pub(sender, instance, **kwargs):
    if instance.Imagem:
        instance.Imagem.delete(False)