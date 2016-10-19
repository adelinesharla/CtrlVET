# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.views.generic.list import ListView,View
import abc
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
'Tradução e estados para PT-BR'
from django.utils.translation import ugettext_lazy as _

#from django.core.exceptions import ValidationError

'Estas classes implementam os campos de Tutor do Subsistema Secretaria e sua respectivas regras de negócio.'

STATE_CHOICES = (
	('', '----'),
	('AC', 'Acre'), 
	('AL', 'Alagoas'), 
	('AP', 'Amapá'), 
	('AM', 'Amazonas'), 
	('BA', 'Bahia'), 
	('CE', 'Ceará'), 
	('DF', 'Distrito Federal'), 
	('ES', 'Espírito Santo'), 
	('GO', 'Goiás'), 
	('MA', 'Maranhão'), 
	('MT', 'Mato Grosso'), 
	('MS', 'Mato Grosso do Sul'), 
	('MG', 'Minas Gerais'), 
	('PA', 'Pará'),
	('PB', 'Paraíba'), 
	('PR', 'Paraná'), 
	('PE', 'Pernambuco'), 
	('PI', 'Piauí'), 
	('RJ', 'Rio de Janeiro'), 
	('RN', 'Rio Grande do Norte'), 
	('RS', 'Rio Grande do Sul'), 
	('RO', 'Rondônia'), 
	('RR', 'Roraima'), 
	('SC', 'Santa Catarina'), 
	('SP', 'São Paulo'), 
	('SE', 'Sergipe'), 
	('TO', 'Tocantins')
	)

GENERO_CHOICES = (
		('', '----'),
		('FE', 'Feminino'),
		('MA', 'Masculino'),
	)

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
	
	def __str__(self):
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
	telefone_fixo_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O formato do número de telefone deve ser: '+999999999'. São Permitidos até 15 dígitos.")
	_telefone1 =  models.CharField(validators=[telefone_fixo_regex],verbose_name='Telefone de Contato 1', max_length=15,blank=True)
	_telefone2 =  models.CharField(validators=[telefone_fixo_regex],null = True,verbose_name='Telefone de Contato 2', max_length=15,blank=True)
	
	
	class Meta:
		abstract = True	
		

class AcoesTelefone(TelefoneAbs):
	def __unicode__(self):
		return u'%s' % (self.telefone)

	class Meta:
		verbose_name_plural = "Telefones"
		abstract = True


class Telefone(AcoesTelefone):
	def _get_telefone1(self):
		return self._telefone1		
	
	def _set_telefone1(self,telefone):
		self._telefone1 = telefone1

	def _get_telefone2(self):
		return self._telefone2		
	
	def _set_telefone2(self,telefone):
		self._telefone2 = telefone2
					
	telefone1 = property(_get_telefone1,_set_telefone1)
	telefone2 = property(_get_telefone2,_set_telefone2)

	class Meta:
		abstract = True	
	

class PessoaAbs(models.Model):
	_nome = models.CharField(verbose_name='Nome', max_length=50)
	_email = models.EmailField(verbose_name='E-Mail')
	_cpf = models.CharField(verbose_name='CPF', max_length=11)
	
	def __unicode__(self):
		return u'%s' % (self.nome)

	def __str__(self):
		return u'%s' % (self.nome)	
	
	def _get_nome(self):
		return self._nome		
		
	def _get_email(self):
		return self._email
	
	def _get_cpf(self):
		return self._cpf
		
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
		

class AcoesTutor(PessoaAbs):
	def __unicode__(self):
		return u'%s' % (self.nome)		
			
	class Meta:
		verbose_name_plural = "Tutores"
		abstract = True	
		

class Tutor(AcoesTutor):
	class Meta:
		abstract = True		


#mudar o nome para tutor_detalhe ou tutordetalhe ou tutordetalhes
class TutorEndTel(Tutor, Endereco, Telefone):
    def get_absolute_url(self):
        return reverse('tutorendtel_detail', kwargs={'pk': self.pk})

class AnimalAbs(models.Model):
	_nome = models.CharField(verbose_name='Nome', max_length=50)
	_rg = models.PositiveSmallIntegerField(verbose_name='RG', unique=True, blank = True)
	_especie = models.CharField(verbose_name='Espécie', max_length=50)
	_raca = models.CharField(verbose_name='Raça', max_length=50)
	sexo = models.CharField(verbose_name='Sexo', max_length=15, choices=GENERO_CHOICES)
	_nascimento = models.DateField(verbose_name='Data de Nascimento')
	_obito = models.DateField(verbose_name='Data de Óbito', null = True ,blank = True)
	_idade = models.PositiveSmallIntegerField(verbose_name='Idade')
	tutor = models.ForeignKey(TutorEndTel, on_delete = models.CASCADE, related_name='animais')

	class Meta:
		verbose_name_plural = "Animais"
		abstract = True

	def get_absolute_url(self):
		return reverse('animal_detalhes', kwargs={'pk': self.pk})


class AcoesAnimal(AnimalAbs):
	def __unicode__(self):
		return u'%s' % (self.nome)
	
	def __str__(self):
		return u'%s' % (self.nome)	

	class Meta:
		abstract = True
		

