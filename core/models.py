from django.db import models

# Create your models here.

#Classes dos pratos
class TB_PRATOS(models.Model):
    Nome = models.CharField(max_length=45)
    Disponibilidade = models.BooleanField()
    Preco = models.FloatField()
    Categoria = models.ForeignKey('TB_CATEGORIAS', on_delete=models.PROTECT)

class TB_CATEGORIAS(models.Model):
    Nome = models.CharField(max_length=45)


#Classes dos usuários

#Classes das publicações
class TB_PUBLICACOES(models.Model):
    Titulo = models.CharField(max_length=45)
    Texto = models.TextField()

class TB_IMAGENS(models.Model):
    Imagem = models.ImageField(upload_to='publi/')
    ID_Publicacao = models.ForeignKey('TB_PUBLICACOES', on_delete=models.PROTECT)