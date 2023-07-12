var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var marker;

document.querySelector('form').addEventListener('submit', function(e) {
  e.preventDefault();
  var lat = document.querySelector('#latitude').value;
  var lng = document.querySelector('#longitude').value;
  if (marker) {
    map.removeLayer(marker);
  }
  marker = L.marker([lat, lng]).addTo(map);
  map.setView([lat, lng], 13);
});