class Animal(AcoesAnimal):
	def get_absolute_url(self):
		return reverse('animal_detail', kwargs={'pk': self.pk})

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

	def _get_obito(self):
		return self._obito
		
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

	def _set_obito(self,obito):
		self._obito = obito
		
	def _set_idade(self,idade):
		self._idade = idade	
	
	nome = property(_get_nome,_set_nome)		
	rg = property(_get_rg,_set_rg)
	especie = property(_get_especie,_set_especie)
	raca = property(_get_raca,_set_raca)
	nascimento = property(_get_nascimento,_set_nascimento)
	idade = property(_get_idade,_set_idade)
	obito = property(_get_obito,_set_obito)

# referente a veterinario
class AcoesVeterinario(PessoaAbs):
		
	class Meta:
		verbose_name_plural = "Veterinarios"
		abstract = True	
				

class Veterinario(AcoesVeterinario):
	_crmv = models.CharField(verbose_name='CRMV', max_length=10)
	
	def __unicode__(self):
		return u'%s' % (self.nome)
	
	def __str__(self):
		return u'%s' % (self.nome)	

	def _get_crmv(self):
		return self._crmv
																									
	def _set_crmv(self,crmv):
		self._crmv = crmv 
	crmv = property(_get_crmv,_set_crmv)
	
# referente a tecnico	
class AcoesTecnico(PessoaAbs):		
	class Meta:
		verbose_name_plural = "Tecnicos"
		abstract = True	

class Tecnico(AcoesTecnico):
	_crf = models.CharField(verbose_name='CRF', max_length=10)

	def __unicode__(self):
		return u'%s' % (self.nome)
	
	def __str__(self):
		return u'%s' % (self.nome)	

	def _get_crf(self):
		return self._crf
																									
	def _set_crf(self,crf):
		self._crf = crf 
	crf = property(_get_crf,_set_crf)
	
# classes para servico,consulta e exame	
class AtendimentoAbs(models.Model):
	_data = models.DateField(auto_now_add=True)
	_diagnostico = models.TextField(default = 'Pendente', blank = True, verbose_name='Diagnóstico', max_length=200)
	cliente = models.ForeignKey(TutorEndTel,on_delete=models.CASCADE, related_name='cliente_a_ser_atendido', null = True ,blank = True)
	
	def _get_data(self):
		return self._data
	
	def _get_diagnostico(self):
		return self._diagnostico	
																																
	def _set_diagnostico(self,diagnostico):
		self._diagnostico = diagnostico
	
	def _set_data(self,data):
		self._data = data
		
	diagnostico = property(_get_diagnostico,_set_diagnostico)		
	data = property(_get_data,_set_data)	

class ConsultaAbs (AtendimentoAbs):
	_retorno = models.BooleanField()
	animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='a_ser_consultado')
	veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='realiza_consulta')	
	_data_realizacao = models.DateField(verbose_name='Data Agendada')
	
	class Meta:
		abstract = True
		verbose_name_plural = "Consultas"
		
class AcoesConsulta(ConsultaAbs):
		class Meta:
			abstract = True

class Consulta (AcoesConsulta):
	
	def _get_retorno(self):
		return self._retorno	
																																
	def _set_retorno(self,retorno):
		self._retorno = retorno
	
	def _get_data_realizacao(self):
		return self._data_realizacao	
																																
	def _set_data_realizacao(self,data_realizacao):
		self._data_realizacao = data_realizacao
	
	retorno = property(_get_retorno,_set_retorno)	
	data_realizacao = property(_get_data_realizacao,_set_data_realizacao)

#classes referentes a laboratório

class Laboratorio (models.Model):
	_nome = models.CharField(verbose_name='Nome', max_length=50)
	_local = models.CharField(verbose_name='local', max_length=50)
	
	def get_absolute_url(self):
			return reverse('laboratorio_detail', kwargs={'pk': self.pk})

	def _get_nome(self):
		return self._nome
	def _get_local(self):
		return self._local	
																												
	def _set_nome(self,nome):
		self._nome = nome
	def _set_local(self,local):
		self.local = local
	nome = property(_get_nome,_set_nome)	
	local = property(_get_local,_set_local)

	def __unicode__(self):
		return u'%s' % (self.nome)
	
	def __str__(self):
		return u'%s' % (self.nome)	

class ExameAbs (AtendimentoAbs):
	animal = models.ForeignKey(Animal,null = True, blank = True,on_delete=models.CASCADE, related_name='mostrado_para_exame')
	veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='realiza_diagnostico')
	tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='realiza_exame', blank = True, null = True)
	_resultado = models.TextField(default = 'Pendente', blank = True, verbose_name='Resultado', max_length=200)
	observacoes = models.CharField(blank=True, null=True, verbose_name='Observações', max_length=200)
	numero_amostra = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Número de amostra')
	estadoexame = models.NullBooleanField(null = True, blank = True, verbose_name='Estado do Exame')
	laboratorio =  models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='exames', blank=True, null=True)
	class Meta:
		abstract = True
		verbose_name_plural = "Exames"
		

class AcoesExame(ExameAbs):
	@classmethod
	def estadoExame(veterinario,tecnico,estadoexame):
		if tecnico != None:
			if veterinario != None:
				estadoExame = True
				return estadoExame
			else:
				estadoExame = False
				return estadoExame
		else:
			estadoExame = False
			return estadoExame
	class Meta:
		abstract = True
	
class Exame (AcoesExame):
	def get_absolute_url(self):
        	return reverse('exame_detail', kwargs={'pk': self.pk})

	def _get_resultado(self):
		return self._resultado	
																																
	def _set_resultado(self,resultado):
		self._resultado = resultado
	
	resultado = property(_get_resultado,_set_resultado)	
	
