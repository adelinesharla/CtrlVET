# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('rg', models.PositiveSmallIntegerField(unique=True, verbose_name='RG')),
                ('especie', models.CharField(max_length=50, verbose_name='Esp\xe9cie')),
                ('raca', models.CharField(max_length=50, verbose_name='Ra\xe7a')),
                ('sexo', models.CharField(choices=[('FE', 'Feminino'), ('MA', 'Masculino')], max_length=15, verbose_name='Sexo')),
                ('nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('idade', models.PositiveSmallIntegerField(max_length=3, verbose_name='Idade')),
            ],
            options={
                'verbose_name_plural': 'Animais',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('numero', models.PositiveSmallIntegerField(verbose_name='N\xfamero')),
                ('bairro', models.CharField(max_length=20, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('cep', models.CharField(max_length=15, verbose_name='CEP')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=10, verbose_name='UF')),
            ],
            options={
                'verbose_name_plural': 'Endere\xe7os',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.PositiveSmallIntegerField(max_length=15, verbose_name='Telefone')),
                ('tipo', models.CharField(choices=[('Fixo', 'Fixo'), ('Celular', 'Celular')], max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('cpf', models.PositiveSmallIntegerField(max_length=11, verbose_name='CPF')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Endereco')),
                ('telefone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Telefone')),
            ],
            options={
                'verbose_name_plural': 'Tutores',
            },
        ),
        migrations.AddField(
            model_name='animal',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Tutor'),
        ),
    ]
