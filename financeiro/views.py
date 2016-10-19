# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.conf.urls import url

"""Classes de views genericas utilizadas"""
from django.views.generic import View, CreateView, TemplateView, DetailView, UpdateView, DeleteView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin
from _functools import reduce

'HttpResponse para uma pagina template indicando que a operação foi realizada (verificar se tal página existe)'
from django.http import HttpResponseRedirect

'Importando Formularios necessários para views de tutor e animal'
from .forms import *
'Importando Models necessárias para views de tutor e animal'
from cadastro.models import Consulta,Exame

from django.forms.models import model_to_dict #iterar em object no template

'Importando atributos da model a serem utilizados nas buscas'
import operator
from django.db.models import Q

from django.forms.formsets import formset_factory

'Importacao para gerar pdf'
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from django.http import HttpResponse
from datetime import datetime

from django.db.models import Sum


class SuccessView(TemplateView):
	template_name='financeiro/success.html'	


class ProdutoFormView(FormView):
	pass

class ServicoFormView(FormView):
	pass


class PrestacaoContasView(TemplateView):
	template_name='financeiro/pagamento_pretacaocontas.html'	


"""class DebitoFormView(FormView):
	template_name = 'financeiro/debito_form.html'
	form_class = DebitoModelForm
	success_url = '/success/'
	debito_formset = formset_factory(NotaModelForm)

	def form_valid(self, form):
		form.save()
		debito_formset.save()
		return HttpResponseRedirect('/success/')

	def get_context_data(self, *args, **kwargs):
		context = super(DebitoFormView, self).get_context_data(*args, **kwargs)
		context['debito_formset'] = formset_factory(NotaModelForm)
		return context 
"""

class NotaFormView(FormView):
	template_name = 'financeiro/nota_form.html'
	form_class = ItemNotaModelForm
	success_url = '/success/'

	def form_valid(self, faorm):
		
		form.save()
		return HttpResponseRedirect('/success/')
		
		
class DebitosList(ListView):
	model = Nota
	paginate_by = 10

class DebitosListView(DebitosList):
	template_name = 'financeiro/debitos_list.html'
	def get_queryset(self):
		return Nota.objects.filter(status=0)

class RecebidosListView(DebitosList):
	template_name = 'financeiro/recebidos_list.html'
	def get_queryset(self):
		return Nota.objects.filter(status=1)		
		

class PagamentoResumo(TemplateView):
	template_name='financeiro/pagamento_resumo.html'
	
	def get_context_data(self, *args, **kwargs):
		context = super(PagamentoResumo, self).get_context_data(*args, **kwargs)
		context['recebidos_list'] = (Nota.objects.filter(status=1).annotate(total=Sum('itemNota___valor'))).order_by('status')[:5]
		context['debitos_list'] = (Nota.objects.filter(status=0).annotate(total=Sum('itemNota___valor'))).order_by('status')[:5]
		return context 



'''class ListPagamento(ListView):
	model = GENERIC_PAGAMENTO
	paginate_by = 10

class EfetuarPagamento(FormView):
	template_name = 'financeiro/GENERICO_PAGAMENTO_FORM.HTML'
	form_class = GENERIC_PAG_FORM
	success_url = '/success/'
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')
  
class AlterarPagamento(UpdateView):
	form_class = GENERIC_PAG_FORM
	model = GENERIC_PAGAMENTO
	fields = '_all_'
	template_name_suffix = '_update_form'
	success_url = '/success/'

class CancelarPagamento(self):
	model = GENERIC_PAGAMENTO
	success_url = reverse_lazy('tutor_resumo')
	success_url = '/successs/'
  
class DetalhesPagamento(DetailView):
	pk_url_kwarg = "generic_id"
	model = GENERIC_PAGAMENTO

	def get_context_data(self, **kwargs):
		context = super(DetalhesPagamento, self).get_context_data(**kwargs)
		return context
	  
class PagamentoBuscaListView(self):
  def get_queryset(self):
	result = super(PagamentoBuscaListView, self).get_queryset()
	query = self.request.GET.get('q')
	if query:
		query_list = query.split()
		result = result.filter(
		reduce(operator.and_,
		(Q(_nome__icontains=q) for q in query_list)) |
		reduce(operator.and_,
		(Q(_email__icontains=q) for q in query_list)) |
		reduce(operator.and_,
		(Q(_cpf__icontains=q) for q in query_list))
		)

		return result'''

class AnoList(ListView):
	model=Ano

