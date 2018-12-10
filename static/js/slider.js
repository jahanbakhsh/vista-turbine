var slideIndex = 1;
slideCode = "<div class='mySlides fade'> <img  style=\"width:100%\"> <div class=\"text\"></div></div>"

$.ajax({
	  url: "/fc/news",
	  type: "get", //send it through get method
	  data: {
		'type': "Main",
	  },
	  success: function(response) {
        data = response.data;
        for(i = 0; i<data.length ; i++){
            $(".slideshow-container").append(
                "<div class='mySlides fade'> <img src='"+data[i].large_img+"' style='width:100%'> <div class='text'> <h3>"+data[i].title+"</h3></div></div>"
            );
            $(".slide-changer").append("<span class='dot' onclick='currentSlide("+(i+1)+")'></span>");
         }
        showSlides();
	  },
	  error: function(xhr) {
		console.log('error', xhr);
	  }
});


function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}


function showSlides() {
    var i;
    var slides = $(".mySlides");
        console.log( slides.length);
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}

    slides[(slideIndex-1)].style.display = "block";

    setTimeout(showSlides, 5000); // Change image every 2 seconds
}
showSlides(slideIndex);
//plusSlides(-1);

// Player


