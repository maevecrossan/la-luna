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

		// Populate the form fields with the current booking details
		bookingName.value = name;
		bookingEmail.value = email;
		bookingPhoneNumber.value = phone_number;
		bookingDate.value = date;
		bookingTime.value = time;
		bookingGuests.value = guests;

		// Fetch booking details from the container (assuming each booking has its own container)
		let name = bookingContainer.querySelector(".booking-name").innerText;
		let email = bookingContainer.querySelector(".booking-email").innerText;
		let phone_number = bookingContainer.querySelector(".booking-phone").innerText;
		let date = bookingContainer.querySelector(".booking-date").innerText;
		let time = bookingContainer.querySelector(".booking-time").innerText;
		let guests = bookingContainer.querySelector(".booking-guests").innerText;

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
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let bookingId = e.target.getAttribute("booking_id");
            deleteConfirm.href = `/bookings/delete-booking/${bookingId}/`;
            deleteModal.show(); // Show the modal
        });
    }
});