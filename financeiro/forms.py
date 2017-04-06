#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms
from django.forms.models import inlineformset_factory

'importação necessária para criar formulários com mais de uma model'
#from django.forms.models import inlineformset_factory
from material import *
from .models import *
from localflavor.br.forms import BRCPFField
from datetime import datetime 


class NotaModelForm(forms.ModelForm):
	class Meta:
		model = Nota
		fields = {'setor'}

	layout = Layout(
		Fieldset("Cadastro de Nota"),
			Row('setor'),
		)

class ItemNotaModelForm(forms.ModelForm):
	class Meta:
		model = ItemNota
		fields = {'_nome', '_valor'}

	layout = Layout(
		Fieldset("Itens da nota"),
			Row('_nome', '_valor'),
		)

class ProdutoModelForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = {'_nome', '_valor'}

	layout = Layout(
		Fieldset("Cadastro de Produto"),
			Row('_nome', '_valor'),
		)



