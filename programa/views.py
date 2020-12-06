from django.shortcuts import render
from .models import *

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Cftv_shopping(request):
    camera = Cameras.objects.all()
    return render(request, 'cftv-shopping.html', {'camera': camera})

def Automacao(request):
    gerenciadoras = Gerenciadoras.objects.all()
    return render(request, 'automacao.html',{'gerenciadoras': gerenciadoras} )

def Sdai_shopping(request):
    return render(request, 'sdai-shopping.html')

def Sdai_torre_empresarial(request):
    return render(request, 'sdai-torre-empresarial.html')


