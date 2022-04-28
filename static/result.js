function show_answers() {
    for (let ind in question_data){
        console.log(ind)
        console.log(question_data[ind])
        if (right_ans[ind-1]){
            var $div =  $("<div> Question " + ind + ". <img src = '/static/pictures/check.png' class='qImage'> </div>")
            console.log("R")
        }
        else{
            var $div =  $("<div> Question " + ind + ". <img src = '/static/pictures/cross.png' class='qImage'> </div>")
            console.log("W")
        }

        $(".answer").append($div)
        $(".answer").append("<br>")
    }
        
}
function show_review_block() {
    let $div = $(`<div> Click on Review to revisit lessons </div>`);
    $("#result-content").append($div)
    let $link = $(`<div class="link"> <a href="/"> REVIEW </a> </div>`);
    $("#result-content").append($link)
}


$(document).ready(function(){
	show_answers()
    if(single_data < 5) {
        show_review_block()
    }
})