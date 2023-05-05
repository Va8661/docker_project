// Get a reference to the form and the token number element
const form = document.querySelector('#appointment-form');
const tokenNumber = document.querySelector('#token-number');

// Add an event listener to the form submission event
form.addEventListener('submit', (event) => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Generate a random token number
  const randomNumber = Math.floor(Math.random() * 1000);

  // Display the token number in the element
  tokenNumber.textContent = `Your token number is ${randomNumber}`;
});
