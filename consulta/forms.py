#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django import forms

"""importação necessária para criar formulários com mais de uma model"""
#from django.forms.models import inlineformset_factory
from material import *
from .models import *
from localflavor.br.forms import BRCPFField
from datetime import datetime
from cadastro.models import GENERO_CHOICES, STATE_CHOICES

ALIMENTACAO_CHOICES = (
		('RA', 'Racao'),
		('CC', 'Comida caseira'),
		('RC', 'Racao + Comida'),
		('PE', 'Petiscos'),
	)
	
VERMIFUGACAO_CHOICES = (
		('NAO', 'Nao'),
		('SIM', 'Sim'),
		('QQ', 'Qual/quando'),
	)	
	
AMBIENTE_CHOICES = (
		('RU', 'Rural'),
		('UR', 'Urbano'),
		('AR', 'Acesso a rua'),
	)	
ECTOPARASITAS_CHOICES = (
		('PU', 'Pulgas'),
		('CA', 'Carrapatos'),
	)	
	
HIDRATACAO_CHOICES = (
		('NO', 'Normal'),
		('LD', 'Leve desidratacao'),
		('MD', 'Moderada desidratacao'),
		('SD', 'Severa desidratacao'),
	)		
	
PROGNOSTICO_CHOICES = (
		('BOM', 'Bom'),
		('RE', 'Reservado'),
		('RU', 'Ruim'),		
	)	
	
EXAMESCOMPLEMENTARES_CHOICES = (
		('HC', 'Hemograma completo'),
		('PL', 'Plaquetas'),
		('HE', 'Hematócrito'),
		('RE', 'Reticulócitos'),		
	)		
	
PERFILRENAL_CHOICES = (
		('UR', 'Uréia'),
		('CR', 'Creatina'),
		('URI', 'Urinálise'),		
	)				
	
PERFILHEPATICO_CHOICES = (
		('ALT', 'ALT'),
		('FA', 'FA'),
		('GGT', 'GGT'),
		('PT', 'PT'),
		('ALB', 'ALB'),
		('GLOB', 'Glob'),
		('BT', 'Bilirrubina total'),
		('BD', 'Bilirrubina direta'),				
		('BI', 'Bilirrubina indireta'),				
	)		
	
BIOQUIMICO_CHOICES = (
		('GLI', 'Glicemia'),
		('TRI', 'Triglicerídeos'),
		('COL', 'Colesterol'),
		('NA', 'Na'),
		('K', 'K'),
		('CA', 'Ca'),
		('P', 'p'),
	)			
	
IMAGEM_CHOICES	= (
		('RX', 'Raio-X'),
		('US', 'US'),
		('ECO', 'ECO'),
		('MI', 'Miolografia'),
	)		
	
OUTROS_CHOICES	= (
		('ECG', 'ECG'),
		('PA', 'PA'),
		('CI', 'Citologia'),
		('BI', 'Biópsia'),
		('SO', 'Sorologia'),
		('PMO', 'PMO'),
	)	

class CabecalhoForm(forms.Form):
	nome = forms.CharField(label='Nome',max_length=100)
	rg = forms.IntegerField(label='RG')
	data = forms.DateField(label='Data')
	especie = forms.CharField(label='Especie',max_length=50)
	raca = forms.CharField(label='Raça', max_length=50)
	idade = forms.IntegerField(label='Idade')
	sexo = forms.ChoiceField(label = 'Sexo', widget=forms.Select, choices=GENERO_CHOICES)
	pelagem = forms.CharField(label='Pelagem', max_length=50)
	peso = forms.DecimalField(label='Peso(Kg)',max_digits=4, decimal_places=3)
	tutor = forms.CharField(label='Proprietário', max_length=50)
	bairro = forms.CharField(label='Endereço', max_length=20)
	email = forms.EmailField(label='E-Mail')
	telefone = forms.CharField(label='Telefone',max_length=15)
	
