#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

'importação necessária para criar formulários com mais de uma model'
#from django.forms.models import inlineformset_factory

from .models import *

class TutorModelForm(forms.ModelForm):
	class Meta:
		model = Tutor
		fields = ('nome', 'email', 'cpf')

class EnderecoModelForm(forms.ModelForm):
	class Meta:
		model = Endereco
		fields = {'logradouro', 'numero', 'bairro', 'cidade', 'cep', 'uf'}

class TelefoneModelForm(forms.ModelForm):
	class Meta:
		model = Telefone
		fields = {'telefone', 'tipo'}
		