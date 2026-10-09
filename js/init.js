// Hamburger Animation
jQuery(".hamburger").click(function () {
  jQuery(".hamburger").toggleClass("is-active");
  jQuery(".menu-wrap").toggleClass("is-open");
});

// Auto-close mobile menu when an item is tapped
jQuery(".menu-wrap a").click(function () {
  jQuery(".hamburger").removeClass("is-active");
  jQuery(".menu-wrap").removeClass("is-open");
});

jQuery(document).ready(function($) {
  var $name = $('.sub-menu')
  let revealsubmenu = false
    $('.subMenuTrig').click(function(){
    if (revealsubmenu === false) {
      $($name).slideUp(500);
      $(this).find($name).slideToggle(500);
        revealsubmenu = true
      } else {
        $(this).find($name).slideToggle(500);
        $(this).siblings().find($name).slideUp(500);
        revealsubmenu = false
    }
  });
  });