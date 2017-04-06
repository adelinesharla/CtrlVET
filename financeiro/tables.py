# -*- encoding: utf-8 -*-
import django_tables2 as tables
from django_tables2.utils import A
from .models import *
from django.contrib.humanize.templatetags.humanize import intcomma

class ColumnWithThousandsSeparator(tables.Column):
	def render(self,value):
		return intcomma(value)

class ColumnWithTelefoneFormat(tables.Column):
	
	def render(self, value):
		if value == 10:
			first = value[0:2]
			second = value[2:6]
			third = value[6:15]
			return '(' + first + ')' + ' ' + second + '-' + third
		else:
			first = value[0:2]
			second = value[2:7]
			third = value[7:15]
			return '(' + first + ')' + ' ' + second + '-' + third


class PagamentosTable(tables.Table):
	_data = tables.DateColumn(short=True, format='date')

	class Meta:
		model = Nota
		template = 'tables_base.html'
		fields = ('pk','_data', 'setor', 'cliente', 'valor')
		sequence = ('pk','_data', 'setor', 'cliente', 'valor')
		attrs = {'class': 'highlight striped'}
		empty_text = 'Nenhuma pagamento encontrado.'