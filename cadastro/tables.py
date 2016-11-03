# -*- encoding: utf-8 -*-
import django_tables2 as tables
from django_tables2.utils import A
from .models import *
from django.contrib.humanize.templatetags.humanize import intcomma

class ColumnWithThousandsSeparator(tables.Column):
	def render(self,value):
		return intcomma(value)

class ColumnWithTelefoneFormat(tables.Column):
	def render(self,value):
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

class TutorEndTelTable(tables.Table):	
	#attrs={'th': {'class': 'center'}, 'td': {'class': 'center'}} alinhamento
	pk = tables.LinkColumn('tutor_detalhes', args=[A('pk')], verbose_name= 'ID')
	_nome = tables.LinkColumn('tutor_detalhes', args=[A('pk')])
	editar = tables.LinkColumn('tutor_editar', text='Editar', args=[A('pk')],  orderable=False)
	excluir = tables.LinkColumn('tutor_deletar', text='Excluir', args=[A('pk')], orderable=False )
	_telefone1 = ColumnWithTelefoneFormat(verbose_name= 'Telefone', orderable=False)
	empty_text = 'Nenhum tutor encontrado.'


	class Meta:
		model = TutorEndTel
		template = 'tables_base.html'
		fields = ('pk', '_nome', '_cidade','_email', '_telefone1', 'editar', 'excluir')
		sequence = ('pk', '_nome', '_cidade','_email', '_telefone1', 'editar', 'excluir')
		attrs = {'class': 'highlight striped'}

class AnimalTable(tables.Table):	
	_nome = tables.LinkColumn('animal_detalhes', args=[A('pk')])
	tutor = tables.LinkColumn('tutor_detalhes', args=[A('pk')])
	editar = tables.LinkColumn('animal_editar', text='Editar', args=[A('pk')],  orderable=False)
	excluir = tables.LinkColumn('animal_deletar', text='Excluir', args=[A('pk')], orderable=False )

	class Meta:
		model = Animal
		template = 'tables_base.html'
		fields = ('_rg', '_nome', '_especie', '_idade', 'tutor', 'editar', 'excluir')
		sequence = ('_rg', '_nome', '_especie', '_idade', 'tutor', 'editar', 'excluir')
		attrs = {'class': 'highlight striped'}
		empty_text = 'Nenhum animal encontrado.'

class ExameTable(tables.Table):
	cliente = tables.LinkColumn('tutor_detalhes', args=[A('pk')], verbose_name='Responsável')
	animal = tables.LinkColumn('animal_detalhes', args=[A('pk')], verbose_name='Animal')
	_data = tables.DateColumn(short=True)
	editar = tables.LinkColumn('exame_editar', text='Editar', args=[A('pk')],  orderable=False)
	excluir = tables.LinkColumn('exame_deletar', text='Excluir', args=[A('pk')], orderable=False )
	
	class Meta:
		model = Exame
		template = 'tables_base.html'
		fields = ('_data', 'numero_amostra', 'cliente','animal',  'veterinario', 'tecnico', 'editar', 'excluir' )
		sequence = ('_data', 'numero_amostra', 'cliente', 'animal',  'veterinario', 'tecnico', 'editar', 'excluir')
		attrs = {'class': 'highlight striped'}
		empty_text = 'Nenhum exame encontrado.'

class ConsultaTable(tables.Table):
	animal = tables.LinkColumn('animal_detalhes',  args=[A('pk')], verbose_name='Animal')
	cliente = tables.LinkColumn('tutor_detalhes',  args=[A('pk')], verbose_name='Cliente')
	veterinario = tables.Column(verbose_name='Veterinário')
	_data_realizacao = tables.DateColumn(short=True)
	editar = tables.LinkColumn('consulta_editar', text='Editar', args=[A('pk')],  orderable=False)
	excluir = tables.LinkColumn('consulta_deletar', text='Excluir', args=[A('pk')], orderable=False )

	
	class Meta:
		model = Consulta
		template = 'tables_base.html'
		fields = ('_data_realizacao', 'animal', 'cliente', 'veterinario', 'editar', 'excluir')
		sequence = ('_data_realizacao', 'animal', 'cliente','veterinario', 'editar', 'excluir')
		attrs = {'class': 'highlight striped'}
		empty_text = 'Nenhuma consulta encontrado.'

