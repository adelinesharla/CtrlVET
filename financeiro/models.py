from __future__ import unicode_literals

from django.db import models

#DAQUI PRA BAIXO SAO AS CLASSES DE NOTA,DEBITO E ITEMNOTA		
class ItemNotaAbs(models.Model):
	_nome = models.CharField(verbose_name='Nome',max_length=150)
	_valor = models.DecimalField(verbose_name='Valor',max_digits=9, decimal_places=2)
	
	class Meta:
			abstract = True
			
class AcoesItemNota(ItemNotaAbs):
	class Meta:
			abstract = True
	
class ItemNota(AcoesItemNota):

	def _get_nome(self):
		return self._nome		
	
	def _set_nome(self,nome):
		self._nome = nome
		
	def _get_valor(self):
		return self._valor		
	
	def _set_valor(self,valor):
		self._valor = valor
		
	nome = property(_get_nome,_set_nome)	
	valor = property(_get_valor,_set_valor)						

class NotaAbs(models.Model):
	
	SETOR_CHOICES = (
		('1', 'Clínica de Pequenos'),
		('2', 'Clínica de Grandes'),
		('3', 'Clínica Cirúrgica'),
		('4', 'Patologia Clínica'),
		('5', 'Diagnóstico por Imagem'),
		('6', 'Parasitologia'),
		('7', 'Microbiologia'),
		('8', 'Patologia Animal'),
	 )
	
	_data = models.DateField(verbose_name='Data')
	setor = models.CharField(verbose_name='Setor', max_length=30, choices=SETOR_CHOICES)
	
	class Meta:
			abstract = True
	
class AcoesNota(NotaAbs):

	class Meta:
			abstract = True
	
class Nota(AcoesNota):

	def _get_data(self):
		return self._data		
	
	def _set_data(self,data):
		self._data = data
		
	data = property(_get_data,_set_data)	
	
class Debito(models.Model):	
	itemNota = models.ForeignKey(ItemNota, on_delete = models.CASCADE)
	nota = models.ForeignKey(Nota, on_delete = models.CASCADE)	
