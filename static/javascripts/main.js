

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


	//color alternating function
	var $knob_colors = ['red', 'green', 'blue'];
	var $alternate_progress = 0;

	function choose_progress_color(){
		if($alternate_progress == 3)$alternate_progress = 0;
		return $knob_colors[$alternate_progress++];
	}

	//skill bars.  Different color for each section
	$('.skill').each(function(){
		var $color = choose_progress_color();

		$(this).find('.skill-bar').jprogress({
			background: $color
		});
	});


	//color alternating function
	var $knob_colors = ['red', 'green', 'blue'];
	var $alternate_knob = 0;

	function choose_knob_color(){
		if($alternate_knob == 3) $alternate_knob = 0;
		return $knob_colors[$alternate_knob++];
	}

	//languages.  Different color for each language
	$('.circle').each(function(){
		$(this).knob({
			'angleOffset': 0,
			'readOnly': true,
			'fgColor': choose_knob_color(),
			'format' : function (value) {
				return value + '%';
			}
		});
	});
	
	$('.subMenu').smint({
		'scrollSpeed' : 1000
	});

})
