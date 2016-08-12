#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

'importação necessária para criar formulários com mais de uma model'
#from django.forms.models import inlineformset_factory

from .models import Animal, TutorEndTel

class TutorModelForm(forms.ModelForm):
	class Meta:
		model = TutorEndTel
		fields = ('_nome', '_email', '_cpf', '_logradouro', '_numero', '_bairro', '_cidade', '_cep', '_uf','_telefone', 'tipo')

"""
class EnderecoModelForm(forms.ModelForm):
	class Meta:
		model = Endereco
		fields = {'_logradouro', '_numero', '_bairro', '_cidade', '_cep', '_uf'}

class TelefoneModelForm(forms.ModelForm):
	class Meta:
		model = Telefone
		fields = {'_telefone', 'tipo'}
"""

class AnimalModelForm(forms.ModelForm):
	class Meta:
		model = Animal
		fields = {'_nome', '_rg', '_especie', '_raca', 'sexo', '_nascimento', '_idade'}
