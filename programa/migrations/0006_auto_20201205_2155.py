# Generated by Django 3.0 on 2020-12-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0005_auto_20201205_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suc',
            name='integracaoSdai',
            field=models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=255, verbose_name='Intergração SDAI'),
        ),
        migrations.AlterField(
            model_name='suc',
            name='medidorEnergia',
            field=models.CharField(choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=255, verbose_name='Medidor de Energia'),
        ),
        migrations.AlterField(
            model_name='suc',
            name='nomeLoja',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome Loja'),
        ),
        migrations.AlterField(
            model_name='suc',
            name='suc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='SUC'),
        ),
    ]
