$(document).ready(function () {
    $('#contactForm').on('submit', function (event) {
      event.preventDefault(); // prevent the form from submitting normally

      $.ajax({
        type: 'POST',
        url: '/contact/', // the URL to which the form data will be submitted
        data: $(this).serialize(), // serialize the form data for submission
        dataType: 'json',
        success: function (response) {
          if (response.status === 'true') {
            // if the response indicates success, show the success message
            $('.form-success-result').addClass('show');  //success
            setTimeout(() => {
             window.location.reload();
            }, 2000); 
          } else {
            // if the response indicates failure, show the error message
            alert(response.message); //error
          }
        },
        error: function (xhr, textStatus, errorThrown) {
          alert('An error occurred while submitting the form.');
        }
      });
    });
  });


// $('#contactForm').on('submit', function(e) {

//     e.preventDefault();
  
//     $.ajax({
//       type: 'POST',
//       url: '/contact/',
//       data: $(this).serialize(),
//       success: function(response) {
        
//         if(response.status === 'true') {
//            // Show success message
//            $('.form-success-result').addClass('show'); 
//            console.log('Form submitted!');
  
//            // Reload page
//            setTimeout(() => {
//             window.location.reload();
//           }, 500); 
  
//         } else {
//            alert(response.message);
//         }
  
//       }
//     });
  
//   });