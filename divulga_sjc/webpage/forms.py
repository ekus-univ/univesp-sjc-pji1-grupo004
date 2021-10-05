from django import forms
from .models import Negocio

class NegocioCreateForm(forms.ModelForm):
    class Meta:
        model = Negocio
        fields = "__all__"
