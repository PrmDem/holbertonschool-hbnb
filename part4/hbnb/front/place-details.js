document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();

  function checkAuthentication() {
    const token = getCookie('token');
    const placeID = getPlaceIdFromURL();
    const loginLink = document.getElementById('login-link');

    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
    }

    fetchPlaceDetails(token, placeID);
  }
  function getCookie(name) {
    // Function to get a cookie value by its name
    const match = document.cookie
      .match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match[2];
  }
  function getPlaceIdFromURL() {
    // Function to recover place ID from URL
    const params = new URLSearchParams(window.location.search);
    const placeID = params.get('q');
    return placeID;
  }

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

  function displayPlaceDetails(place) {
    console.log(place);
    const secPlace = document.getElementById('place-details');
    secPlace.innerHTML = '';

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

    redirSubmitForm(place);
  }

  function redirSubmitForm(place) {
    const btn = document.getElementById('submit');
    btn.addEventListener('click', () => {
      window.location.href = `add_review.html?q=${place.id}`;
    });
  }
});
