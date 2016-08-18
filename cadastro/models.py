# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.views.generic.list import ListView,View
import abc
import datetime
from django.utils import timezone

'Tradução e estados para PT-BR'
from django.utils.translation import ugettext_lazy as _
from localflavor.br.forms import STATE_CHOICES

#from django.core.exceptions import ValidationError

'Estas classes implementam os campos de Tutor do Subsistema Secretaria e sua respectivas regras de negócio.'

class EnderecoAbs(models.Model):
	_logradouro = models.CharField(verbose_name='Logradouro', max_length=200)
	_numero = models.PositiveSmallIntegerField(verbose_name='Número')
	_bairro = models.CharField(verbose_name='Bairro', max_length=20)
	_cidade = models.CharField(verbose_name='Cidade', max_length=200)
	_cep = models.CharField(verbose_name = 'CEP', max_length=15)
	_uf = models.CharField(verbose_name = 'UF', max_length=10, choices=STATE_CHOICES)
	
	class Meta:
		abstract = True	


class AcoesEndereco(EnderecoAbs):
	def __unicode__(self):
		return u'%s %s' % (self.logradouro, self.numero)

	class Meta:
		verbose_name_plural = "Endereços"
		abstract = True			


class Endereco(AcoesEndereco):
	def _get_logradouro(self):
		return self._logradouro
		
	def _get_numero(self):
		return self._numero
	
	def _get_bairro(self):
		return self._bairro
	
	def _get_cidade(self):
		return self._cidade
		
	def _get_cep(self):
		return self._cep
	
	def _get_uf(self):
		return self._uf		
	
	def _set_logradouro(self,logradouro):
		self._logradouro = logradouro			
	
	def _set_numero(self,numero):
		self._numero = numero
	
	def _set_bairro(self,bairro):
		self._bairro = bairro		
	
	def _set_cidade(self,cidade):
		self._cidade = cidade		
	
	def _set_cep(self,cep):
		self._cep = cep
	
	def _set_uf(self,uf):
		self._uf = uf
		
	logradouro = property(_get_logradouro,_set_logradouro)
	numero = property(_get_numero,_set_numero)	
	bairro = property(_get_bairro,_set_bairro)
	cidade = property(_get_cidade,_set_cidade)
	cep = property(_get_cep,_set_cep)		
	uf = property(_get_uf,_set_uf)	
	class Meta:
		abstract = True	
			

class TelefoneAbs(models.Model):
	TIPO_CHOICES = (
		('Fixo', 'Fixo'),
		('Celular', 'Celular'),
    )
	_telefone =  models.CharField(verbose_name='Telefone', max_length=15)
	tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
	
	class Meta:
		abstract = True	
		

class AcoesTelefone(TelefoneAbs):
	def __unicode__(self):
		return u'%s' % (self.telefone)

	class Meta:
		verbose_name_plural = "Telefones"
		abstract = True


class Telefone(AcoesTelefone):
	def _get_telefone(self):
		return self._telefone		
	
	def _set_telefone(self,telefone):
		self._telefone = telefone
					
	telefone = property(_get_telefone,_set_telefone)

	class Meta:
		abstract = True	
	

class TutorAbs(models.Model):
	_nome = models.CharField(verbose_name='Nome', max_length=50)
	_email = models.EmailField(verbose_name='E-Mail')
	_cpf = models.CharField(verbose_name='CPF', max_length=11)
	#endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE)
	#telefone = models.ForeignKey(Telefone, on_delete = models.CASCADE)
	
	class Meta:
		abstract = True
		

class AcoesTutor(TutorAbs):
	def __unicode__(self):
		return u'%s %s' % (self.nome, self.cpf)
				
	@classmethod
	def retornarID(tutor_id):
		lista = (Tutor.objects.get(self.id_ == tutor_id)) 
		return lista
		
	@classmethod	
	def verificarAtributos(item):
		lista_tutor = Tutor.objects.get(nome__icontains = item) 
		lista_tutor += Tutor.objects.filter(email__icontains = item) 	
		lista_tutor += Tutor.objects.filter(cpf__icontains = item) 		
		lista_retornavel = list(set(lista_tutor))		
		return lista_retornavel
		
	@classmethod	
	def buscarTutor(atributo_de_busca):	
		lista_tutor = AcoesTutor.retornarID(atributo_de_busca)
		if lista_retornavel != None: 
			return lista_retornavel
		lista_retornavel = AcoesTutor.verificarAtributos(atributo_de_busca) 	
		return lista_retornavel
			
	@classmethod		
	def listarAnimais(animal_id):
		return animais.objects.filter(self.id_ == animal_id) 			
			
	class Meta:
		verbose_name_plural = "Tutores"
		abstract = True	
		

