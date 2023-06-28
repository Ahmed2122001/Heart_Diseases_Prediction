var closeButton = document.getElementsByClassName('close');
var alertContainer = document.getElementsByClassName('D_alert');

for (let i = 0; i < closeButton.length; i++) {
  closeButton[i].addEventListener('click', (function(index) {
    return function() {
      alertContainer[index].style.display = "none";
    };
  })(i));
}