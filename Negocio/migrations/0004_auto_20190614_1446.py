# Generated by Django 2.1.2 on 2019-06-14 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Negocio', '0003_auto_20190609_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': (('is_administrador', 'is administrador'), ('is_tecnico', 'is tecnico'), ('is_cliente', 'is cliente'))},
        ),
    ]