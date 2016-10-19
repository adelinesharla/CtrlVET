#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from cadastro.models import AtendimentoAbs 

#DAQUI PRA BAIXO SAO AS CLASSES DE NOTA,DEBITO E ITEMNOTA	

	
class Ano(models.Model):
	_ano = models.CharField(verbose_name='Ano',max_length=4)

	def get_absolute_url(self):
        	return reverse('ano_detail', kwargs={'pk': self.pk})

	def _get_ano(self):
		return self._ano

	def _set_ano(self, ano):
		self._ano = ano

	ano = property(_get_ano,_set_ano)
		
	def __unicode__(self):
		return u'%s - %s' % (self.nota, self._status)
	
	def __str__(self):
		return u'%s - %s' % (self.nota, self._status)
	
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

	def __unicode__(self):
		return u'%s - %s (R$)' % (self._nome, self.valor)		
		
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
	
	_data = models.DateField(auto_now_add=True)
	setor = models.CharField(verbose_name='Setor', max_length=30, choices=SETOR_CHOICES)
	atendimento = models.OneToOneField(AtendimentoAbs,on_delete=models.CASCADE,primary_key=True)
	status = models.BooleanField(verbose_name='Pago', default=False)
	ano = models.ForeignKey(Ano, on_delete = models.CASCADE, related_name='notas')
	itemNota = models.ManyToManyField(ItemNota, related_name='notas')

	class Meta:
			abstract = True

	def __unicode__(self):
		return u'%s - %s' % (self.setor, self._data)
	
class AcoesNota(NotaAbs):	
	class Meta:
			abstract = True
	
class Nota(AcoesNota):
	
	def get_absolute_url(self):
		return reverse('nota_detail', kwargs={'pk': self.pk})

	def _get_data(self):
		return self._data		
	
	def _set_data(self,data):
		self._data = data

	data = property(_get_data,_set_data)



class Produto(ItemNota):
	pass

class Servico(ItemNota):
	pass


