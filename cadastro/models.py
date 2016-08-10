from __future__ import unicode_literals

from django.db import models


import datetime
from django.utils import timezone

'Tradução e estados para PT-BR'
from django.utils.translation import ugettext_lazy as _
from localflavor.br.forms import STATE_CHOICES

#from django.core.exceptions import ValidationError

'Estas classes implementam os campos de Tutor do Subsistema Secretaria e sua respectivas regras de negócio.'

class Endereco(models.Model):
	logradouro = models.CharField(verbose_name='Logradouro', max_length=200)
	numero = models.PositiveSmallIntegerField(verbose_name='Número')
	bairro = models.CharField(verbose_name='Bairro', max_length=20)
	cidade = models.CharField(verbose_name='Cidade', max_length=200)
	cep = models.CharField(verbose_name = 'CEP', max_length=15)
	uf = models.CharField(verbose_name = 'UF', max_length=10, choices=STATE_CHOICES)

	def __unicode__(self):
		return u'%s %s' % (self.logradouro, self.numero)

	class Meta:
		verbose_name_plural = "Endereços"

class Telefone(models.Model):
	TIPO_CHOICES = (
		('Fixo', 'Fixo'),
		('Celular', 'Celular'),
    )
	telefone =  models.PositiveSmallIntegerField(verbose_name='Telefone', max_length=15)
	tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)

	
	def __unicode__(self):
		return u'%s' % (self.telefone)

	class Meta:
		verbose_name_plural = "Telefones"

class Tutor(models.Model):
	nome = models.CharField(verbose_name='Nome', max_length=50)
	email = models.EmailField(verbose_name='E-Mail')
	cpf = models.PositiveSmallIntegerField(verbose_name='CPF', max_length=11)
	endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE)
	telefone = models.ForeignKey(Telefone, on_delete = models.CASCADE)

	def __unicode__(self):
		return u'%s %s' % (self.nome, self.cpf)

	class Meta:
		verbose_name_plural = "Tutores"

class Animal(models.Model):
	GENERO_CHOICES = (
		('FE', 'Feminino'),
		('MA', 'Masculino'),
    )
	nome = models.CharField(verbose_name='Nome', max_length=50)
	rg = models.PositiveSmallIntegerField(verbose_name='RG', unique=True)
	especie = models.CharField(verbose_name='Espécie', max_length=50)
	raca = models.CharField(verbose_name='Raça', max_length=50)
	sexo = models.CharField(verbose_name='Sexo', max_length=15, choices=GENERO_CHOICES)
	nascimento = models.DateField(verbose_name='Data de Nascimento')
	idade = models.PositiveSmallIntegerField(verbose_name='Idade', max_length=3)
	tutor = models.ForeignKey(Tutor, on_delete = models.CASCADE)
	
	def __unicode__(self):
		return u'%s %s' % (self.nome, self.rg)

	class Meta:
		verbose_name_plural = "Animais"

