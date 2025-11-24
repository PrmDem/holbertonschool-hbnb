function checkAuthentication() {
    // grabs and returns identifying token
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    const logoutLink = document.getElementById('logout-link');

    if (!token) {
        loginLink.style.display = 'block';
        logoutLink.style.display = 'none';
    } else {
        loginLink.style.display = 'none';
        logoutLink.style.display = 'block';
        return token;
    }
}

function getCookie(name) {
    // Function to get a cookie value by its name
    const match = document.cookie
        .match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match[2];
}

document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();
});