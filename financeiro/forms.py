#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

'importação necessária para criar formulários com mais de uma model'
#from django.forms.models import inlineformset_factory
from material import *
from .models import *
from localflavor.br.forms import BRCPFField
from datetime import datetime 

class DebitoModelForm(forms.ModelForm):
	class Meta:
		model = Debito
		fields = {'itemNota', 'nota'}

	layout = Layout(
		)

class NotaModelForm(forms.ModelForm):
	class Meta:
		model = Nota
		fields = {'_data', '_setor'}

	layout = Layout(
		)

class ProdutoModelForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = {'_nome', '_valor'}

	layout = Layout(
		)

class ServicoModelForm(forms.ModelForm):
	class Meta:
		model = Debito
		fields = {'_nome', '_valor'}

	layout = Layout(
		)


