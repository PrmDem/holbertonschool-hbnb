document.addEventListener('DOMContentLoaded', () => {
    const reviewForm = document.getElementById('review-form');
    const token = checkAuthentication();
    const placeId = getPlaceIdFromURL();

    function checkAuthentication() {
        // Function to ensure user is logged in
        const token = getCookie('token');
        const loginLink = document.getElementById('login-link');

        if (!token) {
            loginLink.style.display = 'block';
            window.location.href = 'index.html';
        } else {
            loginLink.style.display = 'none';
            return token;
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
    function getPlaceIdFromURL() {
        // Function to recover place ID from URL
        const params = new URLSearchParams(window.location.search);
        const placeID = params.get('q');
        return placeID;
    }

    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const reviewText = reviewForm.get(review); // Get review text from form
            console.log(reviewText);

            submitReview(token, placeId, reviewText);

            async function submitReview(token, placeId, reviewText) {
                // Make a POST request to submit review data
                const response = await fetch('http://127.0.0.1:5000/api/v1/reviews', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `Bearer ${token}` // Include the token in the Authorization header
                    },
                    body: JSON.stringify({ placeId, reviewText }) // Send placeId and reviewText in the request body
                });
                handleResponse(response);
            }
            function handleResponse(response) {
                if (response.ok) {
                    alert('Review submitted successfully!');
                    reviewForm.set()
                } else {
                    alert('Failed to submit review');
                }
            }
        });
    }
});

