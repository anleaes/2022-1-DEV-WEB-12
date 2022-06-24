
from django import forms
from .models import Tipo

class TipoForm(forms.ModelForm):

    class Meta:
        model = Tipo
        exclude = ('created_on' , 'updated_on',)