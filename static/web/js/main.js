(function ($) {
    "use strict";
  	/*----------------------------------------
 	          Preloader
 	 ----------------------------------------*/

    // Mean Menu JS
	jQuery('.mean-menu').meanmenu({ 
		meanScreenWidth: "991"
    });
    
    // Search Menu JS
    $(".search-box i").on("click", function(){
		$(".search-overlay").toggleClass("search-overlay-active");
	});
	$(".search-overlay-close").on("click", function(){
		$(".search-overlay").removeClass("search-overlay-active");
	});

	// Header Sticky
	$(window).on('scroll',function() {
		if ($(this).scrollTop() > 120){  
			$('.navbar-area').addClass("is-sticky");
		}
		else{
			$('.navbar-area').removeClass("is-sticky");
		}
	});


    // Home One Banner Slider JS
	$('.home_one_banner_slider').owlCarousel({
		items: 1,
		loop: true,
		margin: 15,
		nav: false, 
		dots: true,
		smartSpeed: 1000,
		autoplay: false,
		autoplayTimeout: 4000,
		autoplayHoverPause: true,
	});
    // What We Do Slider
    $('.what_we_slider').owlCarousel({
        loop:true,
        margin:30,
        dots:true,
        nav:false,
        autoplay:false,
        responsiveClass:true,
        autoplaySpeed:1000,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:3,
            }
        }
    })
    // Our Portfolio
    $('.our_portfolio_slider').owlCarousel({
        loop:true,
        margin:0,
        dots:true,
        nav:false,
        autoplay:false,
        responsiveClass:true,
        autoplaySpeed:1000,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2,
            },
            1000:{
                items:4,
            }
        }
    })
    // Our Client
    $('.client_wrappers ').owlCarousel({
        loop:true,
        margin:20,
        dots:true,
        nav:false,
        autoplay:false,
        responsiveClass:true,
        autoplaySpeed:1000,
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:1,
            },
            1000:{
                items:1,
            }
        }
    })

    
    /* Our Partner */
    $('.partner_slider').owlCarousel({
        loop:true,
        margin:20,
        dots:false,
        autoplay:false,
        responsiveClass:true,
        autoplaySpeed:1000,
        nav:false,
        responsive:{
            0:{
                items:3,
            },
            600:{
                items:4,
            },
            1000:{
                items:6,
            }
        }
    })

     /* Home Two Banner */
    $('.home_two_banner_slider').owlCarousel({
        loop:true,
        margin:20,
        dots:true,
        nav:false,
        autoplay:false,
        responsiveClass:true,
        autoplaySpeed:1000,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    })
 /* Case Study Slider */
 $('.case_study_home_slider').owlCarousel({
    loop:true,
    margin:0,
    dots:true,
    items:1,
    nav:false,
    autoplay:false,
    responsiveClass:true,
    autoplaySpeed:1000,
})
   
    /* Counter */
    $('.count').each(function () {
        $(this).prop('Counter',0).animate({
          Counter: $(this).text()
        },  {
          duration: 10000,
          easing: 'swing',
          step: function (now) {
              $(this).text(Math.ceil(now));
            }
        });
    });

     /* Team_Area_slider */
    $('.team_slider_wrapper').owlCarousel({
        loop:true,
        margin:20,
        nav:false,
        dots:true,
        autoplay:true,
        autoplaySpeed:1000,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:3
            }
        }
    })
     /* Testimonial Slider */
     $('.client_sliders_wrappers').owlCarousel({
        loop:true,
        margin:10,
        nav:true,
        dots:false,
        autoplay:true,
        autoplaySpeed:1000,
        navText : ["<i class='fas fa-arrow-left fa-2x'></i>","<i class='fas fa-arrow-right fa-2x'></i>"], 
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:1
            },
            1000:{
                items:2
            }
        }
    })
     /* Client Slider */
     $('.client_logo_slider').owlCarousel({
        loop:true,
        margin:10,
        nav:false,
        dots:false,
        autoplay:true,
        autoplaySpeed:1000,
        navText : ["<i class='fas fa-arrow-left fa-2x'></i>","<i class='fas fa-arrow-right fa-2x'></i>"], 
        responsive:{
            0:{
                items:1,
            },
            600:{
                items:2
            },
            1000:{
                items:5
            }
        }
    })

// Video Area
$('.video_btn').magnificPopup({
    disableOn: 50,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,

    fixedContentPos: false
});
    
}(jQuery));

