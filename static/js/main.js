// animation for navigation
$(function() {
  $(".navigation__trigger").click(function(event) {
    event.preventDefault();
    $(".nav").slideToggle("fast", "linear");
  });

  $(".navigation__link").click(function(event) {
    if ($(window).width() > 435) {

    } else {
      $(".nav").slideToggle("fast", "linear");
    }
  });
});
