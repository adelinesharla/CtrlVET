#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

'importação necessária para criar formulários com mais de uma model'
#from django.forms.models import inlineformset_factory
from material import *
from .models import *
from localflavor.br.forms import BRCPFField
from datetime import datetime
from .models import GENERO_CHOICES, STATE_CHOICES


class TutorModelForm(forms.ModelForm):
	_cpf = BRCPFField()
	class Meta:
		model = TutorEndTel
		fields = ('_nome', '_email', '_cpf', '_logradouro', '_numero', '_bairro', '_cidade', '_cep', '_uf','_telefone1','_telefone2')

	layout = Layout(
		Fieldset("Dados pessoais"),
			Row(Span2('_nome'), '_cpf'),
		Fieldset("Contato"),
			Row(Span2('_telefone1'), Span2('_telefone2'), Span2('_email')),
		Fieldset("Endereço"),
			Row(Span3('_logradouro'), '_numero'),
			Row(Span2('_bairro'), Span2('_cidade'), '_cep', ('_uf')),
		)

class TutorModelFormDisable(forms.ModelForm):
	_cpf = BRCPFField()
	_uf = forms.CharField(label='UF', max_length=20, required=False)
	
	def __init__(self, readonly_form=False, *args, **kwargs):
		super(TutorModelFormDisable, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['readonly'] = True
		self.fields['_uf'].widget.attrs['disabled'] = True

	class Meta:
		model = TutorEndTel
		fields = ('_nome', '_email', '_cpf', '_logradouro', '_numero', '_bairro', '_cidade', '_cep', '_uf','_telefone1','_telefone2')
    

	layout = Layout(
		Fieldset("Dados pessoais"),
			Row(Span2('_nome'), '_cpf'),
		Fieldset("Contato"),
			Row(Span2('_telefone1'), Span2('_telefone2'), Span2('_email')),
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
	def __init__(self, *args, **kwargs):
		super(AnimalModelForm, self).__init__(*args, **kwargs)
		self.fields['_obito'].label = ''
		
	class Meta:
		model = Animal
		fields = {'_nome', '_rg', '_especie', '_raca', 'sexo', '_nascimento', '_obito', '_idade', 'tutor'}
		widgets = {
		'_obito': forms.HiddenInput(),
		}

	layout = Layout(
		Fieldset("Dados do Animal"),
			Row('_nome', 'sexo', '_rg'),
			Row('_especie', '_raca'),
			Row('_nascimento', '_idade'),
			Row('_obito'),
		Fieldset("Dados do Tutor"),
			Row('tutor')
		)

class AnimalModelFormDisable(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(AnimalModelFormDisable, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['readonly'] = True
		self.fields['sexo'].widget.attrs['disabled'] = True
		self.fields['tutor'].widget.attrs['disabled'] = True
		self.fields['_nascimento'].widget.attrs['disabled'] = True
		self.fields['_obito'].widget.attrs['disabled'] = True

	class Meta:
		model = Animal
		fields = {'_nome', '_rg', '_especie', '_raca', 'sexo', '_nascimento', '_obito', '_idade', 'tutor'}



	layout = Layout(
		Fieldset("Dados do Animal"),
			Row('_nome', 'sexo', '_rg'),
			Row('_especie', '_raca'),
			Row('_nascimento', '_idade', '_obito'),
		Fieldset("Dados do Tutor"),
			Row('tutor')
		)

class AnimalObitoForm(forms.ModelForm):
	class Meta:
		model = Animal
		fields = {'_nome', '_rg', '_especie', '_raca', 'sexo', '_nascimento', '_obito', '_idade', 'tutor'}
		widgets = {
		'_nome': forms.HiddenInput(),
		'_rg': forms.HiddenInput(),
		'_especie': forms.HiddenInput(),
		'_raca': forms.HiddenInput(),
		'sexo': forms.HiddenInput(),
		'_nascimento': forms.HiddenInput(),
		'_idade': forms.HiddenInput(),
		'tutor': forms.HiddenInput()
		}

	layout = Layout(
		Fieldset("Data de Óbito"),
			Row('_obito'),
		)

class AnimalBuscaAdvForm(forms.Form):
	_animal = forms.CharField(label='Nome do Animal', max_length=50, required=False)
	_rg = forms.IntegerField(label='RG', required=False)
	_especie = forms.CharField(label='Especie', max_length=50, required=False)
	_raca = forms.CharField(label='Raca', max_length=50, required=False)
	sexo = forms.ChoiceField(label = 'Sexo', widget=forms.Select, choices=GENERO_CHOICES, required=False)
	_idade = forms.IntegerField(label='Idade', required=False)
	_tutor = forms.CharField(label='Nome do Tutor', max_length=50, required=False)
	#_cpf = forms.CharField(label='CPF', max_length=11, required=False)

	layout = Layout(
		Fieldset("Dados do Animal"),
			Row('_animal', 'sexo', '_rg'),
			Row('_especie', '_raca', '_idade'),
		Fieldset("Dados do Tutor"),
			Row('_tutor'),
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

class ConsultaModelFormDisable(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ConsultaModelFormDisable, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['readonly'] = True
		self.fields['animal'].widget.attrs['disabled'] = True
		self.fields['veterinario'].widget.attrs['disabled'] = True
		self.fields['_data_realizacao'].widget.attrs['disabled'] = True
		self.fields['_retorno'].widget.attrs['disabled'] = True

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
		
class ExameModelFormDisable(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ExameModelFormDisable, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['readonly'] = True
		self.fields['veterinario'].widget.attrs['disabled'] = True
		self.fields['animal'].widget.attrs['disabled'] = True
		self.fields['cliente'].widget.attrs['disabled'] = True
		self.fields['tecnico'].widget.attrs['disabled'] = True
		self.fields['laboratorio'].widget.attrs['disabled'] = True

	class Meta:
		model = Exame
		fields = ( 'animal', 'veterinario', 'tecnico', 'cliente', 'laboratorio', 'numero_amostra', 'observacoes')

	layout = Layout(
		Fieldset("Dados do Exame"),
			Row('laboratorio'),
			Row(Span2('tecnico'), 'numero_amostra',),
		Fieldset("Dados Gerais"),
			Row('cliente', 'animal', 'veterinario'),
			Row('observacoes')
		)

class ExameModelForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ConsultaModelForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['readonly'] = True

	def __init__(self, *args, **kwargs):
		super(ExameModelForm, self).__init__(*args, **kwargs)
		self.fields['laboratorio'].label = ''

	class Meta:
		model = Exame
		fields = ( 'animal', 'veterinario', 'tecnico', 'cliente', 'laboratorio', 'numero_amostra', 'observacoes')
		widgets = {'laboratorio': forms.HiddenInput()}

	layout = Layout(
		Fieldset("Dados do Exame"),
			Row(Span2('tecnico'), 'numero_amostra',),
		Fieldset("Dados Gerais"),
			Row('cliente', 'animal', 'veterinario'),
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
	
		
		
