document.getElementById("edit-button").addEventListener("click", function() {
    var profile = document.querySelector(".profile");
    var editForm = document.getElementById("edit-form");
  
    profile.classList.add("hidden");
    editForm.classList.remove("hidden");
  
    // Pre-fill form fields with current values
    var name = document.getElementById("name");
    var age = document.getElementById("age");
    var gender = document.getElementById("gender");
    var city = document.getElementById("city");
    var phone = document.getElementById("phone");
    var email = document.getElementById("email");
    name.value = "John Doe";
    age.value = 30;
    gender.value = "male";
    city.value = "Giza";
    phone.value = '011111111111';
    email.value = "mazen1145@gmail.com";
  });
  
  // document.getElementById("edit-form").addEventListener("submit", function(event) {
  //   event.preventDefault();
  
  //   var name = document.getElementById("name").value;
  //   var age = document.getElementById("age").value;
  //   var gender = document.getElementById("gender").value;
  //   var city = document.getElementById("city").value;
  //   var phone = document.getElementById("phone").value;
  //   var email = document.getElementById("email").value;
  
  //   // Perform save/update operation with the values
  
  //   var profile = document.querySelector(".profile");
  //   var editForm = document.getElementById("edit-form");
  
  //   profile.classList.remove("hidden");
  //   editForm.classList.add("hidden");
  
  //   // Update profile with new values
  //   var profileName = document.querySelector(".profile h2");
  //   var profileAge = document.querySelectorAll(".profile p")[0];
  //   var profilegender = document.querySelectorAll(".profile p")[1];
  //   var profilecity = document.querySelectorAll(".profile p")[2];
  //   var profilephone = document.querySelectorAll(".profile p")[3];
  //   var profileemail = document.querySelectorAll(".profile p")[4];
    
  //   profileName.textContent = "Name: " + name;
  //   profileAge.textContent = "Age: " + age;
  //   profilegender.textContent = "Gender: " + gender;
  //   profilecity.textContent = "City: " + city;
  //   profilephone.textContent = "Phone Number: " + phone;
  //   profileemail.textContent = "Email: " + email;
  // });
  