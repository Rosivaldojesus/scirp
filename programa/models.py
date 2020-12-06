from django.db import models
from ckeditor.fields import *


# Create your models here.

class Gerenciadoras(models.Model):
    gerenciadora = models.CharField(max_length=255, blank=True, null=True, verbose_name='Gerenciadora: ')
    STATUS =(
        ("Online","Online"),
        ("Offline","Offline"),
    )
    statusGerenciadora = models.CharField(max_length=50, choices=STATUS, verbose_name='Status:')
    localizacao = models.CharField(max_length=255, blank=True, null=True, verbose_name='Localização: ')
    tagQuadro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Tag Quadro: ')

    class Meta:
        db_table = 'tbGerenciadoras'
        verbose_name_plural = 'Gerenciadoras'
    def __str__(self):
        return self.gerenciadora



class Sap(models.Model):
    quadroSap = models.CharField(max_length=50, blank=True, null=True, verbose_name='Quadros Automação: ')
    quadroEletrico = models.CharField(max_length=50, blank=True, null=True, verbose_name='Quadros Elétrico: ')
    STATUS =(
        ("Online","Online"),
        ("Offline","Offline"),
    )
    statusSap = models.CharField(max_length=50, choices=STATUS, verbose_name='Status')
    quantidadeControladoras = models.IntegerField(blank=True, null=True, verbose_name='Quantidade de Controladoras: ')
    localizacao = models.CharField(max_length=255, blank=True, null=True, verbose_name='Localização: ')
    Gerenciadora = models.ForeignKey(Gerenciadoras, on_delete=models.CASCADE)
    observacoesSap = RichTextField(blank=True, null=True)
    class Meta:
        db_table = 'tbSap'
        verbose_name_plural = 'Quadros SCIRP'
    def __str__(self):
        return self.quadroSap



class Cameras(models.Model):
    nomeCamera = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome Câmera: ')
    STATUS = (
        ("Online", "Online"),
        ("Offline", "Offline"),
    )
    statusCamera= models.CharField(max_length=50, choices=STATUS, verbose_name='Status')
    numeroCamera = models.IntegerField(blank=True, null=True, verbose_name='Número Câmera: ')
    numeroIp = models.CharField(max_length=20,blank=True, null=True, verbose_name='IP Câmera: ')
    FABRICANTE_CAMERA = (
        ("Axis", "Axis"),
        ("Interlbras", "Intelbras"),
    )
    fabricanteCamera = models.CharField(max_length=255, choices=FABRICANTE_CAMERA, )
    loginCamera = models.CharField(max_length=20, blank=True, null=True, verbose_name='Login: ')
    senhaCamera = models.CharField(max_length=20, blank=True, null=True, verbose_name='Senha: ')
    EQUIPAMENTO_GRAVACAO = (
        ("DVR 1", "DVR 1"),
        ("DVR 2", "DVR 2"),
        ("DVR 3", "DVR 3"),
        ("NVR 1", "NVR 1"),
        ("NVR 2", "NVR 2"),
        ("NVR 3", "NVR 3"),
        ("VAU 1", "VAU 1"),
        ("VAU 2", "VAU 2"),
        ("VAU 3", "VAU 3"),
    )
    equipamentoGravacao = models.CharField(max_length=50, choices=EQUIPAMENTO_GRAVACAO, verbose_name='Equipamento de Gravação: ')
    class Meta:
        db_table = 'tbCameraIp'
        verbose_name_plural = 'Câmeras IP'

    def __str__(self):
        return self.nomeCamera



class Suc(models.Model):
    suc = models.CharField(max_length=255, blank=True, null=True, verbose_name='SUC')
    nomeLoja = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome Loja')
    INTEGRACAO_SDAI = (
        ("SIM", "SIM"),
        ("NÃO", "NÃO"),
    )
    integracaoSdai = models.CharField(max_length=255, choices= INTEGRACAO_SDAI, verbose_name='Intergração SDAI' )

    MEDIDOR_ENERGIA = (
        ("SIM", "SIM"),
        ("NÃO", "NÃO")
    )
    medidorEnergia =  models.CharField(max_length=255, choices= MEDIDOR_ENERGIA, verbose_name='Medidor de Energia' )
    class Meta:
        db_table = 'tbSuc'
        verbose_name = 'SUC'

    def __str__(self):
        return self.suc    