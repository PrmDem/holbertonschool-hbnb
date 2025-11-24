function checkAuthentication() { // Grabs and returns identifying token
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');
  const logoutLink = document.getElementById('logout-link');

  if (!token) { // Display login link only
    loginLink.style.display = 'block';
    logoutLink.style.display = 'none';
  } else { // Display logout link only
    loginLink.style.display = 'none';
    logoutLink.style.display = 'block';
  }

  if (logoutLink) { // Force token expiry on click
    logoutLink.addEventListener('click', (event) => {
      event.preventDefault();
      document.cookie = 'token=; path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT';
      logoutLink.style.display = 'none';
      window.location.reload();
    });
  }

  // Return token only after checking it exists and logout hasn't been triggered
  return token
}

function getCookie(name) {
  // Function to get a cookie value by its name
  const match = document.cookie
    .match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match[2];
}

export { checkAuthentication, getCookie };
