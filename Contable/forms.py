from django import forms
from .models import ContaCapitulos

class CapituloForm(forms.ModelForm):
    class Meta:
        model=ContaCapitulos
        fields = "__all__"
    
