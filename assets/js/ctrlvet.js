$( document ).ready(function() {
	Materialize.updateTextFields();
	$('.button-collapse').sideNav({
      menuWidth: 240, // Default is 240

  }
  );
	$('.collapsible').collapsible({
		accordion : true
	});
	$(".dropdown-button").dropdown();
	$('select').material_select();
	$('input:not([placeholder])').attr('placeholder', '');

	$('.modal-trigger').leanModal({
		dismissible: true, 
		opacity: .5, 
		in_duration: 300,
		out_duration: 200, 
	});

	jQuery.fn.datetimepicker.defaults['lang'] = 'pt';

	jQuery('#id__nascimento').datetimepicker({
		maxDate: 0,
	});

	jQuery('#id__data_realizacao').datetimepicker({
		minDate: 0,
	});

	
	$('#id__cep').mask('00000-000', {placeholder:"00000-000"});
	$('#id__cpf').mask('000.000.000-00', {placeholder:"000.000.000-00"}, {reverse: true});
	$('#id__telefone1').mask('(99)9999-99999', {placeholder:"(99)9999-99999"});
	$('#id__telefone2').mask('(99)99999-9999', {placeholder:"(99)99999-9999"});
	$('#id__telefone2').mask('(99)99999-9999', {placeholder:"(99)99999-9999"});
	$('#id__valor').mask('000.000.000.000.000,00', {reverse: true});
	$('#id__cep').mask('00.000-000',  {placeholder:"00.000-000"}, {reverse: true});

});

function AlertSucesso(){

	$('#id__telefone1').unmask();
	$('#id__telefone2').unmask();
	$('#id__cep').unmask();
	$('#id__cpf').unmask();
	$('#id__valor').unmask();
	
	$('#id__telefone1').cleanVal();
	$('#id__telefone2').cleanVal();
	$('#id__cep').cleanVal();
	$('#id__cpf').cleanVal();
	$('#id__valor').cleanVal();

	flag = 1;
	for (i = 0; i < document.forms[0].getElementsByTagName('input').length; i++ ){
		if( document.forms[0][i].value == null || document.forms[0][i].value == "" ){
			flag = 0;
		}
	}
	if (flag == 0) {
		alert("Erro no formulário!");
		return false;
	}else{
		alert("Sucesso! clique 'ok' para voltar ao resumo!");
		return true;
	}
};

