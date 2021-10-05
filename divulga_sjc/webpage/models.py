from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length = 200)
    
class Negocio(models.Model):
    categoria = models.ForeignKey(Categories, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    descricao = models.CharField(max_length=800)
    instagram = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=200)
    