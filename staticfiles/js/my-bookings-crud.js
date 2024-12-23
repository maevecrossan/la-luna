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
    if (deleteModalElement) {
        const deleteModal = new bootstrap.Modal(deleteModalElement); /* global bootstrap */
        const deleteButtons = document.getElementsByClassName("btn-delete");

        // Iterate over all delete buttons and add event listeners
        for (let button of deleteButtons) {
            button.addEventListener("click", (e) => {
                // Get the booking ID from the button's data-booking-id attribute
                const bookingId = e.target.getAttribute("data-booking-id");
                console.log("Booking ID to delete:", bookingId); // Debugging line

                // Check if the booking ID is found
                if (bookingId) {
                    // Get the delete confirmation link
                    const deleteConfirm = document.getElementById("deleteConfirm");

                    if (deleteConfirm) {
                        // Set the correct href for the confirmation link
                        deleteConfirm.setAttribute("href", `/bookings/delete-booking/${bookingId}/`);
                    }

                    // Show the modal
                    deleteModal.show();
                } else {
                    console.error("Booking ID not found!");
                }
            });
        }
    }
});

// Prevents users from booking in the past (time slot)
document.getElementById('id_time').addEventListener('focus', function () {
    const dateField = document.getElementById('id_date');
    const selectedDate = dateField.value;
    const today = new Date().toISOString().split('T')[0]; // Get today's date
    const currentTime = new Date();

    // When the date is selected, update the time options accordingly
    updateTimeOptions(selectedDate, currentTime, today);
});

// Prevents users from booking in the past (time slot)
document.getElementById('id_time').addEventListener('focus', function () {
    const dateField = document.getElementById('id_date');
    const selectedDate = dateField.value;
    const today = new Date().toISOString().split('T')[0]; // Get today's date
    const currentTime = new Date();

    // When the date is selected, update the time options accordingly
    updateTimeOptions(selectedDate, currentTime, today);
});

// This function is called whenever the date or time changes
function updateTimeOptions(selectedDate, currentTime, today) {
    const timeField = document.getElementById('id_time');
    const selectedTime = timeField.value;  // Store the current time selection
    const timeOptions = [...timeField.options];
    
    let isValidTime = false; // Flag to track if the selected time is still valid

    // If the selected date is today, disable past time slots
    if (selectedDate === today) {
        const currentHours = currentTime.getHours();
        const currentMinutes = currentTime.getMinutes();

        // Disable past time slots and preserve the current selection if possible
        timeOptions.forEach(option => {
            const [hours, minutes] = option.value.split(':').map(Number);
            if (hours < currentHours || (hours === currentHours && minutes <= currentMinutes)) {
                option.disabled = true; // Disable past times
            } else {
                option.disabled = false; // Enable future times
            }

            // Check if the currently selected time is still valid
            if (option.value === selectedTime && !option.disabled) {
                isValidTime = true; // Mark as valid if the selected time is still enabled
            }
        });
    } else {
        // Enable all options if the selected date is not today
        timeOptions.forEach(option => {
            option.disabled = false; // Enable all time options
        });

        // If the time field was previously reset due to invalid time, check if it's still valid
        isValidTime = timeOptions.some(option => option.value === selectedTime);
    }

    // Reset the time field if the selected time is no longer valid
    if (!isValidTime) {
        // Delay the reset to ensure the option list is updated
        setTimeout(() => {
            timeField.value = '';  // Reset time if the previously selected time is no longer valid
        }, 100); // Slight delay to ensure DOM updates first
    }
}

// Add event listener to the date field to update time options when the date is changed
document.getElementById('id_date').addEventListener('change', function () {
    const selectedDate = this.value;
    const today = new Date().toISOString().split('T')[0]; // Get today's date
    const currentTime = new Date();

    // Update time options when the date is changed
    updateTimeOptions(selectedDate, currentTime, today);
});