class Tutor(AcoesTutor):
	def _get_nome(self):
		return self._nome		
		
	def _get_email(self):
		return self._email
	
	def _get_cpf(self):
		self._cpf
		
	def _set_nome(self,nome):
		self._nome = nome
	
	def _set_email(self,email):
		self._email = email	

	def _set_cpf(self,cpf):
		self._cpf = cpf	
	
	nome = property(_get_nome,_set_nome)
	email = property(_get_email,_set_email)	
	cpf = property(_get_cpf,_set_cpf)
	class Meta:
		abstract = True		


#mudar o nome para tutor_detalhe ou tutordetalhe ou tutordetalhes
class TutorEndTel(Tutor, Endereco, Telefone):
	def get_absolute_url(self):
		return reverse('tutor-detail', kwargs={'pk': self.pk})


class AnimalAbs(models.Model):
	GENERO_CHOICES = (
		('FE', 'Feminino'),
		('MA', 'Masculino'),
	 )
	_nome = models.CharField(verbose_name='Nome', max_length=50)
	_rg = models.PositiveSmallIntegerField(verbose_name='RG', unique=True)
	_especie = models.CharField(verbose_name='Espécie', max_length=50)
	_raca = models.CharField(verbose_name='Raça', max_length=50)
	sexo = models.CharField(verbose_name='Sexo', max_length=15, choices=GENERO_CHOICES)
	_nascimento = models.DateField(verbose_name='Data de Nascimento')
	_idade = models.PositiveSmallIntegerField(verbose_name='Idade')
	tutor = models.ForeignKey(TutorEndTel, on_delete = models.CASCADE)

	class Meta:
		verbose_name_plural = "Animais"
		abstract = True


class AcoesAnimal(AnimalAbs):
	def __unicode__(self):
		return u'%s %s' % (self.nome, self.rg)
		
	@classmethod		
	def verificarID(animal_id):
		return animais.objects.filter(self.id_ == animal_id)
		
	
	@classmethod	
	def verificarAtributos(item):
		lista_animal = Animal.objects.get(nome__icontains = item) 
		lista_animal += Animal.objects.filter(rg__icontains = item) 	
		lista_animal += Animal.objects.filter(especie__icontains = item)
		lista_animal += Animal.objects.filter(raca__icontains = item) 		
		lista_retornavel = list(set(lista_animal))		
		return lista_retornavel			
		
	class Meta:
		abstract = True
		

class Animal(AcoesAnimal):
	def _get_nome(self):
		return self._nome
		
	def _get_rg(self):
		return self._rg
		
	def _get_especie(self):
		return self._especie
		
	def _get_raca(self):
		return self._raca
		
	def _get_nascimento(self):
		return self._nascimento
		
	def _get_idade(self):
		return self._idade
																									
	def _set_nome(self,nome):
		self._nome = nome
	
	def _set_rg(self,rg):
		self._rg = rg
	
	def _set_especie(self,especie):
		self._especie = especie
	
	def _set_raca(self,raca):
		self._raca = raca
		
	def _set_nascimento(self,nascimento):
		self._nascimento = nascimento
		
	def _set_idade(self,idade):
		self._idade = idade		
	
	nome = property(_get_nome,_set_nome)		
	rg = property(_get_rg,_set_rg)
	especie = property(_get_especie,_set_especie)
	raca = property(_get_raca,_set_raca)
	nascimento = property(_get_nascimento,_set_nascimento)
	idade = property(_get_idade,_set_idade)

class Servico(models.Model):
	#campos
	#métodos
	class Meta:
		abstract = True

class ConsultaAbs (Servico):
	#campos
	#métodos
	class Meta:
		abstract = True

class Consulta (ConsultaAbs):
	#campos
	#métodos
	pass

class ExameAbs (Servico):
	#campos
	#métodos
	class Meta:
		abstract = True

class Exame (ExameAbs):
	#campos
	#métodos
	pass
