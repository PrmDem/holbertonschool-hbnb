import { checkAuthentication } from './checkauth.js';

// ---------- FUNCTIONS TO FETCH AND DISPLAY PLACE ----------

// Fetches place data
async function fetchPlaceDetails(token, placeId) {
  try {
    const placeUrl = `http://127.0.0.1:5000/api/v1/places/${placeId}`;
    const response = await fetch(placeUrl, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      }
    });
    if (!response.ok) {
      window.alert('Something went wrong, kupo :(' + response.statusText);
      return;
    }
    const data = await response.json();
    // Displays place details after verification auth/aut
    displayPlaceDetails(data);
  } catch (error) {
    window.alert('Error' + error.message);
  }
}

// Displays place details from fetched data
function displayPlaceDetails(place) {
  const secPlace = document.getElementById('place-details');
  secPlace.innerHTML = ''; // Empties place section, clearing previously checked place

  const deets = document.createElement('article');
  deets.classList.add('detailed-card');
  deets.innerHTML = `
          <h2>${place.title}</h2>
          <img src=${place.picture}>
          <p class="location">${place.location}</p>
          <p class="description">${place.description}</p>
          <p class="price"><span>Price per night:</span> ${place.price} gil</p>
        `;

  secPlace.appendChild(deets);

  const ameniText = document.createElement('p');
  ameniText.classList.add('amenities');
  place.amenities.forEach(amenity => {
    ameniText.textContent += `${amenity.name} `;
  });

  deets.appendChild(ameniText);

  // checks whether there are reviews or not
  const reviewList = place.reviews;
  if (!reviewList || reviewList.length === 0) {
    const sectionR = document.getElementById('reviews');
    const noRevs = document.createElement('p');
    noRevs.classList.add('no-reviews');
    noRevs.textContent = 'There are no reviews for this place yet!';
    sectionR.appendChild(noRevs);
  } else {
    displayReviews(reviewList);
  }
}

// ---------- FUNCTION TO DISPLAY EXISTING REVIEWS ----------

async function displayReviews(allReviews) {
  console.log(allReviews);
  const revSection = document.getElementById('reviews');
  if (!revSection) {
    console.log('section reviews not found');
    return; // Exit if the section isn't found
  }
  revSection.innerHTML = ''; // clear past loaded reviews

  allReviews.forEach(rev => {
    const revContents = document.createElement('article'); // create new reviews space
    revContents.classList.add('review');
    revContents.innerHTML = `
    <p id="rating">${rev.rating}</p>
    <blockquote class="review-body">${rev.text}<br/><br/>
    <cite class="reviewer">${rev.user.first_name}</cite>
    </blockquote>
    `;
    revSection.appendChild(revContents);
  });
}

// ---------- ON PAGE LOAD ----------

document.addEventListener('DOMContentLoaded', () => {
  const token = checkAuthentication();
  const params = new URLSearchParams(window.location.search);
  const placeID = params.get('q');

  fetchPlaceDetails(token, placeID);

  const btn = document.getElementById('submit');
  btn.addEventListener('click', () => {
    window.location.href = `add_review.html?q=${placeID}`;
  });
});
