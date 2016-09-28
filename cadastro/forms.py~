#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

'importação necessária para criar formulários com mais de uma model'
#from django.forms.models import inlineformset_factory
from material import *
from .models import *
from localflavor.br.forms import BRCPFField
from datetime import datetime
from localflavor.br.forms import STATE_CHOICES
from .models import GENERO_CHOICES


class TutorModelForm(forms.ModelForm):
	_cpf = BRCPFField()
	class Meta:
		model = TutorEndTel
		fields = ('_nome', '_email', '_cpf', '_logradouro', '_numero', '_bairro', '_cidade', '_cep', '_uf','_telefone', 'tipo')

	layout = Layout(
		Fieldset("Dados pessoais"),
			Row('_nome', '_cpf'),
		Fieldset("Contato"),
			Row('_email'),
			Row(Span3('_telefone'), 'tipo'),
		Fieldset("Endereço"),
			Row(Span3('_logradouro'), '_numero'),
			Row(Span2('_bairro'), Span2('_cidade'), '_cep', ('_uf')),
		)

class TutorBuscaAdvForm(forms.Form):
	_nome = forms.CharField(label='Nome', max_length=50, required=False)
	_email = forms.EmailField(label='E-Mail', required=False)
	_cpf = forms.CharField(label='CPF', max_length=11, required=False)
	_bairro = forms.CharField(label='Bairro', max_length=20, required=False)
	_cidade = forms.CharField(label='Cidade', max_length=200, required=False)
	_cep = forms.CharField(label = 'CEP', max_length=15, required=False)
	_uf = forms.ChoiceField(label = 'UF', widget=forms.Select, choices=STATE_CHOICES, required=False)

	layout = Layout(
		Row('_nome', '_cpf'),
		Row('_email'),
		Row(Span2('_bairro'), Span2('_cidade'), '_cep', ('_uf')),
		)

class AnimalModelForm(forms.ModelForm):
	class Meta:
		model = Animal
		fields = {'_nome', '_rg', '_especie', '_raca', 'sexo', '_nascimento', '_idade', 'tutor'}

	

	layout = Layout(
		Fieldset("Dados do Animal"),
			Row('_nome', 'sexo', '_rg'),
			Row('_especie', '_raca'),
			Row('_nascimento', '_idade'),
		Fieldset("Dados do Tutor"),
			Row('tutor')
		)

class AnimalBuscaAdvForm(forms.Form):
	_nome = forms.CharField(label='Nome', max_length=50, required=False)
	_rg = forms.IntegerField(label='RG', required=False)
	_especie = forms.CharField(label='Especie', max_length=50, required=False)
	_raca = forms.CharField(label='Raca', max_length=50, required=False)
	sexo = forms.ChoiceField(label = 'Sexo', widget=forms.Select, choices=GENERO_CHOICES, required=False)
	_idade = forms.IntegerField(label='Idade', required=False)
	_tutor = forms.CharField(label='Tutor', max_length=50, required=False)
	
	layout = Layout(
		Row('_nome', 'sexo', '_rg'),
		Row('_especie', '_raca'),
		Row('_tutor', '_idade'),
		)
				
class ConsultaModelForm(forms.ModelForm):
	class Meta:
		model = Consulta
		fields = ('_retorno', 'animal', 'veterinario', '_data_realizacao')

	layout = Layout(
		Fieldset("Dados da Consulta"),
			Row('_data_realizacao','_retorno'),
			Row('animal', 'veterinario'),
		)
		
class ConsultaBuscaAdvForm(forms.Form):
	_animal = forms.CharField(label='Animal', max_length=50, required=False)
	_veterinario = forms.CharField(label='Veterinario', max_length=50, required=False)
	_data = forms.DateField(label='Data', required=False)
	
	layout = Layout(
		Row('_animal', '_veterinario'),
		Row('_data'),	
		)
		
class ExameModelForm(forms.ModelForm):
	class Meta:
		model = Exame
		fields = ( 'animal', 'veterinario', 'tecnico', 'tutor', 'laboratorio')
		

	observacoes = forms.CharField()
	numero_amostra = forms.IntegerField()

	layout = Layout(
		Fieldset("Dados do Exame"),
			Row(Span2('tecnico'), 'numero_amostra',),
		Fieldset("Dados Gerais"),
			Row('tutor', 'animal', 'veterinario'),
			Row('observacoes', 'laboratorio')
		)
		
class ExameBuscaAdvForm(forms.Form):		
	_animal = forms.CharField(label='Animal', max_length=50, required=False)
	_veterinario = forms.CharField(label='Veterinario', max_length=50, required=False)
	_tecnico = forms.CharField(label='Tecnico', max_length=50, required=False)
	_tutor = forms.CharField(label='Tutor', max_length=50, required=False)
	_laboratorio = forms.CharField(label='Laboratorio', max_length=50, required=False)
	
	layout = Layout(
			Row(Span2('_tecnico')),
			Row('_tutor', '_animal', '_veterinario'),
			Row('_laboratorio')
		)


class LaboratorioModelForm(forms.ModelForm):
	class Meta:
		model = Laboratorio
		fields = ('_nome','_local')
	
		
		
