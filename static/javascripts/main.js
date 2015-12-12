
/*$('.circle').each(function(){
	console.log($(this).attr("percentage"))
})

$('.circle').each(function(){
	var $percent = $(this).attr("percentage");
	$(this).circleProgress({
		value: $percent,
		startAngle: Math.PI*1.5,
		reverse: true,
		size: 80,
		thickness: 80/10,
		animation: false,
		fill: { gradient: ["green", "blue"] }
	});
});*/

$(document).ready(function(){

	var $knob_colors = ['red', 'green', 'blue'];
	var alternate = 0;

	function choose_knob_color(){
		if(alternate == 3)alternate = 0;
		return $knob_colors[alternate++];
	}

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

})
