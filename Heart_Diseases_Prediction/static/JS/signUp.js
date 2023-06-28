// document.getElementById("signUpForm").addEventListener("submit", function(event) {
//     event.preventDefault();

//     var username = document.getElementById("username").value;
//     var password = document.getElementById("password").value;
//     var email = document.getElementById("email").value;
//     var gender = document.getElementById("gender").value;
//     var phone = document.getElementById("phone").value;
//     var age = document.getElementById("age").value;
//     var address = document.getElementById("address").value;

//     // Perform client-side validation
//     var errorMessages = [];

//     if (username.length < 3) {
//       errorMessages.push("Username must be at least 3 characters long.");
//     }

//     if (password.length < 6) {
//       errorMessages.push("Password must be at least 6 characters long.");
//     }

//     if (!email.includes("@")) {
//       errorMessages.push("Please enter a valid email address.");
//     }

//     if (!phone.match(/^\d+$/)) {
//       errorMessages.push("Phone number must contain only digits.");
//     }

//     var errorContainer = document.getElementById("errorMessages");
//     errorContainer.innerHTML = "";

//     if (errorMessages.length > 0) {
//       for (var i = 0; i < errorMessages.length; i++) {
//         var errorMessage = document.createElement("p");
//         errorMessage.textContent = errorMessages[i];
//         errorContainer.appendChild(errorMessage);
//       }
//     } else {
//       // Submit the form
//       document.getElementById("signinForm").submit();
//     }
//   });