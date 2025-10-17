from django.db import models

# Create your models here.

#Classes dos pratos
class TB_PRATOS(models.Model):
    Nome = models.CharField(max_length=45, null=False)
    Disponibilidade = models.BooleanField(default=True)
    Preco = models.FloatField(null=False)
    Categoria = models.ForeignKey('TB_CATEGORIAS', on_delete=models.PROTECT, null=False)

class TB_CATEGORIAS(models.Model):
    Nome = models.CharField(max_length=45)


#Classes dos usuários
class TB_USUARIOS(models.Model):
    Nome =  models.CharField(max_length=45, null=False)
    CPF = models.CharField(max_length=11, null=False, primary_key=True)
    Email = models.CharField(max_length=45, null=False)
    Login = models.CharField(max_length=45, null=False)
    Senha = models.CharField(max_length=45, null=False)
    N_Acesso = models.ForeignKey('TB_NACCESS', on_delete=models.PROTECT)

class TB_NACCESS (models.Model):
    Nome = models.CharField(max_length=20)
    ADD_PRATO = models.BooleanField(default=False)
    MOD_PRATO = models.BooleanField(default=False)
    REM_PRATO = models.BooleanField(default=False)

    ADD_PUBLI = models.BooleanField(default=False)
    MOD_PUBLI = models.BooleanField(default=False)
    REM_PUBLI = models.BooleanField(default=False)

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