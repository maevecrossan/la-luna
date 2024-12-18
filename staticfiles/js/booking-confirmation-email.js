// CRED: CI UCD Resume Template
function sendBookingConfirmation(bookingForm) {
    if (form.checkValidity()) {
        // Get all input elements within the form
        var inputs = form.querySelectorAll('input, textarea, select');

        // Object to hold form data
        var formData = {};
        var isValid = true;

        // Check each input field
        for (var i = 0; i < inputs.length; i++) {
            var input = inputs[i];
            if (input.required && !input.value) {
                alert("Please fill out the " + input.name + " field.");
                isValid = false;
                break;
            }
            formData[input.name] = input.value;
        }

        if (isValid) {
            emailjs.sendForm("service_3cz29sk", "template_j6lagrm", formData)
                .then(
                    function (response) {
                        console.log('Email sent successfully:', response);
                        form.reset();
                    },
                    function (error) {
                        console.log('Failed to send email:', error);
                    }
                );
            return true;
        } else {
            form.reportValidity();
            return false;
        }
    }
}