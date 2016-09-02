# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('_rg', models.PositiveSmallIntegerField(unique=True, verbose_name='RG')),
                ('_especie', models.CharField(max_length=50, verbose_name='Esp\xe9cie')),
                ('_raca', models.CharField(max_length=50, verbose_name='Ra\xe7a')),
                ('sexo', models.CharField(max_length=15, verbose_name='Sexo', choices=[('FE', 'Feminino'), ('MA', 'Masculino')])),
                ('_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('_idade', models.PositiveSmallIntegerField(verbose_name='Idade')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_data', models.DateField(auto_now_add=True)),
                ('_diagnostico', models.TextField(default='Pendente', max_length=200, verbose_name='Diagn\xf3stico', blank=True)),
                ('_retorno', models.BooleanField(default='False')),
                ('_data_realizacao', models.DateField(verbose_name='Data Agendada')),
                ('animal', models.ForeignKey(related_name='a_ser_consultado', to='cadastro.Animal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Debito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_data', models.DateField(auto_now_add=True)),
                ('_diagnostico', models.TextField(default='Pendente', max_length=200, verbose_name='Diagn\xf3stico', blank=True)),
                ('_resultado', models.TextField(default='Pendente', max_length=200, verbose_name='Resultado', blank=True)),
                ('estadoexame', models.BooleanField(verbose_name='Estado do Exame')),
                ('animal', models.ForeignKey(related_name='amostrado_para_exame', blank=True, to='cadastro.Animal', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemNota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('_valor', models.DecimalField(verbose_name='Valor', max_digits=9, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('_local', models.CharField(max_length=50, verbose_name='local')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_data', models.DateField(verbose_name='Data')),
                ('setor', models.CharField(max_length=30, verbose_name='Setor', choices=[('1', 'Cl\xednica de Pequenos'), ('2', 'Cl\xednica de Grandes'), ('3', 'Cl\xednica Cir\xfargica'), ('4', 'Patologia Cl\xednica'), ('5', 'Diagn\xf3stico por Imagem'), ('6', 'Parasitologia'), ('7', 'Microbiologia'), ('8', 'Patologia Animal')])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('_email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('_cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('_crf', models.CharField(max_length=10, verbose_name='CRF')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Tecnicos',
            },
        ),
        migrations.CreateModel(
            name='TutorEndTel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_logradouro', models.CharField(max_length=200, verbose_name='Logradouro')),
                ('_numero', models.PositiveSmallIntegerField(verbose_name='N\xfamero')),
                ('_bairro', models.CharField(max_length=20, verbose_name='Bairro')),
                ('_cidade', models.CharField(max_length=200, verbose_name='Cidade')),
                ('_cep', models.CharField(max_length=15, verbose_name='CEP')),
                ('_uf', models.CharField(max_length=10, verbose_name='UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
                ('_telefone', models.CharField(blank=True, max_length=15, verbose_name='Telefone', validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="O formato do n\xfamero de telefone deve ser: '+999999999'. S\xe3o Permitidos at\xe9 15 d\xedgitos.")])),
                ('tipo', models.CharField(max_length=15, choices=[('Fixo', 'Fixo'), ('Celular', 'Celular')])),
                ('_nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('_email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('_cpf', models.CharField(max_length=11, verbose_name='CPF')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('_email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('_cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('_crmv', models.CharField(max_length=10, verbose_name='CRMV')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Veterinarios',
            },
        ),
        migrations.AddField(
            model_name='exame',
            name='laboratorio',
            field=models.ForeignKey(to='cadastro.Laboratorio'),
        ),
        migrations.AddField(
            model_name='exame',
            name='tecnico',
            field=models.ForeignKey(related_name='realiza_exame', blank=True, to='cadastro.Tecnico', null=True),
        ),
        migrations.AddField(
            model_name='exame',
            name='tutor',
            field=models.ForeignKey(related_name='dono_da_amostra', to='cadastro.TutorEndTel'),
        ),
        migrations.AddField(
            model_name='exame',
            name='veterinario',
            field=models.ForeignKey(related_name='realiza_diagnostico', to='cadastro.Veterinario'),
        ),
        migrations.AddField(
            model_name='debito',
            name='itemNota',
            field=models.ForeignKey(to='cadastro.ItemNota'),
        ),
        migrations.AddField(
            model_name='debito',
            name='nota',
            field=models.ForeignKey(to='cadastro.Nota'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='veterinario',
            field=models.ForeignKey(related_name='realiza_consulta', to='cadastro.Veterinario'),
        ),
        migrations.AddField(
            model_name='animal',
            name='tutor',
            field=models.ForeignKey(to='cadastro.TutorEndTel'),
        ),
    ]
