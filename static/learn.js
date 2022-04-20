function edit_entry(new_entry,curr_id){
	let time = new_entry["time"]
	let data_to_save = {"time": time, "id_rn":curr_id}
	console.log(data_to_save)
	$.ajax({
		type: "POST",
		url: "edit_entry",
		dataType : "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(data_to_save),
		success: function(result){
			console.log("Success")
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


  $(".edit-submit").click(function(){


    let curr_id = $('.edit-submit').attr('name')

    let new_id = parseInt(curr_id)+1
    /**If condition for last learn page**/
    if(new_id == 12){
      window.location.href = "http://127.0.0.1:5000/middle";
    }else{
      window.location.href = "http://127.0.0.1:5000/learn/"+new_id;
      let time =  new Date($.now())
      let new_entry = {"time": time}
      edit_entry(new_entry, curr_id)
    }




  })

})
