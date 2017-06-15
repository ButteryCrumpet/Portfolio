$(document).ready(function() {
  console.log("run script")
  var $root = $('html, body')

  $("a[href*=\\#]").on('click', function(event) {
      $root.animate(
        { scrollTop: $(this.hash).offset().top },
        1000,
      )});
  });
