// CRED: CI UCD Resume Template
function sendBookingConfirmation(contactForm) {
    emailjs.send("service_3cz29sk", "template_j6lagrm", {
        "name" :contactForm.name.value,
        "phone": contactForm.phone.value,
        "email": contactForm.email.value,
        "date": contactForm.date.value,
        "time": contactForm.time.value,
        "guests": contactForm.guests.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false; // To block from loading a new page on submission
}