function validate_answer(answer, id){
	let data_to_save = {"answer": answer, "id": id}
	console.log("D", data_to_save)
	$.ajax({
		type: "POST",
		url: "http://127.0.0.1:5000/calculate_score",
		dataType : "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(data_to_save),
		success: function(result){
            if(parseInt(result) == 6){
                window.location.href = "http://127.0.0.1:5000/result";
            }else{
                window.location.href = "http://127.0.0.1:5000/quiz/"+parseInt(result);
            }
		},
		error: function(request, status, error){
			console.log("Error");
			console.log(request)
			console.log(status)
			console.log(error)
		}
	});
}

$(document).ready(function(){
    $(".next").click(function(){
        answer = $('#answer').val()
        let curr_id = $('.next').attr('name')
        validate_answer(answer, parseInt(curr_id))
    })
})
  