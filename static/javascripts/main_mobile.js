

function get_resume(){
	$.get('/resume', function(data){

	});
}

function send_email(){
	$.post('/mail', {
		'email-address': $("#email-address").val(),
		'email-content': $("#email-content").val()
	}, function(data){
		console.log(data);
		if(data == "OK") console.log("yes");
		$("#thank-you").text("Thank you for your message!");
	});
}

$(document).ready(function(){


})
