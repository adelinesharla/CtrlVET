from django.shortcuts import render



class ListPagamento(ListView):
    model = GENERIC_PAGAMENTO
    paginate_by = 10

class EfetuarPagamento(FormView):
    template_name = 'financeiro/GENERICO_PAGAMENTO_FORM.HTML'
    form_class = GENERIC_PAG_FORM
    suess_url = '/success/'
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

        return result