class RodapeForm(forms.Form):
	docente = forms.CharField(label='Docente', max_length=100)
	medicoVeterinario = forms.CharField(label='Veterinário', max_length=100)
	aluno = forms.CharField(label='Aluno', max_length=100)
	estagiario = forms.CharField(label='Estagiário', max_length=100)

class FichaAtendimentoPequenos(forms.Form):
	
	queixaEhistoria = forms.CharField(label='Queixa principal e história médica recente', max_length=100)
	#medicacoes = forms.CharField(label='Medicações', max_length=100)
	doencasAnteriores = forms.CharField(label='Doenças anteriores', max_length=100)
	aparenciaGeral = forms.CharField(label='Aparência geral/estado nutricional', max_length=100)
	sistemaDigestorio = forms.CharField(label='Sistema Digestório',widget=forms.Textarea, max_length=100)
	sistemaUrogenital = forms.CharField(label='Sistema urogenital', max_length=100)
	sitemaCardiorespiratorio = forms.CharField(label='Sistema Cardiorespiratório', max_length=100)
	sistemaNeurologico = forms.CharField(label='Sistema neurológico', max_length=100)
	sistemaLocomotor = forms.CharField(label='Sistema locomotor', max_length=100)
	peleOuvidos = forms.CharField(label='Pele e ouvidos', max_length=100)
	olhos = forms.CharField(label='Olhos', max_length=100)
	
	
	alimentacao = forms.ChoiceField(label = 'Alimentação', widget=forms.Select, choices = ALIMENTACAO_CHOICES)
	quantidade = forms.IntegerField(label='Quantidade')
	tipoDeAlimento = forms.CharField(label='Tipo de ração/alimento', max_length=50)
	frequencia = forms.CharField(label='Frequência', max_length=40)
	vacinacao = forms.CharField(label='Vacinação', max_length=100)
	vermifugacao = forms.ChoiceField(label = 'Vermifugação', widget=forms.Select, choices = VERMIFUGACAO_CHOICES)
	ambiente = forms.ChoiceField(label = 'Ambiente', widget=forms.Select, choices = AMBIENTE_CHOICES)
	contactantes = forms.CharField(label='Contactantes', max_length=100)
	ectoparasitas = forms.ChoiceField(label = 'Ectoparasitas', widget=forms.Select, choices = ECTOPARASITAS_CHOICES)
	tipoDeControle = forms.CharField(label='Tipo de controle', max_length=100)
	#contatoComRoedores = forms.Booleanfield(label = 'Contato com roedores',Field.default = false)
	#contatoProdutosToxicos = forms.Booleanfield(label = 'Contato com produtos tóxicos',Field.default = false)
	qual = forms.CharField(label='Qual', max_length=100)
	banho = forms.CharField(label='Banho', max_length=50)
	
	
	estadoDeHidratacao = forms.ChoiceField(label = 'Estado de hidratação', widget=forms.Select, choices = HIDRATACAO_CHOICES)
	mandibulares = forms.CharField(label='Mandibulares', max_length=50)
	preEscapulares = forms.CharField(label='Pré-escapulares', max_length=50)
	popliteos = forms.CharField(label='Poplíteos', max_length=50)
	outros = forms.CharField(label='Outros', max_length=50)

	
	mucosas = forms.CharField(label='Mucosas', max_length=100)
	tpc = forms.CharField(label='TPC')
	fr = forms.IntegerField(label='FR')
	fc = forms.IntegerField(label='FC')
	pulso = forms.IntegerField(label='Pulso')
	temperatura = forms.DecimalField(label='Banho',max_digits=3, decimal_places=2)


	palpacaoAbdominal = forms.CharField(label='Palpação abdominal', max_length=100)
	auscultacaoCardiopulmonar = forms.CharField(label='Auscultação cardiopulmonar', max_length=100)
	outrosAchados = forms.CharField(label='Outros achados', max_length=100)

	
	observacoes = forms.CharField(label='Observações', max_length=100)
	#prognostico = forms.ChoiceField(label = 'Prognostico', widget=forms.Select, choices = PROGNOSTICO_CHOICES)
	diagnosticoDefinitivo =  forms.CharField(label='Diagnóstico definitivo', max_length=100)
	tratamentoAmbulatorial =  forms.CharField(label='Tratamento ambulatorial', max_length=100)
	fluidoterapia =  forms.CharField(label='Fluidoterapia', max_length=100)
	prescricao =  forms.CharField(label='Prescrição', max_length=100)
	retorno = forms.DateField(label='Retorno')
	alta = forms.DateField(label='Alta')
	encaminhamento = forms.CharField(label='Encaminhamento', max_len)

	
	
