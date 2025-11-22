import { checkAuthentication } from './js/checkauth.js';

// ---------- FUNCTIONS TO FETCH AND DISPLAY PLACES ----------

// Fetching data for all places
async function fetchPlaces(token) {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/places', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      }
    });
    if (!response.ok) {
      window.alert('There is nowhere to go!' + response.statusText);
      return;
    }
    const data = await response.json();
    // Displays places after verification auth/aut
    displayPlaces(data);
  } catch (error) {
    window.alert('Error' + error.message);
  }
}

// Displays places as cards
function displayPlaces(places) {
  const placesList = document.getElementById('places-list');
  placesList.innerHTML = ''; // Empties previous list, clearing filters

  places.forEach(place => {
    const art = document.createElement('article');
    art.classList.add('place-card');
    art.innerHTML = `
            <h2>${place.title}</h2>
            <img src=${place.picture}>
            <p class="location">${place.location}</p>
            <p class="latitude hidden">lat: ${place.latitude}</p>
            <p class="price"><span>Price per night:</span> ${place.price} gil</p>
            <button id="details-button"><a href="place.html?q=${place.id}">View Details</a></button>
        `;
    placesList.appendChild(art);
  });
}

// ---------- SETTING FILTERS BY PRICE AND CONTINENT ----------

const priceFilter = document.getElementById('price-filter');
const priceOptions = ['All', 100, 250, 500];

priceOptions.forEach(value => { // Populates price filter options
  const oneOption = document.createElement('option');
  oneOption.value = value;
  oneOption.textContent = value;
  priceFilter.appendChild(oneOption);
});

const localFilter = document.getElementById('local-filter');

// Filters by price *and* continent
function filterAll() {
  const maxPrice = document.getElementById('price-filter').value;
  const where = document.getElementById('local-filter').value;
  const places = document.querySelectorAll('#places-list > .place-card');

  places.forEach(place => {
    const priceLine = place.querySelector('.price');
    const onlyFloat = parseFloat(priceLine.textContent.replace(/\D/g, '')); // Selecting the float part of price line
    const latLine = place.querySelector('.latitude');
    const locatedAt = parseFloat(latLine.textContent.replace(/\D/g, '')); // location of the place

    let priceMatch = (maxPrice === 'All' || onlyFloat <= parseFloat(maxPrice));
    let latMatch = (where === 'All' || locatedAt === parseFloat(where));

    if (priceMatch && latMatch) {
      place.style.display = 'block';
    } else {
      place.style.display = 'none';
    }
  });
}

// ---------- ON PAGE LOAD ----------

document.addEventListener('DOMContentLoaded', () => {
  const token = checkAuthentication();
  fetchPlaces(token);

  priceFilter.addEventListener('change', filterAll);
  localFilter.addEventListener('change', filterAll);
});