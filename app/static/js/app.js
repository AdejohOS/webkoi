const showMenu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)

    if(toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('show')
            toggle.classList.toggle('bx-x')
        })
    }
}

showMenu('header-toggle', 'nav-menu')

const navLink = document.querySelectorAll('.nav-link')

function linkAction(){
    navLink.forEach(n => n.classList.remove('active'))
    this.classList.add('active')
}

navLink.forEach(n => n.addEventListener('click', linkAction))


//const r = rolly({
 //   view: document.querySelector('.app'),
 //   native: true,
 //   // other options
 // });
 // r.init();

 // AOS.init({
//      duration: 1500 //Global duration
//  });

//Flipster plugin

//$('.photos-container').flipster();


//Swiper for testimonies
let swiperEvents = new Swiper('.upcomingEvents', {
	cssMode: true,
	navigation: {
	  nextEl: '.swiper-button-next',
	  prevEl: '.swiper-button-prev'
	},
	slidesPerView: 1,
	spaceBetween: 10,
	// init: false,
	pagination: {
	  el: '.swiper-pagination-upcoming',
	  clickable: true,
	  dynamicBullets: true,
	},

  
	breakpoints: {
	  620: {
		slidesPerView: 1,
		spaceBetween: 20,
	  },
	  680: {
		slidesPerView: 2,
		spaceBetween: 40,
	  },
	  920: {
		slidesPerView: 3,
		spaceBetween: 40,
	  },
	  1240: {
		slidesPerView: 4,
		spaceBetween: 50,
	  },
	},
	mousewheel: true,
  	keyboard: true, 
    });



	//Swiper for testimonies

	let swiperTestimonies = new Swiper('.koiTestimonies', {
		        
		loop: true,
		grabCursor: true,
		spaceBetween:48,

		pagination: {
			el: '.swiper-pagination-testimonies',
			clickable: true,
			dynamicBullets:true,
		},
		autoplay: {
			delay: 5000,
		  },

		});


		//json search

	```	const searchField = document.querySelector('#searchField');

		const searchResult = document.querySelector('.search-result');
		searchResult.style.display = 'none';

		const searchResultInner = document.querySelector('.search-result-inner')

		const searchTable = document.querySelector('.search_table')

		const messageWrapper =document.querySelector('.message-wrapper');

		const messagePagination = document.querySelector ('.message-pagination');

		searchField.addEventListener('keyup', (e) => {

			const searchValue = e.target.value;

			if (searchValue.trim().length>0) {
				messagePagination.style.display = 'none';
				
				console.log('searchValue', searchValue);

				fetch('/message-search', {
					body: JSON.stringify({ searchText: searchValue }),
					method:"POST",
				})
				.then((res) => res.json())
				.then((data) => {
					console.log('data', data);

					messageWrapper.style.display = 'none';
					

					searchResult.style.display = 'block';

					if (data.length === 0){
						searchResult.innerHTML = 'No results found'
					}
					else{
						
						data.forEach(message=>{
							searchResultInner .innerHTML+=
						 
						    <p> </p>
							<p></p>
						 
						 
						 
						 

						})
						 
					}

				});

			}
			else{
				messagePagination.style.display = 'block';
				messageWrapper.style.display = 'block';
				searchResult.style.display = 'none';
			}

		}); ```

// Search form
// 1. Get search form and page links
let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('pageLinks')

// 2. Ensure search form exist

if(searchForm){
	for(let i=0; pageLinks.length > i; i++) {
		pageLinks[i].addEventListener('click', function (e) {
			e.preventDefault()

			//get data attribute

			let page = this.dataset.page

			//add hidden search input
			searchForm.innerHTML +- `<input value=${page} name="page" hidden/>`

			//submit form

			searchForm.submit()
		})
	}
}