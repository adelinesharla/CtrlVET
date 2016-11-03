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


'''			
class ConsultaModelForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ConsultaModelForm, self).__init__(*args, **kwargs)
		self.fields['cliente'].label = ''

	class Meta:
		model = Consulta
		fields = ('_retorno', 'animal', 'veterinario', '_data_realizacao', 'cliente')
		widgets = {
		'cliente': forms.HiddenInput()
		}

	layout = Layout(
		Fieldset("Dados da Consulta"),
			Row('_data_realizacao','_retorno'),
			Row('animal', 'veterinario'),
			Row('cliente')
		)
'''
