from django.db import models
from areadoartista.models import Areadoartista



# Create your models here.

class Artista(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    artista_areadoartista = models.ManyToManyField(Areadoartista, through='ArtistaAreadoartista', blank=True)
    
    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering =['id']

    def __str__(self):
        return self.first_name


class ArtistaAreadoartista(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Artista, on_delete=models.CASCADE)
    areadoartista = models.ForeignKey(Areadoartista, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item da Área do Artista'
        verbose_name_plural = 'Itens das Áreas do Artista'
        ordering =['id']

    def __str__(self):
        return self.areadoartista.name