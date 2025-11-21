document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();

  const priceFilter = document.getElementById('price-filter');
  const priceOptions = ['All', 10, 50, 100];

  priceOptions.forEach(value => {
    const oneOption = document.createElement('option');
    oneOption.value = value;
    oneOption.textContent = value;
    priceFilter.appendChild(oneOption);
  });

  const localFilter = document.getElementById('local-filter');
  const worldOptions = ['All', 'Mist continent', 'Outer continent', 'Terra']

  worldOptions.forEach(value => {
    const oneOption = document.createElement('option');
    oneOption.value = value;
    oneOption.textContent = value;
    localFilter.appendChild(oneOption);
  });

  function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
      // Fetch places data if the user is authenticated
      fetchPlaces(token);
    }
  }
  function getCookie(name) {
    // Function to get a cookie value by its name
    const match = document.cookie
      .match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) {
      return match[2];
    } else {
      console.log('oopsie');
    }
  }

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

  function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = '';

    places.forEach(place => {
      const art = document.createElement('article');
      art.classList.add('place-card');
      art.innerHTML = `
            <h2>${place.title}</h2>
            <img src=${place.picture}>
            <p class="location">${place.location}</p>
            <p class="price"><span>Price per night:</span> ${place.price} gil</p>
            <button id="details-button"><a href="place.html?q=${place.id}">View Details</a></button>
        `;
      placesList.appendChild(art);
    });
  }

  priceFilter.addEventListener('change', filterByPrice);
  localFilter.addEventListener('change', filterByLocation);

  function filterByPrice() {
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
    })
  };

  function filterByLocation() {
    const where = document.getElementById('local-filter').value;
    const places = document.querySelectorAll('#places-list > .place-card');

    places.forEach(place => {
      const localLine = place.querySelector('.location');
      const locatedAt = localLine.textContent;
      console.log(locatedAt);

      if (where === 'All' || locatedAt === where) {
        place.style.display = 'block';
      } else {
        place.style.display = 'none';
      }
    })
  };

});
