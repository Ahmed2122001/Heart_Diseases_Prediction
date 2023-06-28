// JavaScript code
const historyItems = document.querySelectorAll('.history-item');

historyItems.forEach(item => {
  item.addEventListener('click', () => {
    item.classList.toggle('show-details');
  });
});