from django import forms
from .models import Areadoartista

class AreadoartistaForm(forms.ModelForm):

    class Meta:
        model = Areadoartista
        exclude = ('created_on' , 'updated_on',)