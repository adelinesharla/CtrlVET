$( document ).ready(function() {
	$(".dropdown-button").dropdown();
	$(".button-collapse").sideNav();
	$('.collapsible').collapsible({
		accordion : true
	});

	Materialize.updateTextFields();

	$('select').material_select();


	$('.datepicker').pickadate({
		format: 'mm/dd/yyyy',
		selectMonths: true, 
		selectYears: 15,
		firstDay: 0,

		monthsFull: [ 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro' ],
		monthsShort: [ 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez' ],
		weekdaysFull: [ 'domingo', 'segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado' ],
		weekdaysShort: [ 'dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab' ],
		weekdaysMin: ['d', 's', 't', 'q', 'q', 's', 's'],
		today: 'hoje',
		clear: 'limpar',
		close: 'fechar',
		format: 'mm/dd/yyyy',
		formatSubmit: 'yyyy/mm/dd'

	});

	$('input:not([placeholder])').attr('placeholder', '');

	$('.modal-trigger').leanModal({
		dismissible: true, 
		opacity: .5, 
		in_duration: 300,
		out_duration: 200, 
	}
	);
});