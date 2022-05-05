function show_answers() {
    for (let ind in question_data){
        console.log(ind)
        console.log(question_data[ind])
        if (right_ans[ind-1]){
            var $div =  $("<div class='right-wrong'> Question " + ind + " <i class='fa fa-check'></i> </div>")
        }
        else{
            var $div =  $("<div class='right-wrong'> Question " + ind + " <i class='fa fa-close'></i> </div>")
        }
        $(".answer").append($div)
    }    
}

function show_review_block() {
    let $div = $(`<div> Click on <b> <span class="links"> <a href="/"> REVIEW </a> </span> </b> to revisit lessons. </div>`);
    $("#result-content").append($div)
}


$(document).ready(function(){
	show_answers()
    if(single_data < 9) {
        show_review_block()
    }
})