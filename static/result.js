function show_review_block() {
    let $div = $(`<div> Click on Review to revisit lessons </div>`);
    $("#result-content").append($div)
    let $link = $(`<div class="link"> <a href="/"> REVIEW </a> </div>`);
    $("#result-content").append($link)
}


$(document).ready(function(){
	if(single_data < 5) {
        show_review_block()
    }
})