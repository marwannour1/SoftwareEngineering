//jQuery time
$(document).ready(function () {
  var current_fs, next_fs, previous_fs; //fieldsets
  var left, opacity, scale; //fieldset properties which we will animate
  var animating = false; //flag to prevent quick multi-click glitches
  let i = 0;  //index of myForm
  let j = 3;  //index of search limit
  $(".next").click(function () {
    for (let x = i; x<j; x++){   //loop through the three forms in every page
      if(x == 2){                       //checks if password and confirm password are the same
        if($(".myForm").eq(x).val() != $(".myForm").eq(x-1).val()){            
          alert("Password and confirm password do not match")
          return false
        }
      }
      if (x == 5){           //checks if number has 11 digits as any egyptian number
        if ($(".myForm").eq(x).val().toString().length != 11){
          alert("invalid phone number")
          return false;
        }
      }

      if ($(".myForm").eq(x).val() == ""){            //check if the rest of the forms are not empty
        $(".myForm").eq(x).css("border", "2px solid red")
        return false;
      }else{
        $(".myForm").eq(x).css("border", "none")
      }
    }
    if (animating) return false;
	
    animating = true;
    i+=3
    j+=3;

    current_fs = $(this).parent();
    next_fs = $(this).parent().next();

    //activate next step on progressbar using the index of next_fs
    $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

    //show the next fieldset
    next_fs.show();
    //hide the current fieldset with style
    current_fs.animate(
      { opacity: 0 },
      {
        step: function (now, mx) {
          //as the opacity of current_fs reduces to 0 - stored in "now"
          //1. scale current_fs down to 80%
          scale = 1 - (1 - now) * 0.2;
          //2. bring next_fs from the right(50%)
          left = now * 50 + "%";
          //3. increase opacity of next_fs to 1 as it moves in
          opacity = 1 - now;
          current_fs.css({
            transform: "scale(" + scale + ")",
            position: "absolute",
          });
          next_fs.css({ left: left, opacity: opacity });
        },
        duration: 800,
        complete: function () {
          current_fs.hide();
          animating = false;
        },
        //this comes from the custom easing plugin
        easing: "easeInOutBack",
      }
    );
  });

  $(".previous").click(function () {
    if (animating) return false;
    animating = true;
    i-=3;
    j-=3;

    current_fs = $(this).parent();
    previous_fs = $(this).parent().prev();

    //de-activate current step on progressbar
    $("#progressbar li")
      .eq($("fieldset").index(current_fs))
      .removeClass("active");

    //show the previous fieldset
    previous_fs.show();
    //hide the current fieldset with style
    current_fs.animate(
      { opacity: 0 },
      {
        step: function (now, mx) {
          //as the opacity of current_fs reduces to 0 - stored in "now"
          //1. scale previous_fs from 80% to 100%
          scale = 0.8 + (1 - now) * 0.2;
          //2. take current_fs to the right(50%) - from 0%
          left = (1 - now) * 50 + "%";
          //3. increase opacity of previous_fs to 1 as it moves in
          opacity = 1 - now;
          current_fs.css({ left: left });
          previous_fs.css({
            transform: "scale(" + scale + ")",
            opacity: opacity,
          });
        },
        duration: 800,
        complete: function () {
          current_fs.hide();
          animating = false;
        },
        //this comes from the custom easing plugin
        easing: "easeInOutBack",
      }
    );
  });
});
