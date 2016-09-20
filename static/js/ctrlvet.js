$( document ).ready(function() {
	Materialize.updateTextFields();
	$('.button-collapse').sideNav();
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
});

function AlertSucesso(){
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
