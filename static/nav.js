$('.menu-icon-toggle').on('click', function(e) {
  $('body').toggleClass('open');

  e.preventDefault();
});

$('#faq-link').on('click', function(e) {
  $('body').removeClass('open');
  window.location.assign("http://127.0.0.1:8000/#faq");
  e.preventDefault();
});

$('#team-link').on('click', function(e) {
  $('body').removeClass('open');
  window.location.assign("http://127.0.0.1:8000/#team");
  e.preventDefault();
});

$('#contact-link').on('click', function(e) {
  $('body').removeClass('open');
  window.location.assign("http://127.0.0.1:8000/#contact");
  e.preventDefault();
});
