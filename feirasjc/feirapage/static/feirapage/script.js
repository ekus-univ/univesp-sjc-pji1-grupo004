const header = document.querySelector('#header');
const nav = header.offsetHeight;

window.addEventListener('scroll', function() {
    if(window.scrollY >= nav) {

        header.classList.add('scroll')

    } else {
        header.classList.remove('scroll')

    }
})