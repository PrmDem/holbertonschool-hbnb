function checkAuthentication() {
  // grabs and returns identifying token
  const token = getCookie('token');
  const loginLink = document.getElementById('login-link');

  if (!token) {
    loginLink.style.display = 'block';
  } else {
    loginLink.style.display = 'none';
    return token;
  }
}

function getCookie(name) {
  // Function to get a cookie value by its name
  const match = document.cookie
    .match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match[2];
}

export { checkAuthentication, getCookie };
