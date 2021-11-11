const header = document.querySelector('#header');
const nav = header.offsetHeight;

window.addEventListener('scroll', function() {
    if(window.scrollY >= nav) {

        header.classList.add('scroll')

    } else {
        header.classList.remove('scroll')

    }
})

const swiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    pagination: {
        el: '.swiper-pagination',
    },
    //opera pelo mouse e teclado
    mousewheel: true,
    keyboard: true
});

// Scroll Reveal 
const sr = ScrollReveal({
    origin: 'top',
    distance: '30px',
    duration: 1000,
    reset: true
});

sr.reveal(
`#home img, #home .text,
#about img, #about .text,
#services img, #services .text,
#testimonials img, #testimonials .text,
#contact img, #contact .text`
, { interval: 100});