class AnoDetalhesView(DetailView):
	pk_url_kwarg = "ano_id"
	model = Ano

	def get_context_data(self, **kwargs):
		context = super (AnoDetalhesView, self).get_context_data(**kwargs)

		debitos = self.object.notas.all()
		soma = []
		for debito in debitos:
			soma.append(debito.itemNota.valor)
		context ['valor_total'] = sum(soma)
		soma = []
				
		for debito in debitos:
			if (debito.nota.setor == '1'):
				soma.append(debito.itemNota.valor)
		context ['pequenos'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '2'):
				soma.append(debito.itemNota.valor)
		context ['grandes'] = sum(soma)	
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '3'):
				soma.append(debito.itemNota.valor)
		context ['cirurgica'] = sum(soma)	
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '4'):
				soma.append(debito.itemNota.valor)
		context ['clinica'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '5'):
				soma.append(debito.itemNota.valor)
		context ['imagem'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '6'):
				soma.append(debito.itemNota.valor)
		context ['parasitologia'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '7'):
				soma.append(debito.itemNota.valor)
		context ['microbiologia'] = sum(soma)
		soma = []

		for debito in debitos:
			if (debito.nota.setor == '8'):
				soma.append(debito.itemNota.valor)
		context ['animal'] = sum(soma)
		soma = []

		return context

class GeraPdfPrestacaoContas(DetailView):
	model=Ano

	def get(self, request,ano):
		pk_url_kwarg = "ano_id"
		model = Ano
	
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename= "Prestacao de contas.pdf"'
		pdf = canvas.Canvas(response)
		pdf.setLineWidth(.2)
		pdf.setFont('Helvetica', 12, leading=None)
		
		pdf.setFont('Helvetica', 16, leading=None)
		pdf.drawString(30,800,'Prestação de Contas''(Jan - Dez) '+str(ano))
		pdf.setFont('Helvetica', 14, leading=None)
		
		coluna = 30
		colunaP = 440
		linha = 750
		espacamento = 35
		
		pdf.drawString(coluna,linha,'Setor')
		pdf.drawString(400,linha,'Valor Arrecadado (R$)')
		pdf.line(coluna,739,540,739)
		pdf.setFont('Helvetica', 12, leading=None)
		notas = Nota.objects.all()
		linha = linha-espacamento
		soma = []
		
		for nota in notas:
			if (nota.setor == '1' and nota.ano.ano == ano):
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Clínica de Pequenos')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		
		for nota in notas:
			if (nota.setor == '2'and nota.ano.ano == ano):
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Clínica de Grandes')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		
		for nota in notas:
			if (nota.setor == '3'and nota.ano.ano == ano):
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Clínica Cirúrgica')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))	
			
		soma = []
		linha = linha-espacamento
		
		for nota in notas:
			if (nota.setor == '4'and nota.ano.ano == ano):
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Patologia Clínica')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))	
		
		soma = []
		linha = linha-espacamento
		
		for nota in notas:
			if (nota.setor == '5'and nota.ano.ano == ano):
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Diagnóstico por Imagem')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))	
		
		soma = []
		linha = linha-espacamento
		
		for nota in notas:
			if (nota.setor == '6'and nota.ano.ano == ano):
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Parasitologia')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
			
		soma = []
		linha = linha-espacamento
		
		for nota in notas:
			if (nota.setor == '7'and nota.ano.ano == ano):
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Microbiologia')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		
		for nota in notas:
			if (nota.setor == '8'and nota.ano.ano == ano):
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Patologia Animal')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		
		soma = []
		linha = linha-espacamento
		
		pdf.line(30,459,540,459)
		
		for nota in notas:
			if nota.ano.ano == ano:
				itens= nota.itemNota.all()
				for item in itens:
					soma.append(item.valor)
		pdf.drawString(coluna,linha,'Valor Total Arrecadado (R$)')
		pdf.drawString(colunaP,linha,"%d,00" % sum(soma))
		dataAtual = datetime.now()
		pdf.drawString(30,30,'Emissão do Relatório: '+str(dataAtual.day)+'/'+str(dataAtual.month)+'/'+str(dataAtual.year))	
		pdf.save()
		return response
		
		
