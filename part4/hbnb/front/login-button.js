document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();
  function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
    }
  }
  function getCookie(name) {
    // Function to get a cookie value by its name
    const match = document.cookie
      .match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match[2];
  }
});