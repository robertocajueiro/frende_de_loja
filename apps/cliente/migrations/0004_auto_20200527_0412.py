# Generated by Django 3.0.6 on 2020-05-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_cliente_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(help_text='Informe o contato do cliente', max_length=20),
        ),
    ]
