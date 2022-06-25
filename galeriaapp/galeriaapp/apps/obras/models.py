from django.db import models
from tipo.models import Tipo

# Create your models here.

class Obra(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data De Pintura', auto_now=False, auto_now_add=False) 
    is_active = models.BooleanField('Ativo', default=False)
    photo = models.ImageField('Foto', upload_to='photos')
    doc = models.FileField('Documentos', upload_to='docs')
    category = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        ordering =['id']

    def __str__(self):
        return self.name
