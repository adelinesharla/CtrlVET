#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

'importação necessária para criar formulários com mais de uma model'
#from django.forms.models import inlineformset_factory
from material import *
from .models import *
from localflavor.br.forms import BRCPFField
from datetime import datetime 

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

class ConsultaModelForm(forms.ModelForm):
	class Meta:
		model = Consulta
		fields = ('_retorno', 'animal', 'veterinario', '_data_realizacao')

	layout = Layout(
		Fieldset("Dados da Consulta"),
			Row('_data_realizacao','_retorno'),
			Row('animal', 'veterinario'),
		)
class ExameModelForm(forms.ModelForm):
	class Meta:
		model = Exame
		fields = ( 'animal', 'veterinario', 'tecnico')
		

	observacoes = forms.CharField()
	numero_amostra = forms.IntegerField()
	tutor = forms.CharField()

	layout = Layout(
		Fieldset("Dados do Exame"),
			Row(Span2('tecnico'), 'numero_amostra',),
		Fieldset("Dados Gerais"),
			Row('tutor', 'animal', 'veterinario'),
			Row('observacoes')
		)

class LaboratorioModelForm(forms.ModelForm):
	class Meta:
		model = Laboratorio
		fields = ('_nome','_local')
