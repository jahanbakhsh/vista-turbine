
function main() {

(function () {
   'use strict';
   
  	$('a.page-scroll').click(function() {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
          var target = $(this.hash);
          target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
          if (target.length) {
            $('html,body').animate({
              scrollTop: target.offset().top - 50
            }, 900);
            return false;
          }
        }
      });

	
    // Show Menu on Book
    $(window).bind('scroll', function() {
        var navHeight = $(window).height() - 500;
        if ($(window).scrollTop() > navHeight) {
            $('.navbar-default').addClass('on');
        } else {
            $('.navbar-default').removeClass('on');
        }
    });

    $('body').scrollspy({ 
        target: '.navbar-default',
        offset: 80
    });

	// Hide nav on click
  $(".navbar-nav li a").click(function (event) {
    // check if window is small enough so dropdown is created
    var toggle = $(".navbar-toggle").is(":visible");
    if (toggle) {
      $(".navbar-collapse").collapse('hide');
    }
  });
	
  	// Portfolio isotope filter
    $(window).load(function() {
        var $container = $('.portfolio-items');
        $container.isotope({
            filter: '*',
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
        });
        $('.cat a').click(function() {
            $('.cat .active').removeClass('active');
            $(this).addClass('active');
            var selector = $(this).attr('data-filter');
            $container.isotope({
                filter: selector,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            return false;
        });

    });
	
    // Nivo Lightbox 
    $('.portfolio-item a').nivoLightbox({
            effect: 'slideDown',  
            keyboardNav: true,                            
        });
		
	// Testimonial Slider
	  	$(document).ready(function() {
	      $("#testimonial").owlCarousel({
        navigation : false, // Show next and prev buttons
        slideSpeed : 300,
        paginationSpeed : 400,
        singleItem:true
        });

  	});	

}());


}
main();

var img = document.getElementById("capabilitie-img")
var modal_img = document.getElementById("capabilitie-img-large")
var modal = document.getElementById("capilitie-modal")
img.onclick=function(evt){
    modal_img.src = this.src;
    modal.style.display = "block";
    img.style.display = "none";
}
var close = document.getElementsByClassName("close")[0];

close.onclick = function(evt){
    modal.style.display = "none";
    img.style.display = "block";
}

// employment form
$(".submit-form").click(function(evt){
        var education =new Array();
        var jobs =new Array();
        var computer_level =new Array();
        var language_level =new Array();
        var certificates =new Array();
        $(".education table tr").each(function () {
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
        })
        $(".job1 table tr").each(function () {
            jobs.push({
                "company": $(this).find("td:eq(0)").text(),
                "employment": $(this).find("td:eq(1)").text(),
                "date_from":$(this).find("td:eq(2)").find("input").val(),
                "date_to": $(this).find("td:eq(3)").find("input").val(),
                "position": $(this).find("td:eq(4)").text(),
                "salary": $(this).find("td:eq(5)").text(),
                "reason": $(this).find("td:eq(6)").text(),
                "description":$(".job1 textarea").val(),
            })
        })
        $(".job2 table tr").each(function () {
            jobs.push({
                "company": $(this).find("td:eq(0)").text(),
                "employment": $(this).find("td:eq(1)").text(),
                "date_from":$(this).find("td:eq(2)").find("input").val(),
                "date_to": $(this).find("td:eq(3)").find("input").val(),
                "position": $(this).find("td:eq(4)").text(),
                "salary": $(this).find("td:eq(5)").text(),
                "reason": $(this).find("td:eq(6)").text(),
                "description":$(".job2 textarea").val(),
            })
        })
        $(".job3 table tr").each(function () {
            jobs.push({
                "company": $(this).find("td:eq(0)").text(),
                "employment": $(this).find("td:eq(1)").text(),
                "date_from":$(this).find("td:eq(2)").find("input").val(),
                "date_to": $(this).find("td:eq(3)").find("input").val(),
                "position": $(this).find("td:eq(4)").text(),
                "salary": $(this).find("td:eq(5)").text(),
                "reason": $(this).find("td:eq(6)").text(),
                "description":$(".job3 textarea").val(),
            })
        })
        $(".language table tr").each(function () {
            language_level.push({
                "language": $(this).find("td:eq(0)").text(),
                "level": $(this).find("td:eq(1)").find("select").val(),
            })
        })
        $(".computer table tr").each(function () {
            computer_level.push({
                "program": $(this).find("td:eq(0)").text(),
                "level": $(this).find("td:eq(1)").find("select").val(),
            })
        })
        $(".certificate table tr").each(function () {
            certificates.push({
                "certificate": $(this).find("td:eq(0)").text(),
                "score":$(this).find("td:eq(1)").text(),
                "issued":$(this).find("td:eq(2)").text(),
                "date":$(this).find("td:eq(3)").find("input").val()
            })
        })
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

        data = {
            'education': education,
            'personal_information': personal_information,
            'jobs': jobs,
            'certificates':certificates,
            'language_level':language_level,
            'computer_level':computer_level,
        }
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
    });
