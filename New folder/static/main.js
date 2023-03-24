
function scale(){
  let ad1 = document.querySelector('.AD1');
  let ad2 = document.querySelector('.AD2');
  let ad3 = document.querySelector('.AD3');
  if (ad1.style.transform == 'scale(1)') {
    ad1.style.transform = 'scale(1.11)';
    ad2.style.transform = 'scale(1.11)';
    ad3.style.transform = 'scale(1.11)';
  } else {
    ad1.style.transform = 'scale(1)';
    ad2.style.transform = 'scale(1)';
    ad3.style.transform = 'scale(1)';
  }
};
window.setInterval(scale, 2000);

document.addEventListener('DOMContentLoaded', function () {
  visit = document.querySelector('#visit');
  visit.addEventListener('click', function (event) {
    location.href = '/visit';
    event.preventDefault();
  });
});

document.addEventListener('DOMContentLoaded', function () {
  visit = document.querySelector('.night');
  styleo = document.querySelector('.styleo');
  visit.addEventListener('click', function (event) {
    visit.style.color = 'red';
    styleo.href = '/static/night.css'; 
    // if (styleo.href == '/static/style.css') {
    //   styleo.href == '/static/night.css';
    // } else {
    //   styleo.href == '/static/style.css';
    // }
    // location.href = '/night';
    event.preventDefault();
  });
});
