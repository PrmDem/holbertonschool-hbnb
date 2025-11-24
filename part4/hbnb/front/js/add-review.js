import { checkAuthentication } from './checkauth.js';

// ---------- FETCHES PLACE INFO TO DISPLAY ABOVE REVIEW FORM ----------

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
    return (data);
  } catch (error) {
    window.alert('Error' + error.message);
  }
}


// ---------- SENDS REVIEW DATA ----------
async function submitReview(token, placeId, reviewData) {
  const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}` // Include the token in the Authorization header
    },
    body: JSON.stringify({ text: reviewData.text, rating: reviewData.rating, place_id: placeId }) // Send placeId and reviewText in the request body
  });
  handleResponse(response, placeId);
}

function handleResponse(response, placeId) {
  if (response.ok) { // Validation msg + redirect to reviewed place
    window.alert('Review submitted successfully!');
    window.location.href = `http://localhost:5501/part4/hbnb/front/place.html?q=${placeId}`;
  } else if (response.status === 401) { // Specific login error msg + redirect to login form
    window.alert('Authentication required. Please log back in, stat.');
    window.location.href = 'http://localhost:5501/part4/hbnb/front/login.html';
  } else if (response.status === 400) { // Specific error message + redirect to reviewed place
    window.alert('You have already reviewed this place, kupo!');
    window.location.href = `http://localhost:5501/part4/hbnb/front/place.html?q=${placeId}`;
  } else {
    window.alert('Failed to submit review');
  }
}


// ---------- ON PAGE LOAD ----------

document.addEventListener('DOMContentLoaded', async () => {
  const token = checkAuthentication();
  if (!token) {
    console.error('Authentication token is missing or empty');
    window.alert('Authentication required. Please log back in, stat.');
    window.location.href = 'http://localhost:5501/part4/hbnb/front/login.html';
  }
  const params = new URLSearchParams(window.location.search);
  const placeID = params.get('q');
  const placeData = await fetchPlaceDetails(token, placeID);
  const whereTo = document.getElementById('review-where');
  whereTo.textContent = `You are reviewing ${placeData.owner.first_name}'s ${placeData.title}`;

  const reviewForm = document.getElementById('review-form');
  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const reviewData = {
        text: document.getElementById('review').value,
        rating: parseInt(document.getElementById('pick-rating').value)
      }
      submitReview(token, placeID, reviewData);
    });
  }
});
