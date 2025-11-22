import './checkauth.js';

function filterByPrice () {
  const maxPrice = document.getElementById('price-filter').value;
  const places = document.querySelectorAll('#places-list > .place-card');

  places.forEach(place => {
    const priceLine = place.querySelector('.price');
    const onlyFloat = parseFloat(priceLine.textContent.replace(/\D/g, ''));

    if (maxPrice === 'All' || onlyFloat <= parseFloat(maxPrice)) {
      place.style.display = 'block';
    } else {
      place.style.display = 'none';
    }
  });
}

function filterByLocation () {
  // Get filter choice info & all place cards to analyse
  const where = document.getElementById('local-filter').value;
  const places = document.querySelectorAll('#places-list > .place-card');

  places.forEach(place => {
    const localLine = place.querySelector('.location');
    const locatedAt = localLine.textContent; // location of the place

    if (where === 'All' || locatedAt === where) {
      place.style.display = 'block'; // if All or place location is the filtered choice
    } else {
      place.style.display = 'none'; // hide places that don't match the filtered choice
    }
  });
}
