from django import forms
from .models import Obras

class ObraForm(forms.ModelForm):

    class Meta:
        model = Obras
        exclude = ('created_on' , 'updated_on',)