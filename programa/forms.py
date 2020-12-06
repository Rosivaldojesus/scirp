from django import forms
from .models import Cameras

class CftvShoppingForm(forms.ModelForm):
    class Meta:
        model = Cameras
        fields = ['numeroCamera','statusCamera','nomeCamera','numeroIp','fabricanteCamera','loginCamera','senhaCamera','equipamentoGravacao']


