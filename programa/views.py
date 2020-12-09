from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

#Controle de acesso na Views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin





#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
# Create your views here.
@login_required(login_url='/login/')
def Index(request):
    qnt_online = Gerenciadoras.objects.filter(statusGerenciadora='Online').count()
    qnt_offline = Gerenciadoras.objects.filter(statusGerenciadora='Offline').count()
    qnt_quadros_on = Sap.objects.filter(statusSap = 'Online').count()
    qnt_quadros_off = Sap.objects.filter(statusSap = 'Offline').count()
    return render(request, 'index.html',{'qnt_online': qnt_online,
                                         'qnt_offline': qnt_offline,
                                         'qnt_quadros_on':  qnt_quadros_on,
                                         'qnt_quadros_off': qnt_quadros_off
                                         })


@login_required(login_url='/login/')
def Cftv_shopping(request):
    camera = Cameras.objects.all()
    return render(request, 'cftv-shopping.html', {'camera': camera})


@login_required(login_url='/login/')
def Cftv_shopping_create(request):
    form = CftvShoppingForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/cftv-shopping/')
    else:
        form = CftvShoppingForm()
    return render(request, 'cftv-shopping-create.html', {'form': form})


@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def Automacao(request):
    gerenciadoras = Gerenciadoras.objects.all()
    controladoras = Sap.objects.all()
    return render(request, 'automacao.html',{'gerenciadoras': gerenciadoras, 'controladoras':controladoras })


@login_required(login_url='/login/')
def Sdai_shopping(request):
    return render(request, 'sdai-shopping.html')


@login_required(login_url='/login/')
def Sdai_torre_empresarial(request):
    return render(request, 'sdai-torre-empresarial.html')


