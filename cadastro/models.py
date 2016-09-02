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
	telefone_fixo_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="O formato do número de telefone deve ser: '+999999999'. São Permitidos até 15 dígitos.")
	_telefone =  models.CharField(validators=[telefone_fixo_regex],verbose_name='Telefone', max_length=15,blank=True)
	tipo = models.CharField( max_length=15, choices=TIPO_CHOICES)
	
	
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
	

class PessoaAbs(models.Model):
	_nome = models.CharField(verbose_name='Nome', max_length=50)
	_email = models.EmailField(verbose_name='E-Mail')
	_cpf = models.CharField(verbose_name='CPF', max_length=11)
	#endereco = models.ForeignKey(Endereco, on_delete = models.CASCADE)
	#telefone = models.ForeignKey(Telefone, on_delete = models.CASCADE)
	
	def __unicode__(self):
		return u'%s %s' % (self.nome, self.cpf)
	
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
	class Meta:
		abstract = True		


#mudar o nome para tutor_detalhe ou tutordetalhe ou tutordetalhes
class TutorEndTel(Tutor, Endereco, Telefone):
    def get_absolute_url(self):
        return reverse('tutorendtel_detail', kwargs={'pk': self.pk})


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

	def get_absolute_url(self):
		return reverse('animal_detalhes', kwargs={'pk': self.pk})


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

# referente a veterinario
class AcoesVeterinario(PessoaAbs):			
	@classmethod
	def retornarID(veterinario_id):
		lista = (Veterinario.objects.get(self.id_ == veterinario_id)) 
		return lista
		
	@classmethod	
	def buscarVeterinario(atributo_de_busca):	
		lista_veterinario = AcoesVeterinario.retornarID(atributo_de_busca)
		if lista_retornavel != None: 
			return lista_retornavel
		lista_retornavel = AcoesVeterinario.verificarAtributos(atributo_de_busca) 	
		return lista_retornavel
			
	class Meta:
		verbose_name_plural = "Veterinarios"
		abstract = True	
				

class Veterinario(AcoesVeterinario):
	_crmv = models.CharField(verbose_name='CRMV', max_length=10)
	def _get_crmv(self):
		return self._crmv
																									
	def _set_crmv(self,crmv):
		self._crmv = crmv 
	crmv = property(_get_crmv,_set_crmv)
	
# referente a tecnico	
class AcoesTecnico(PessoaAbs):
	@classmethod
	def retornarID(tecnico_id):
		lista = (Tecnico.objects.get(self.id_ == tecnico_id)) 
		return lista
		
	@classmethod	
	def buscarTecnico(atributo_de_busca):	
		lista_tecnico = AcoesTecnico.retornarID(atributo_de_busca)
		if lista_retornavel != None: 
			return lista_retornavel
		lista_retornavel = AcoesTecnico.verificarAtributos(atributo_de_busca) 	
		return lista_retornavel
			
	class Meta:
		verbose_name_plural = "Tecnicos"
		abstract = True	

class Tecnico(AcoesTecnico):
	_crf = models.CharField(verbose_name='CRF', max_length=10)
	def _get_crf(self):
		return self._crf
																									
	def _set_crf(self,crf):
		self._crf = crf 
	crf = property(_get_crf,_set_crf)
	
# classes para servico,consulta e exame	
class AtendimentoAbs(models.Model):
	_data = models.DateField(auto_now_add=True)
	_diagnostico = models.TextField(default = 'Pendente', blank = True, verbose_name='Diagnóstico', max_length=200)

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
		
	class Meta:
		abstract = True

class ConsultaAbs (AtendimentoAbs):
	_retorno = models.BooleanField(default = 'False')
	animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='a_ser_consultado')
	veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='realiza_consulta')	
	_data_realizacao = models.DateField(verbose_name='Data Agendada')
	
	class Meta:
		abstract = True
		verbose_name_plural = "Consultas"
		
class AcoesConsulta(ConsultaAbs):
		#métodos
		class Meta:
			abstract = True

class Consulta (AcoesConsulta):
	
	def _get_retorno(self):
		return self._retorno	
																																
	def _set_retorno(self,retorno):
		self._retorno = retorno
	
	retorno = property(_get_retorno,_set_retorno)	

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

class ExameAbs (AtendimentoAbs):
	tutor = models.ForeignKey(TutorEndTel,on_delete=models.CASCADE, related_name='dono_da_amostra')
	animal = models.ForeignKey(Animal,null = True, blank = True,on_delete=models.CASCADE, related_name='amostrado_para_exame')
	veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='realiza_diagnostico')
	tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='realiza_exame', blank = True, null = True)
	_resultado = models.TextField(default = 'Pendente', blank = True, verbose_name='Resultado', max_length=200)
	estadoexame = models.BooleanField(blank = True, verbose_name='Estado do Exame')
	laboratorio =  models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
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
	
