import { checkAuthentication } from './checkauth.js';

// ---------- SENDS REVIEW DATA ----------
async function submitReview(token, placeId, reviewData) {
  console.log(placeId, token, reviewData);
  const response = await fetch('http://127.0.0.1:5000/api/v1/reviews/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}` // Include the token in the Authorization header
    },
    body: JSON.stringify({ text: reviewData.text, rating: reviewData.rating, place_id: placeId }) // Send placeId and reviewText in the request body
  });
  console.log(response);
  handleResponse(response);
}
function handleResponse(response) {
  if (response.ok) {
    window.alert('Review submitted successfully!');
  } else if (response.status === 401) {
    window.alert('Authentication required. Please log back in, stat.');
    window.location.href = 'http://localhost:5501/part4/hbnb/front/login.html';
  } else {
    window.alert('Failed to submit review');
  }
}

// ---------- ON PAGE LOAD ----------

document.addEventListener('DOMContentLoaded', () => {
  const token = checkAuthentication();
  if (!token) {
    console.error('Authentication token is missing or empty');
    window.alert('Authentication required. Please log back in, stat.');
    window.location.href = 'http://localhost:5501/part4/hbnb/front/login.html';
  }
  const params = new URLSearchParams(window.location.search);
  const placeID = params.get('q');
  const reviewForm = document.getElementById('review-form');

  if (reviewForm) {
    reviewForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const reviewData = {
        text: document.getElementById('review').value,
        rating: parseInt(document.getElementById('rating').value)
      }
      submitReview(token, placeID, reviewData);
    });
  }
});
