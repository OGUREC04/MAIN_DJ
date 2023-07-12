

$('#multi-select')
  .dropdown()
;

$('.ui.accordion')
  .accordion()
;


const iconMenu = document.querySelector('.burger');
const menuBody = document.querySelector('.menu');
const iconBody = document.querySelector('.icon');
if (iconMenu) {
  iconMenu.addEventListener("click", function (e) {
    document.body.classList.toggle('_lock');
    iconMenu.classList.toggle('_active');
    menuBody.classList.toggle('_active');
    iconBody.classList.toggle('_active');
  });
}


const btn = document.querySelector('.button');
const pop = document.querySelector('.popup');
const close = document.querySelector('.closeModal');
if (btn) {
  btn.addEventListener("click", function (e) {
    document.body.classList.toggle('_lock');
    btn.classList.toggle('_active');
    pop.classList.toggle('_active');
  });
}

 if (close){
  close.addEventListener("click", function (e) {
  document.body.classList.toggle('_lock');
  pop.classList.toggle('_active');
});
  
}


