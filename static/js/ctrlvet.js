$( document ).ready(function() {
	Materialize.updateTextFields();
	$('.button-collapse').sideNav();
	$('.collapsible').collapsible({
		accordion : true
	});
	$(".dropdown-button").dropdown();
	$('select').material_select();
	$('input:not([placeholder])').attr('placeholder', '');
});