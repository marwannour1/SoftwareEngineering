$("document").ready(function () {
    $('input[type="email"], input[type="password"]').focus(function () {
      var background = $(this).attr("id");
      $("#" + background + "-form").addClass("formgroup-active");
      $("#" + background + "-form").removeClass("formgroup-error");
    });
    $('input[type="email"], input[type="password"]').blur(function () {
      var background = $(this).attr("id");
      $("#" + background + "-form").removeClass("formgroup-active");
    });
  
    function errorfield(field) {
      $(field).addClass("formgroup-error");
      console.log(field);
    }
  
    $("#waterform").submit(function () {
      var stopsubmit = false;
  
      if ($("#email").val() == "") {
          errorfield("#email-form");
          stopsubmit = true;
        }
        if ($("#password").val() == "") {
          errorfield("#password-form");
          stopsubmit = true;
        }
      if (stopsubmit) return false;
    });
  });