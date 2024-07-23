from django import forms 
from .models import marca

class MarcaForm(forms.ModelForm):
    class Meta:
        model=marca
        fields='__all__'