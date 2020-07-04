/*back to top*/
jQuery(document).ready( function( $ ){
    "use strict";
    $('body').append('<div id="toTop" class="btn hidden-xs"><i class="fa fa-long-arrow-up"></i>Back to top </div>');
    $(window).scroll(function () {
        if ($(this).scrollTop() != 0) {
            $('#toTop').fadeIn();
        } else {
            $('#toTop').fadeOut();
        }
    });
    $('#toTop').click(function(){
        $("html, body").animate({ scrollTop: 0 }, 600);
        return false;
    });


    /** Search Panel **/
    $('.search-panel .dropdown-menu').find('a').on("click",function(e) {
        e.preventDefault();
        var param = $(this).attr("href").replace("#","");
        var concept = $(this).text();
        $('.search-panel span#search_concept').text(concept);
        $('.input-group #search_param').val(param);
    });

    /*Span menu click index3 */
    //Search
    $('a.search-header4').on('click', function () {
        $(this).removeAttr('href');
        var element = $(this).parent('span');
        if (element.hasClass('active')) {
            element.removeClass('active');
            element.find('span').removeClass('active');
            $('#search-home4').slideUp();
        }
        else {
            element.addClass('active');
            $('#search-home4').slideDown();
        }

    });
    $('a.search-header4').on('hover', function () {
        $(this).removeAttr('href');
        var element = $(this).parent('span');
        if (element.hasClass('active')) {
            element.removeClass('active');
            element.find('span').removeClass('active');
            $('#search-home4').slideUp();
        }
        else {
            element.addClass('active');
            $('#search-home4').slideDown();
        }

    });
    $('#close').on('click',function() {
        $('a.search-header4').parent('span').removeClass('active');
        $('#search-home4').slideUp();
    });
    $("#hl_head").on('click',function(){
                $("#hl_body").slideToggle('active');
    });
    $( ".top-header-v3 .btn-nav-icon" ).on('click',function() {
        $(".top-header-v3").toggleClass( "highlight" );
    });

    /*icon-nav*/
    var iconmenu = $('.btn-nav-icon'),
        vmenu    = $('.vmegamenu-contain');

        iconmenu.on('click', function(e){
            if ($(this).hasClass('active')){
                iconmenu.removeClass('active');
                vmenu.removeClass('active');
            }
            else {
                iconmenu.addClass('active');
                vmenu.addClass('active');
            }
            e.preventDefault();
        });

    /** Mega menu **/
    $(window).load(function() {
        "use strict";
	    $("ul.engo-megamenu > li.dropdown").each(function () {
	        var dropdown        = $(this).children(".dropdown-menu");
	        var megamenu       = $("ul.engo-megamenu");
	        $(dropdown).css("right", "auto");

	        var dropdown_begin_mega = $(this).offset().left - megamenu.offset().left;
	        if($(this).hasClass('aligned-fullwindown')) {
	            var dropdown_begin = $(this).offset().left;
	            $(dropdown).css({'left':-dropdown_begin,'width':$(window).width()});
	        } else if($(this).hasClass('aligned-fullwidth')) {
	            $(dropdown).css({'left':-dropdown_begin_mega,'width':$(megamenu).outerWidth()});
	        } else if($(this).hasClass('aligned-right')) {
	            var dropdown_end_right = ($(megamenu).offset().left + $(megamenu).outerWidth()) - ($(this).offset().left + $(this).outerWidth()) ;
	            // console.log(dropdown_end_right);
	            $(dropdown).css({'right':-dropdown_end_right});
	        } else if($(this).hasClass('aligned-left')) {
	            $(dropdown).css({'left':-dropdown_begin_mega});
	        } else {
	            var end_right     = ($(window).width() - (dropdown.offset().left + dropdown.outerWidth()));
	            var end_right2    = ($(window).width() - (megamenu.offset().left + megamenu.outerWidth()));
	            if(end_right2 > end_right) {
	            }
	        }
	        $(this).hover(function () {
	            $("ul.engo-megamenu > li").removeClass("active");
	            $(this).addClass("active");

		        },function () {
		            $(this).removeClass("active");
		        });
			});
		});
    /** Vervical toggle menu **/
    $('.toggle-dropdown-menu ul li.item-toggle-dropdown').each(function(){
            if ($(this).find('.item-toggle-menu').length > 0) {
                $(this).append('<i class="closed toggle-button fa fa-plus"></i>');
            }
            $(this).find('.item-toggle-menu').slideUp('fast');
        });
    $( "body" ).on( "click", '.toggle-dropdown-menu ul li.item-toggle-dropdown .closed', function(){
        $(this).parent().find('.item-toggle-menu').first().slideDown('fast');
        $(this).removeClass('closed').removeClass('fa-plus').addClass('opened').addClass('fa-minus');
    });
    $( "body" ).on( "click", '.toggle-dropdown-menu ul li.item-toggle-dropdown .opened', function(){
        $(this).parent().find('.item-toggle-menu').first().slideUp('fast');
        $(this).removeClass('opened').removeClass('fa-minus').addClass('closed').addClass('fa-plus');
    });


/** Swiper slider **/

/*Homepage_02*/
var swiper1 = new Swiper('#new-ticker', {
             pagination: '.swiper-pagination',
             nextButton: '.swiper-button-next',
             prevButton: '.swiper-button-prev',
             paginationClickable: true,
             spaceBetween: 30,
             centeredSlides: true,
             autoplay: 2500,
             autoplayDisableOnInteraction: false
         });
/*Homepage_01*/
var swiper2 = new Swiper('#popularproduct', {
             pagination: '.swiper-pagination',
             paginationClickable: true,
             slidesPerView: 6,
             spaceBetween: 30,
             nextButton: '.swiper-button-next',
             prevButton: '.swiper-button-prev',
             breakpoints: {
                 480: {
                     slidesPerView: 1,
                     spaceBetweenSlides: 10
                 },
                 640: {
                     slidesPerView: 2,
                     spaceBetweenSlides: 30
                 },
                 1024: {
                     slidesPerView: 3,
                     spaceBetweenSlides: 30
                 },
                 1200: {
                     slidesPerView: 4,
                     spaceBetweenSlides: 30
                 },
                1366: {
                     slidesPerView: 5,
                     spaceBetweenSlides: 30
                 }  
             }
         });
var swiper22 = new Swiper('#popularproduct-v2', {
             pagination: '.swiper-pagination',
             paginationClickable: true,
             slidesPerView: 6,
             spaceBetween: 30,
             nextButton: '.swiper-button-next',
             prevButton: '.swiper-button-prev',
             breakpoints: {
                 480: {
                     slidesPerView: 1,
                     spaceBetween: 10
                 },
                 640: {
                     slidesPerView: 2,
                     spaceBetween: 30
                 },
                 1024: {
                     slidesPerView: 3,
                     spaceBetween: 30
                 },
                 1200: {
                     slidesPerView: 4,
                     spaceBetween: 30
                 },
                1366: {
                     slidesPerView: 5,
                     spaceBetween: 30
                 } 
             }
         });
var swiper23 = new Swiper('#popularproduct-v3', {
             pagination: '.swiper-pagination',
             paginationClickable: true,
             slidesPerView: 6,
             spaceBetween: 30,
             nextButton: '.swiper-button-next',
             prevButton: '.swiper-button-prev',
             breakpoints: {
                 480: {
                     slidesPerView: 1,
                     spaceBetween: 10
                 },
                 640: {
                     slidesPerView: 2,
                     spaceBetween: 30
                 },
                 1024: {
                     slidesPerView: 3,
                     spaceBetween: 30
                 },
                 1200: {
                     slidesPerView: 4,
                     spaceBetween: 30
                 },
                1366: {
                     slidesPerView: 5,
                     spaceBetween: 30
                 } 
             }
         });

/*brank-logo*/
var swiper3 = new Swiper('#brank-logo', {
             pagination: '.swiper-pagination',
             paginationClickable: true,
             slidesPerView: 9,
             spaceBetween: 20,
             nextButton: '.swiper-button-next',
             prevButton: '.swiper-button-prev',
             autoplay: 3000,
             breakpoints: {
                320: {
                     slidesPerView: 2,
                     spaceBetween: 10
                 },
                640: {
                     slidesPerView: 3,
                     spaceBetween: 20
                 },
                 768: {
                     slidesPerView: 4,
                     spaceBetween: 30
                 },
                 1024: {
                     slidesPerView: 5,
                     spaceBetween: 40
                 }
                
                 
                 
             }
         });
/*Homepage_01-lastestblog*/
var swiper4 = new Swiper('#swiper-container', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        keyboardControl: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false,
        breakpoints: {
                // when window width is <= 320px
                 420: {
                     slidesPerView: 1,
                     spaceBetween: 10
                 },
                 680: {
                     slidesPerView: 2,
                     spaceBetween: 30
                 },

                 768: {
                     slidesPerView: 1,
                     spaceBetween: 30
                 }
                
             }
    });
/*Homepage_01*/
var swiper5 = new Swiper('#dailydeals', {
        pagination: '.swiper-pagination',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        keyboardControl: true,
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        breakpoints: {
                 420: {
                     slidesPerView: 1,
                     spaceBetween: 10
                 },
                 680: {
                     slidesPerView: 2,
                     spaceBetween: 30
                 },

                 768: {
                     slidesPerView: 1,
                     spaceBetween: 30
                 }
                 
                 
                
             }
    });

/*product_single_post2*/
var zoomConfig = {
    galleryActiveClass: "active"
}
var galleryTop = new Swiper('.gallery-top2', {
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        spaceBetween: 10,
        onInit: function (swiper) {
            // console.log(swiper.activeIndex);
            var zoomImage = $('.gallery-top2 .swiper-slide:eq('+swiper.activeIndex+') .zoom_01');
            // Remove old instance od EZ
            $('.zoomContainer').remove();
            zoomImage.removeData('elevateZoom');
            zoomImage.data('zoom-image', zoomImage.data('zoom-image'));
            zoomImage.elevateZoom();
        },
        onSlideChangeEnd: function (swiper) {
            console.log(swiper.activeIndex);
            var zoomImage = $('.gallery-top2 .swiper-slide:eq('+swiper.activeIndex+') .zoom_01');
            // Remove old instance od EZ
            $('.zoomContainer').remove();
            zoomImage.removeData('elevateZoom');
            zoomImage.data('zoom-image', zoomImage.data('zoom-image'));
            zoomImage.elevateZoom();
        }

    });
    var galleryThumbs = new Swiper('.gallery-thumbs2', {
        spaceBetween: 10,
        slidesPerView: 3,
        centeredSlides: true,
        paginationClickable: true,
        grabCursor: true,
        slideToClickedSlide: true
    });
    galleryTop.params.control = galleryThumbs;
    galleryThumbs.params.control = galleryTop;

});