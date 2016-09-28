# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-28 18:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_ano', models.CharField(max_length=4, verbose_name='Ano')),
            ],
        ),
        migrations.CreateModel(
            name='Debito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Pago')),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debitos', to='financeiro.Ano')),
            ],
        ),
        migrations.CreateModel(
            name='ItemNota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('_valor', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('_data', models.DateField(auto_now_add=True)),
                ('setor', models.CharField(choices=[('1', 'Cl\xednica de Pequenos'), ('2', 'Cl\xednica de Grandes'), ('3', 'Cl\xednica Cir\xfargica'), ('4', 'Patologia Cl\xednica'), ('5', 'Diagn\xf3stico por Imagem'), ('6', 'Parasitologia'), ('7', 'Microbiologia'), ('8', 'Patologia Animal')], max_length=30, verbose_name='Setor')),
                ('atendimento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cadastro.AtendimentoAbs')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('itemnota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.ItemNota')),
            ],
            options={
                'abstract': False,
            },
            bases=('financeiro.itemnota',),
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('itemnota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='financeiro.ItemNota')),
            ],
            options={
                'abstract': False,
            },
            bases=('financeiro.itemnota',),
        ),
        migrations.AddField(
            model_name='debito',
            name='itemNota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.ItemNota'),
        ),
        migrations.AddField(
            model_name='debito',
            name='nota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financeiro.Nota'),
        ),
    ]
