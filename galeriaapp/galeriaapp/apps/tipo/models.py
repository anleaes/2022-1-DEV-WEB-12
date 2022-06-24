from django.db import models

# Create your models here.

class Tipo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'Tipos'
        ordering =['id']

    def __str__(self):
        return self.name