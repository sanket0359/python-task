// Simple form validation
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();  // Prevents form from submitting the traditional way

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (name && email && message) {
        alert('Thank you for your message! I will get back to you soon.');
        document.getElementById('contactForm').reset();  // Reset form fields after submission
    } else {
        alert('Please fill in all fields.');
    }
});
