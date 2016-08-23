#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

'importação necessária para criar formulários com mais de uma model'
#from django.forms.models import inlineformset_factory
from material import *
from .models import *
from localflavor.br.forms import BRCPFField

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

	auto_chave = forms.BooleanField(required=False, label='Auto rg')

	layout = Layout(
		Fieldset("Dados do Animal"),
			Row('_nome', 'sexo', '_rg', 'auto_chave'),
			Row('_especie', '_raca'),
			Row('_nascimento', '_idade'),
		Fieldset("Dados do Tutor"),
			Row('tutor')
		)

class ConsultaModelForm(forms.ModelForm):
	class Meta:
		model = Consulta
		fields = ('_data','_diagnostico', '_retorno', 'animal', 'veterinario')

class ExameModelForm(forms.ModelForm):
	class Meta:
		model = Exame
		fields = ('_data','_diagnostico', 'animal', 'veterinario', 'tecnico', '_resultado')