class GeraPdfNotaDePagamento(DetailView):
	model=Nota

	def get(self, request,nota_id):
		pk_url_kwarg = "nota_id"
		model = Nota

		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename= "Nota de Pagamento.pdf"'
		pdf = canvas.Canvas(response)
		pdf.setLineWidth(.2)
		dataAtual = datetime.now()
		pdf.line(20,820,574,820)
		pdf.line(20,820,20,20)
		pdf.line(574,820,574,20)
		pdf.line(20,20,574,20)
		
		logo ='static/media/logo/ufes.png'
		pdf.drawImage(logo,30,695, width = None, height = None)
		
		pdf.setFont('Helvetica', 18, leading=None)
		pdf.drawString(185,790,'Universidade Federal do Espírito Santo')
		pdf.drawString(185,670,'Controle de Pagamento')
		pdf.drawString(265,740,'Hospital Veterinário')
		pdf.setFont('Helvetica', 16, leading=None)
		pdf.drawString(240,765,'Centro de Ciências Agrárias')
		pdf.setFont('Helvetica', 11, leading=None)
		pdf.drawString(370,715,'BR 482, km 63 - Tel. (28) 98803-4503')
		pdf.drawString(302,695,'Área Experimental do CCA-UFES, Alegre-ES-Brasil')
		pdf.line(20,690,574,690)
		
		pdf.setFont('Helvetica', 12, leading=None)
		
		hovet = 'static/media/logo/hovet2.jpg'
		pdf.drawImage(hovet,430,545, width = None, height = None)
		
		notas = Nota.objects.filter(pk = nota_id)
		
		pdf.drawString(30,620,'Proprietário: ')
		pdf.drawString(30,600,'Telefone: ')
		cont = 0
		terminou = False
		
		for nota in notas:
			pdf.drawString(30,640,'Setor: '+nota.get_setor_display())	
			if hasattr(nota.atendimento.cliente ,'pk') == True:
				pdf.drawString(100,620,nota.atendimento.cliente.nome)	
				pdf.drawString(85,600,nota.atendimento.cliente.telefone1)
				
			if hasattr(nota.atendimento,'data_realizacao') :
				pdf.drawString(30,580,'Deu Certo: ')
				
			if hasattr(nota.atendimento,'resultado') :
				pdf.drawString(30,580,'Deu Certo: ')
							
				
			""" is instance deve ser utilizado no if e no elif abaixo"""	
								
			if isinstance(nota.atendimento,Consulta):	
				consulta = Consulta(nota.atendimento)
				pdf.drawString(30,580,'Animal: '+consulta.animal.nome)
			
		
			elif isinstance(nota.atendimento,Exame):	
				exame = Exame(nota.atendimento)
				pdf.drawString(30,580,'Amostra: '+exame.amostra)		
					
		x1= 20
		y1 = 540
		x2 = 574	
		espacamento = 20
		pdf.line(x1,y1,x2,y1)
		pdf.drawString(200,525,'PROCEDIMENTOS ')
		pdf.drawString(500,525,'VALOR ')
		y1 = y1 - espacamento
		pdf.line(x1,y1,x2,y1)	
		pdf.line(460,y1+espacamento,460,y1)	
		soma = []
		numItens = 0
		
		for nota in notas:
			for item in nota.itemNota.all():
				numItens = numItens+1
		
		for nota in notas:
			for item in nota.itemNota.all():
				y1 = y1 - 15	
				pdf.drawString(30,y1,item.nome)
				pdf.drawString(500,y1,"%d,00" % item.valor)
				soma.append(item.valor)
				y1 = y1 - 5
				pdf.line(x1,y1,x2,y1)		
				pdf.line(460,y1+espacamento,460,y1) #linha vertical
				cont = cont + 1
				if cont >22:
					terminou = True
					cont = 0
					if terminou == True:	
						if numItens % 23 != 0:
							pdf.showPage()
							y1 = 805
							pdf.drawString(200,y1,'PROCEDIMENTOS ')
							pdf.drawString(500,y1,'VALOR ')
							y1 = y1-5
							pdf.line(x1,y1,x2,y1)
							pdf.line(460,y1+espacamento,460,y1)	
						
							pdf.line(20,820,574,820)
							pdf.line(20,820,20,20)
							pdf.line(574,820,574,20)
							pdf.line(20,20,574,20)
						terminou = False				
				
		y1 = y1 - espacamento				
		pdf.line(x1,y1,x2,y1)
		pdf.line(460,y1+espacamento,460,y1)
		pdf.drawString(230,y1+5,'TOTAL')
		pdf.drawString(500,y1+5,"%d,00" % sum(soma))
		pdf.setFont('Helvetica', 11, leading=None)
		pdf.drawString(30,30,'Emissão do Relatório: '+str(dataAtual.day)+'/'+str(dataAtual.month)+'/'+str(dataAtual.year))	
		pdf.save()
		return response
	
class EstoqueResumo(TemplateView):
	template_name='financeiro/estoque_resumo.html'

class ItemNotaFormView(FormView):
	template_name = 'financeiro/nota_form.html'
	form_class = ItemNotaModelForm
	success_url = '/success/'

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/success/')

class EfetuarPagamento(View):
	model = Nota
	success_url = '/pagamentos/resumo'

	def get(self, args, **kwargs):
		nota =  Nota.objects.get(pk=self.kwargs['pk'])
		nota.status = True
		nota.save()
		return HttpResponseRedirect(self.success_url)
		
