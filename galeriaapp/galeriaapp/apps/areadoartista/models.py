from django.db import models


# Create your models here.

class Areadoartista(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Área do Artista'
        verbose_name_plural = 'Áreas do Artista'
        ordering =['id']

    def __str__(self):
        return self.name

# class ArtistaAreadoartista(models.Model):
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     client = models.ForeignKey(Artista, on_delete=models.CASCADE)
#     areadoartista = models.ForeignKey(Areadoartista, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = 'Item da Area do Artista'
#         verbose_name_plural = 'Itens da Area do Artista'
#         ordering =['id']

#     def __str__(self):
#         return self.areadoartista.name
