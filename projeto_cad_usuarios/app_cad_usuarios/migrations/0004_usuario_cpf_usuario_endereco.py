# Generated by Django 4.2.4 on 2023-08-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0003_remove_usuario_cpf_remove_usuario_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cpf',
            field=models.IntegerField(default='cpf'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='endereco',
            field=models.TextField(default='endereco', max_length=250),
            preserve_default=False,
        ),
    ]
