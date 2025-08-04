var swiper = new Swiper(".mySwiper2", {
	// slidesPerView: 3,
	spaceBetween: 40,
	slidesPerGroup: 1,
	loop: true,
	loopFillGroupWithBlank: true,
	pagination: {
	  el: ".swiper-pagination",
	  clickable: true,
	},
	autoplay: {
        delay: 3000,
        disableOnInteraction: false,
      },
	// navigation: {
	//   nextEl: ".swiper-button-next",
	//   prevEl: ".swiper-button-prev",
	// },
	breakpoints: {
        0: {
          slidesPerView: 2,
	// slidesPerGroup: 1,

        },
        540: {
          slidesPerView: 3,
	// slidesPerGroup: 2,

        },
        768: {
          slidesPerView: 4,
	// slidesPerGroup: 2,

        },
        1024: {
          slidesPerView: 5,
	// slidesPerGroup: 2,

        },
      },
  });
