/**
 * Handles CRUD functionality for users.
 */

const editButtons = document.getElementsByClassName("btn-edit"); // Edit buttons for each booking
const bookingName = document.getElementById("id_name"); // Booking name input field
const bookingEmail = document.getElementById("id_email"); // Booking email input field
const bookingPhoneNumber = document.getElementById("id_phone_number"); // Booking phone number input field
const bookingDate = document.getElementById("id_date"); // Booking date input field
const bookingTime = document.getElementById("id_time"); // Booking time input field
const bookingGuests = document.getElementById("id_guests"); // Booking guests input field
const bookingForm = document.getElementById("bookingForm"); // The form used to edit bookings
const submitButton = document.getElementById("submitButton"); // The submit button in the form


/**
 * Allows users to EDIT their booking with the edit button.
 */

for (let button of editButtons) {
	button.addEventListener("click", (e) => {
		let bookingId = e.target.getAttribute("booking_id"); // Get the booking's ID from the button
		let bookingContainer = document.getElementById(`booking${bookingId}`); // Container for the booking data

		// Fetch booking details from the container (assuming each booking has its own container)
		let name = bookingContainer.querySelector(".booking-name").innerText;
		let email = bookingContainer.querySelector(".booking-email").innerText;
		let phone_number = bookingContainer.querySelector(".booking-phone").innerText;
		let date = bookingContainer.querySelector(".booking-date").innerText;
		let time = bookingContainer.querySelector(".booking-time").innerText;
		let guests = bookingContainer.querySelector(".booking-guests").innerText;

		// Populate the form fields with the current booking details
		bookingName.value = name;
		bookingEmail.value = email;
		bookingPhoneNumber.value = phone_number;
		bookingDate.value = date;
		bookingTime.value = time;
		bookingGuests.value = guests;

		// Change submit button text to "Update" to reflect that this is an update operation
		submitButton.innerText = "Update";

		// Update the form's action attribute to target the edit booking URL
		bookingForm.setAttribute("action", `edit_booking/${bookingId}`);
	});
}


/**
 * Allows a user to delete a booking.
 * Displays warning modal before deletion.
 */
document.addEventListener("DOMContentLoaded", () => {
    const deleteModalElement = document.getElementById("deleteModal");
    const deleteButtons = document.getElementsByClassName("btn-delete");

    if (!deleteModalElement || !deleteButtons.length) return; // Exit early if the modal or buttons are not present

    const deleteModal = new bootstrap.Modal(deleteModalElement); // Initialize Bootstrap Modal

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            const bookingId = e.target.getAttribute("data-booking-id");

            if (bookingId) {
                const deleteConfirm = document.getElementById("deleteConfirm");
                if (deleteConfirm) {
                    deleteConfirm.setAttribute("href", `/bookings/delete-booking/${bookingId}/`);
                }
                deleteModal.show();
            }
        });
    }
});


/**
 * Prevents users from booking in the past (time slot)
 */
// Check if the #time input element exists before adding the event listener
const timeField = document.getElementById('time');

if (timeField) {
    timeField.addEventListener('focus', function () {
        const dateField = document.getElementById('date');
        const selectedDate = dateField.value;
        const today = new Date().toISOString().split('T')[0]; // Get today's date
        const currentTime = new Date();

        // If the selected date is today, disable past time slots
        if (selectedDate === today) {
            const currentHours = currentTime.getHours();
            const currentMinutes = currentTime.getMinutes();

            // Disable past time slots
            [...this.options].forEach(option => {
                const [hours, minutes] = option.value.split(':').map(Number);
                if (hours < currentHours || (hours === currentHours && minutes <= currentMinutes)) {
                    option.disabled = true; // Disable past times
                } else {
                    option.disabled = false; // Enable future times
                }
            });
        } else {
            // Enable all options if the date is not today
            [...this.options].forEach(option => (option.disabled = false));
        }
    });
}


// Form submit validation
// Check if the booking form exists before attaching the event listener
if (bookingForm) {
    bookingForm.addEventListener('submit', function (event) {
        const timeField = document.getElementById('time');
        const dateField = document.getElementById('date');
        const selectedDate = dateField.value;
        const today = new Date().toISOString().split('T')[0]; // Get today's date
        const currentTime = new Date();

        // Check if the selected date is today and the selected time is in the past
        if (selectedDate === today) {
            const selectedTime = timeField.value;
            if (selectedTime) {
                const [selectedHours, selectedMinutes] = selectedTime.split(':').map(Number);
                if (selectedHours < currentTime.getHours() || (selectedHours === currentTime.getHours() && selectedMinutes <= currentTime.getMinutes())) {
                    // Show error message
                    const errorMessage = document.createElement('div');
                    errorMessage.classList.add('formbold-error-message');
                    errorMessage.innerText = 'The selected time is in the past. Please choose a valid future time.';
                    
                    // If an error message already exists, remove it
                    const existingError = timeField.parentNode.querySelector('.formbold-error-message');
                    if (existingError) {
                        existingError.remove();
                    }
                    
                    timeField.parentNode.appendChild(errorMessage);

                    // Prevent form submission
                    event.preventDefault();
                }
            }
        }
    });
}
