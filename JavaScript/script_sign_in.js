$("document").ready(function () {
    $('input[type="email"], input[type="password"]').focus(function () {
      var background = $(this).attr("id");
      $("#" + background + "-form").addClass("formgroup-active");    // adds happy octopus on focus
    });
    $('input[type="email"], input[type="password"]').blur(function () {
      var background = $(this).attr("id");
      $("#" + background + "-form").removeClass("formgroup-active");     //removes happy octopus 
    });
  
    function errorfield(field) {                //function to add sad octopus 
      $(field).addClass("formgroup-error");
      console.log(field);
    }
  
    $("#waterform").submit(function () {
      var stopsubmit = false;             // instantiate stop submit of button to false
  
      if ($("#email").val() == "") {       // if email has no value on submit it will show sad octopus and prevent submit
          errorfield("#email-form");        
          stopsubmit = true;
        }
        if ($("#password").val() == "") {
          errorfield("#password-form");        //if password has no value on submit it will show sad octopus and prevent submit
          stopsubmit = true;
        }
      if (stopsubmit) return false;             // will submit if email and password have values
    });
  });