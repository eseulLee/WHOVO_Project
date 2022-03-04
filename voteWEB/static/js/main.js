(function($) {
    "use strict";
    
    /*----------------------------
    jQuery MeanMenu
    ------------------------------ */
    $('nav#dropdown').meanmenu({
        meanScreenWidth: "991",
        meanMenuContainer: ".mobile-menu",
    });
    
    
    /*----------------------------
     counter js active
    ------------------------------ */
    $('.counter').counterUp({
        delay: 10,
        time: 2000
    });
    
    
    /*----------------------------
     owl active
    ------------------------------ */
    $('.slider-active').owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: false,
        nav: true,
        items: 4,
        margin:30,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            },
            1200: {
                items: 3
            }
        }
    });
    
    
    /*----------------------------
     owl active
    ------------------------------ */
    $('.slider-active2').owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: false,
        nav: true,
        items: 3,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 1
            },
            992: {
                items: 2
            },
            1200: {
                items: 3
            }
        }
    });
    
    
    /*----------------------------
     owl active
    ------------------------------ */
    $('.slider-active3').owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: false,
        nav: true,
        items: 1,
        /* transitionStyle : "fade", */
        /* [This code for animation ] */
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
    });
    
    
    /*----------------------------
     owl active
    ------------------------------ */
    $('.slider-active4').owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: false,
        nav: true,
        items: 3,
        /* transitionStyle : "fade", */
        /* [This code for animation ] */
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 1
            },
            992: {
                items: 2
            },
            1200: {
                items: 3
            }
        }
    });
    
    
    /*----------------------------
     owl active
    ------------------------------ */
    $('.president').owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: false,
        nav: true,
        items: 3,
        margin: 30,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            },
            1200: {
                items: 3
            }
        }
    });
    
    
    /*----------------------------
     owl active
    ------------------------------ */
    $('.slider-active5').owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: false,
        nav: true,
        items: 4,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            768: {
                items: 1
            },
            992: {
                items: 2
            },
            1200: {
                items: 4
            }
        }
    });
    
    
    /*----------------------------
    owl active brand-logo
    ------------------------------ */
    $('.slider-active6').owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        dots: true,
        nav: false,
        items: 1,
    });
    
    
    /*--------------------------
    scrollUp
    ---------------------------- */
    var toTop = $('#toTop');
    var win = $(window);
    
    win.on('scroll', function() {
        if (win.scrollTop() > 200) {
            toTop.fadeIn();
        } else {
            toTop.fadeOut();
        }
    });
    toTop.on('click', function() {
        $("html,body").animate({
            scrollTop: 0
        }, 500)
    });
    
    
    /*--
    Magnific Popup
    ------------------------*/
    $('.video-popup').magnificPopup({
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: false,
        zoom: {
            enabled: true,
        }
    });
    
    
    /*---------------------
    countdown
    --------------------- */
    $('[data-countdown]').each(function() {
        var $this = $(this),
            finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function(event) {
            $this.html(event.strftime('<span class="cdown day">%-D <p>Days</p></span> <span class="cdown hour">%-H <p>Hour</p></span> <span class="cdown minutes">%M <p>Min</p></span class="cdown second"> <span>%S <p>Sec</p></span>'));
        });
    });
    
    
    //venbox start
    $('.venobox').venobox({
        numeratio: true,
        infinigall: true,
        titleattr: 'data-title'
    })
    //venbox end
    
    
    /*----------------------------
     sticky active
    ------------------------------ */
    var header = $('.stick-h2');
    
    win.on('scroll', function() {
        var scroll = win.scrollTop();
        if (scroll < 245) {
            header.removeClass('stick');
        } else {
            header.addClass('stick');
        }
    });
    
    
    /*----------------------------
     wow js active
    ------------------------------ */
    new WOW().init();
    
    
    /*----------------------------
    Isotope js active
    ------------------------------ */
    $('.grid').imagesLoaded(function() {
        // filter items on button click
        $('.gallery-menu').on('click', 'button', function() {
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({
                filter: filterValue
            });
        });
        // init Isotope
        var $grid = $('.grid').isotope({
            itemSelector: '.grid-item',
            percentPosition: true,
            masonry: {
                // use outer width of grid-sizer for columnWidth
                columnWidth: '.grid-item',
            }
        });
    });
    $('.gallery-menu button').on('click', function(event) {
        $(this).siblings('.active').removeClass('active');
        $(this).addClass('active');
        event.preventDefault();
    });
    
    
    /*----------------------------
        youtube active
    ------------------------------ */
    $('.youtube-bg').YTPlayer({
        containment: '.youtube-bg',
        autoPlay: true,
        loop: true,
    });


    
    /*------------------------------------
        DateCountdown active 1
    ------------------------------------- */
    $(".DateCountdown").TimeCircles({
        direction: "Counter-clockwise",
        fg_width: 0.009,
        bg_width: 0,
        use_background: false,
        time: {
            Days: {
                text: "Days",
                color: "#fff"
            },
            Hours: {
                text: "Hours",
                color: "#fff"
            },
            Minutes: {
                text: "Mins",
                color: "#fff"
            },
            Seconds: {
                text: "Secs",
                color: "#fff"
            }
        }
    }); 
    
    
    
    
    
    
    
    
    


})(jQuery);