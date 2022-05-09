// Contributors : Aishwarya Sivakumar, Roshan Babu, Nidhi Sunil Kumar, Yina Jian
// UNI : as6418, rbk2145, ns3566, yj2713

function display_options(){
	$(".question_no").text("Question " + question_data["id"]);
	$(".quiz_question").text(question_data["Question"]);
	let $options = $(`<form action="/quiz" method="post"></form>`);
	if (question_data["question_image"]){
		for (let image in question_data["Image"]){
			let question_img = $("<div class='inline'> <img src = '" + question_data['Image'][image] + "' class='qImage' width='" + question_data['Size'][0] + "' height='" + question_data['Size'][1] + "'> </div>")
			$(".quiz_image").append(question_img)
		}
	}

	if (question_data["answer_image"]){
		for(let letter in question_data['Answers']){
        	$options.append(`<input type="radio" name="${question_data['id']}" id = "${letter}" value="${letter}" /> <img src = "${question_data['Answers'][letter]}" class='aImage'> <br> <br>`)
    	}
	}
	else{
		for(let letter in question_data['Answers']){
        	$options.append(`<input type="radio" name="${question_data['id']}" id = "${letter}" value="${letter}" class="aOption"/> <label> ${question_data['Answers'][letter]} </label> <br/>`);
    	}
	}
	$(".quiz_options").append($options);
}


function validate_answer(answer, id){
	let data_to_save = {"answer": answer, "id": id}
	$.ajax({
		type: "POST",
		url: "http://127.0.0.1:5000/calculate_score",
		dataType : "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(data_to_save),
		success: function(result){
			console.log(result)
            if(parseInt(result) == 11){
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
	display_options()
    $(".next").click(function(){
		if ($("input[type=radio]:checked").length == 0) {
			window.alert("Question Not answered! Please choose an option.")
		} else {
			var $chosen_ans = $('input[name=' + question_data["id"] +']:checked').val();
       		validate_answer($chosen_ans, question_data["id"])
		}
	})
})
