// CRED: CI UCD Resume 

function sendBookingConfirmation(formElement) {
    console.log('Form submitted:', formElement);

    emailjs.sendForm('service_3cz29sk', 'template_j6lagrm', {
        "name" :contactForm.name.value,
        "number" :contactForm.number.value,
        "email": contactForm.email.value,
        "date": contactForm.date.value,
        "time": contactForm.time.value,
        "guest": contactForm.date.value
    })
        .then((result) => {
            console.log('Booking confirmation email sent:', result);
            alert('Booking confirmation email sent successfully!');
            // Optionally redirect to the booking list page
            window.location.href = '/bookings/my-bookings/';
        }, (error) => {
            console.error('Error sending booking confirmation email:', error);
            alert('Failed to send booking confirmation email. Please try again later.');
        });

    return false; // Prevent the default form submission
}
