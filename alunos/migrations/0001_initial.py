# Generated by Django 4.2.4 on 2023-08-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_nascimento', models.DateField(default='01/01/2000')),
                ('data_ingresso', models.DateField(default='2023-02-01', verbose_name='Data de Ingresso')),
                ('foto', models.ImageField(upload_to='')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('rg', models.CharField(max_length=8, verbose_name='RG')),
                ('curso', models.CharField(choices=[('BSI', 'BSI'), ('TADS', 'TADS')], max_length=15, verbose_name='Curso')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('test', models.CharField(max_length=50)),
            ],
        ),
    ]
