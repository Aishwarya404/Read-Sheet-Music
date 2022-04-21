function display_options(){
	$(".quiz_question").text(question_data["Question"]);
	console.log("aa")
	console.log(question_data)
	let $options = $(`<form action="/quiz" method="post"></form>`);
	if (question_data["question_image"]){
		for (let image in question_data["Image"]){
			let question_img = $("<img src = '" + question_data['Image'][image] + "' id='theImg'>")
			console.log(question_data["Image"][image])
			$(".quiz_image").append(question_img)
		}
	}

	if (question_data["question_image"]){
    	for(let letter in question_data['Answers']){
        	$options.append(`<input type="radio" name="${question_data['id']}" id = "${letter}" value="${letter}" /> ${question_data['Answers'][letter]}<br/>`);
    	}
	}
	else{
		for(let letter in question_data['Answers']){
        	$options.append(`<input type="radio" name="${question_data['id']}" id = "${letter}" value="${letter}" /> <img src = "${question_data['Answers'][letter]}" id='theImg'> <br/>`)
    	}
	}
	$(".quiz_options").append($options);
}

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
			console.log(result)
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
	console.log("aaaaaaaaa")
	display_options()
    $(".next").click(function(){

		var $chosen_ans = $('input[name=' + question_data["id"] +']:checked').val();

        // let answer = $radio.attr("value")
		// console.log(answer)
        //let curr_id = $('.next').attr('name')
        validate_answer($chosen_ans, question_data["id"])
	})
})
  