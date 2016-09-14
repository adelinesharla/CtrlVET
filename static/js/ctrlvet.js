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