$(document).ready(function() {

    // Check for click events on the navbar burger icon
    $(".navbar-burger").click(function() {
  
        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
  
    });

     $("#finish").change(function () {

     let start_date = $("#start").val();
     let end_date = $("#finish").val();
     if (start_date.length >0 ){
          const date1 = new Date(start_date);
          const date2 = new Date(end_date);
          const diffTime = Math.abs(date2 - date1);
          const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)) + 1;
          $("#dur").val(diffDays);
     }


  });

  });