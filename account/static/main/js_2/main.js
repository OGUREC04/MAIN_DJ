const burger = document.querySelector('.header_burger')
if (burger){
    const Headermenu = document.querySelector(".header_menu")
    burger.addEventListener("click", function (e){
        // document.body.classList.toggle('_lock');
        burger.classList.toggle('_active');
        Headermenu.classList.toggle('_active');
    })
}

"use strict"

window.onload = function (){
    const parallax = document.querySelector('.page_screen');

    if (parallax){
        const image = document.querySelector('.screen_image-parallax')
        console.log('123')


        const forImage = 70;

        const speed = 0.05;

        let positionX = 0,   positionY = 0;
        let cordXprocent = 0,   cordYprocent = 0;

        function setMouseParallaxStyle() {
            const distX = cordXprocent - positionX;
            const distY = cordYprocent - positionY;

            positionX = positionX + (distX * speed)
            positionY = positionY + (distY * speed)


            image.style.cssText = 'transform: translate(${positionX / forImage}%, ${positionY / forImage}%);';

            requestAnimationFrame(setMouseParallaxStyle);
        }
        setMouseParallaxStyle();

        parallax.addEventListener("mousemove", function (e){
            const parallaxWidth = parallax.offsetWidth;
            const parallaxHeight = parallax.offsetHeight;



            const cordX = e.pageX-parallaxWidth / 2;
            const cordY = e.pageY-parallaxHeight / 2;


            cordXprocent = cordX / parallaxWidth * 100;
            cordYprocent = cordY / parallaxHeight * 100;

        });

        }
    }




















// $(function() {
//     let header = $('.header');
//     let mobileTel = $('.main-menu').first(); // сохранем в переменную первый элемент с классом header__tel
//     let hederHeight = header.height(); // вычисляем высоту шапки
//
//     $(window).scroll(function() {
//         if ($(this).scrollTop() > 1) {
//             header.addClass('header_fixed');
//             $('body').css({
//                 'paddingTop': hederHeight + 'px' // делаем отступ у body, равный высоте шапки
//             });
//         } else {
//             header.removeClass('header_fixed');
//             $('body').css({
//                 'paddingTop': 0 // удаляю отступ у body, равный высоте шапки
//             })
//         }
//
//         if ($(this).scrollTop() > 300) {
//             header.css({
//                 'padding': '2px 0',
//                 'background': '#f6ffdb',
//                 'transition': '.3s'
//             });
//         } else {
//             header.css({
//                 'padding': '10px 0',
//                 'background': ' #dfb96a',
//                 'transition': '.3s'
//             });
//         }
//
//
//         if ($(this).scrollTop() > 500) {
//             mobileTel.fadeOut();
//         } else {
//             mobileTel.fadeIn();
//         }
//     });
// });
//
//