class FichaRetornoPequenos(forms.Form):
	
	anamnese = forms.CharField(label='Anamnese',max_length=500)
	
	estadoDeHidratacao = forms.ChoiceField(label = 'Estado de hidratação', widget=forms.Select, choices = HIDRATACAO_CHOICES)
	mandibulares = forms.CharField(label='Mandibulares', max_length=50)
	preEscapulares = forms.CharField(label='Pré-escapulares', max_length=50)
	popliteos = forms.CharField(label='Popliteos', max_length=50)
	outros = forms.CharField(label='Outros', max_length=50)
	
	mucosas = forms.CharField(label='Mucosas', max_length=100)
	tpc = forms.CharField(label='TPC')
	fr = forms.IntegerField(label='FR')
	fc = forms.IntegerField(label='FC')
	pulso = forms.IntegerField(label='Pulso')
	temperatura = forms.DecimalField(label='Banho',max_digits=3, decimal_places=2)
	
	palpacaoAbdominal = forms.CharField(label='Palpacao abdominal', max_length=100)
	auscultacaoCardiopulmonar = forms.CharField(label='Auscultação cardiopulmonar', max_length=100)
	outrosAchados = forms.CharField(label='Outros achados', max_length=100)
	
	examesComplementares = forms.ChoiceField(label = 'Exames Complementares', widget=forms.Select, choices=EXAMESCOMPLEMENTARES_CHOICES)
	perfilRenal = forms.ChoiceField(label = 'Perfil Renal', widget=forms.Select, choices=PERFILRENAL_CHOICES)
	perfilHepatico = forms.ChoiceField(label = 'Perfil hepático', widget=forms.Select, choices=PERFILHEPATICO_CHOICES)
	bioquimico = forms.ChoiceField(label = 'Bioquímico', widget=forms.Select, choices=BIOQUIMICO_CHOICES)
	imagem = forms.ChoiceField(label = 'Imagem', widget=forms.Select, choices=IMAGEM_CHOICES)
	outros = forms.ChoiceField(label = 'Outros', widget=forms.Select, choices=OUTROS_CHOICES)
	
	diagnostico_definitivo = forms.CharField(label='Diagnóstico definitivo', max_length=100)
	tratamentoAmbulatorial = forms.CharField(label='Tratamento ambulatorial', max_length=200)
	fluidoterapia =  forms.CharField(label='Fluidoterapia', max_length=100)
	prescricao =  forms.CharField(label='Prescrição', max_length=100)
	retorno = forms.DateField(label='Retorno')
	alta = forms.DateField(label='Alta')
	
'''Essa ficha também deve ser utiilizada para o retorno'''
class FichaAtendimentoGrandes(forms.Form):
	anamnese = forms.CharField(label='Anamnese',max_length=3000)
	
	'''alimentacao'''
	
	outros = forms.CharField(label='Outros achados',max_length=500)
	suspeita = forms.CharField(label='Suspeita Clínica',max_length=300)
	prognostico = forms.CharField(label='Prognóstico',max_length=300)
	diagnostico = forms.CharField(label='Diagnóstico',max_length=500)
	
	tratamento = forms.CharField(label='Protocolo de Tratamento',max_length=3000)
	observacoes = forms.CharField(label='Observações',max_length=500)	
	



