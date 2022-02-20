$(document).ready(function(){
	$('#loading').hide();
	$("#customfile").click(function(e){
		e.preventDefault();
		$('#loading').show();
		var path = $("#csvfile").val();
		$.ajax({
			//change url below
			url : "/predict",
			type: "POST",
			data: {filepath:path},
			success: function(response){
				$(".json-result").html('<p>Response :</p><pre>' + response + '</pre>');	
				$('#loading').hide();
			}
		});
	});
	$("#defaultfile").click(function(e){
		e.preventDefault();
		$('#loading').show();
		var path = $(this).attr("data-path");
		$.ajax({
			//change url below
			url : "/predict",
			type: "POST",
			data: {filepath:path},
			success: function(response){
				$(".json-result").html('<p>Response :</p><pre>' + response + '</pre>');
				$('#loading').hide();
			}
		});
		
	});
});
