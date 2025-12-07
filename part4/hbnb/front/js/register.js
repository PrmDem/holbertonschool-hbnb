async function createAccount(accData) {
  const response = await fetch('http://127.0.0.1:5000/api/v1/users/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      first_name: accData.first,
      last_name: accData.last,
      email: accData.email,
      password: accData.password,
      is_admin: false
    })
  });
  console.log(response);
  if (response.ok) { // Validation msg + redirect to index
    window.alert('Account created successfully!');
    window.location.assign = 'http://localhost:5501/part4/hbnb/front/index.html';
  } else {
    window.alert('Something went wrong, kupo...');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const regiForm = document.getElementById('register-form');
  if (!regiForm) return;

  regiForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    const regiData = {
      first: document.getElementById('first-name').value,
      last: document.getElementById('last-name').value,
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
      verif: document.getElementById('verif').value
    };

    if (regiData.password !== regiData.verif) {
      window.alert('You need to enter the same password twice, kupo!');
    } else {
      createAccount(regiData);
    }
  });
});
