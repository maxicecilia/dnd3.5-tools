/*!
* js code need for the sticky sidebar.
*/

$(document).ready(function() {
  $('#sidebar').affix({
        offset: {
          top: 45
        }
  });

  var $body   = $(document.body);
  var navHeight = $('.navbar').outerHeight(true) + 10;

  $body.scrollspy({
    target: '#leftCol',
    offset: navHeight
  });
});