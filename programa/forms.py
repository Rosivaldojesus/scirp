from django import forms
from .models import *

class CftvShoppingForm(forms.ModelForm):
    class Meta:
        model = Cameras
        fields = ['numeroCamera','statusCamera','nomeCamera','numeroIp','fabricanteCamera','loginCamera','senhaCamera','equipamentoGravacao']


class SapForm(forms.ModelForm):
    class Meta:
        model = Sap
        fields = ['quadroSap','quadroEletrico','statusSap','quantidadeControladoras','localizacao','Gerenciadora','observacoesSap']