
var footer_pages =['footer-first', 'footer', 'footer-last'];
var forms = ['personal', 'education', 'language', 'computer', 'certificate']

function loadFile(slector,name){
    path = '../static/html/'+name;
  	$(slector).load(path);
  	$(slector).html(path);
}
function stepNextActive(index){
	var headerSection = $('.steps li').eq(index);
    headerSection.removeClass("is-active").next().addClass("is-active");
}
function stepPrevActive(index){
	var headerSection = $('.steps li').eq(index);
    headerSection.removeClass("is-active").prev().addClass("is-active");
}
function stepActive(index){
	var headerSection = $('.steps li').eq(index);
    headerSection.addClass("is-active");
}
function sendData(index){
    var education =new Array();
    var jobs =new Array();
    var computer_level =new Array();
    var language_level =new Array();
    var certificates =new Array();

	if(index==0){
		personal_information ={
            "full_name":$("input[name ='full-name']").val(),
            "futher_name":$("input[name ='futher-name']").val(),
            "gender":$("input[name='gender']:checked").val(),
            "status":$("input[name='status']:checked").val(),
            "military":$("input[name='military']:checked").val(),
            "child_num":$("input[name ='child-num']").val(),
            "email": $("input[name='email']").val(),
            "mobil": $("input[name='mobil']").val(),
        };
        data={'personal_information': personal_information}
	}
	else if( index ===1){
        education.push({
            "level": $(this).find("td:eq(0)").text(),
            "majored":$(this).find("td:eq(1)").text(),
            "field":$(this).find("td:eq(2)").text(),
            "date_from" :$(this).find("td:eq(3)").find("input").val(),
            "date_to" :$(this).find("td:eq(4)").find("input").val(),
            "school":$(this).find("td:eq(5)").text(),
            "city": $(this).find("td:eq(6)").text(),
            "average": $(this).find("td:eq(7)").text(),
        })
	}
	else if( index ===1){}
	else if( index ===1){}
	else if( index ===1){}

    $.ajax({
        type: "POST",
        url: "employment/add/hierd/",
        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data){alert("Your information has been successfully saved.");},
        failure: function(errMsg) {
            alert("An error occurred");
        }
    });
}

function getPersonalData(){
    var pdata={};
    var data = new Array();
    var error = new Array();
    var a=$(".personal-information input");
    for(i=0 ; i<a.length ;i++){
        if(a[i].type==='radio'){
            if(a[i].checked===true){
                pdata[a[i].name]=a[i].value;
            }
        }
        else{
            pdata[a[i].name]=a[i].value;
            if(a[i].value === '')
                error.push(a[i].name);
        }
    }
    data.push({'personal_information':pdata});
    return [data, error];
}

function checkData(index){
    if(index === 0)
        out = getPersonalData();

    return [true,out[0]];
}

function send(data){
    console.log(data);
    $.ajax({
        type: "POST",
        url: "employment/add/hierd/",
        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data){},
        failure: function(errMsg) {
            alert("An error occurred");
        }
    });
}
function main(){
	var form_page_number =0;
	var form_footer_number =0;

	if(window.localStorage){
		form_page_number =parseInt(localStorage.getItem('form_page_number'));
		if(isNaN(form_page_number)){
			form_page_number =0;
		}
	}

	// set footer

	if(form_page_number<forms.length-1 & form_page_number>0){
		form_footer_number = 1;
		}
	else if(form_page_number == forms.length-1) {
        form_footer_number = 2;
    }
	loadFile("#form-content",forms[form_page_number]+".html");
	loadFile("#form-footer",footer_pages [form_footer_number]+".html");
	stepActive(form_page_number);
}

$('body').on('click', '#form-footer #next', function() {
  	form_page_number =parseInt(localStorage.getItem('form_page_number'));
	if(isNaN(form_page_number)){
		form_page_number =0;
	}
	out = checkData(form_page_number);
	if(out[0])
	    send(out[1])
	localStorage.setItem("form_page_number", form_page_number+1);
	main();
	sendData(form_page_number);
    stepNextActive(form_page_number);

    if(form_page_number === forms.length-1){
      $(document).find(".steps li").first().addClass("is-active");
    }
});


$('body').on('click', '#form-footer #back', function() {
  	form_page_number =parseInt(localStorage.getItem('form_page_number'));
	if(isNaN(form_page_number)){
		form_page_number =0;
	}
	localStorage.setItem("form_page_number", form_page_number-1);
	main();

    stepPrevActive(form_page_number);

});
main();