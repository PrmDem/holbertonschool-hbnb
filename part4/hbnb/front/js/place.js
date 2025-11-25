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

  secPlace.innerHTML = `
          <h2>${place.title}</h2>
          <div class="slideshow">
            <img src="${place.picture}1.jpg">
            <img src="${place.picture}2.jpg">
            <img src="${place.picture}3.jpg">
            <img src="${place.picture}4.jpg">
          </div>
          <p class="location">Enjoy ${place.owner.first_name}'s gorgeous space in ${place.location}!</p>
          <p class="description">${place.description}</p>
          <p class="price"><span>Price per night:</span> ${place.price} gil</p>
          <h3>Included in the price:</h3>
        `;

  const amenityList = document.createElement('ul');
  amenityList.classList.add('amenities');
  amenityList.innerHTML = '';

  place.amenities.forEach(amenity => {
    const oneAm = document.createElement('li');
    oneAm.textContent = `${amenity.name}`;
    amenityList.appendChild(oneAm);
  });

  secPlace.appendChild(amenityList);

  // checks whether there are reviews or not
  const reviewList = place.reviews;
  if (!reviewList || reviewList.length === 0) {
    const sectionR = document.getElementById('reviews-list');
    const noRevs = document.createElement('li');
    noRevs.classList.add('no-reviews');
    noRevs.innerHTML = "<p>There are no reviews for this place yet!</p>";
    sectionR.appendChild(noRevs);
  } else {
    displayReviews(reviewList);
  }
}

// ---------- FUNCTION TO DISPLAY EXISTING REVIEWS ----------

async function displayReviews(allReviews) {
  const revSection = document.getElementById('reviews-list');
  revSection.innerHTML = ''; // clear past loaded reviews

  allReviews.forEach(rev => {
    const revContents = document.createElement('li'); // create new reviews space
    revContents.classList.add('review');
    revContents.innerHTML = `
        <p id="rating">${rev.rating} <img src="images/icons/${rev.rating}.ico"></p>
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
