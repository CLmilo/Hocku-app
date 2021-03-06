# Generated by Django 3.2.6 on 2021-09-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionProductos', '0003_auto_20210908_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componente_costo',
            name='valor',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='conversion_moneda',
            name='factor',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sobre_costo',
            name='monto',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sobre_costo',
            name='rangomin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sobre_costo',
            name='rangomx',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
