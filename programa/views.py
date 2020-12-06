from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import CftvShoppingForm

# Create your views here.
def Index(request):
    return render(request, 'index.html')


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def Cftv_shopping(request):
    camera = Cameras.objects.all()
    return render(request, 'cftv-shopping.html', {'camera': camera})


def Cftv_shopping_create(request):
    form = CftvShoppingForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/cftv-shopping/')
    else:
        form = CftvShoppingForm()
    return render(request, 'cftv-shopping-create.html', {'form': form})


def Cftv_shopping_update(request, id=None):
    camera = get_object_or_404(Cameras, id=id)
    form = CftvShoppingForm(request.POST or None, instance=camera)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/cftv-shopping/')
    return render(request, 'cftv-shopping-update.html', {'form': form})
   

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------


def Automacao(request):
    gerenciadoras = Gerenciadoras.objects.all()
    controladoras = Sap.objects.all()
    return render(request, 'automacao.html',{'gerenciadoras': gerenciadoras, 'controladoras':controladoras } )

def Sdai_shopping(request):
    return render(request, 'sdai-shopping.html')

def Sdai_torre_empresarial(request):
    return render(request, 'sdai-torre-empresarial.html')


