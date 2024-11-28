document.addEventListener('DOMContentLoaded', () => {
    // Get the date and time input elements
    const dateInput = document.getElementById('date');
    const timeInput = document.getElementById('time');

    // If the date or time input is not found, log an error and stop
    if (!dateInput || !timeInput) {
        console.error("Date or time input element not found!");
        return;
    }

    // Get the current date and time
    const now = new Date();
    const today = now.toISOString().split('T')[0]; // Get today's date in YYYY-MM-DD format
    const currentHours = String(now.getHours()).padStart(2, '0'); // Current hours as a 2-digit string
    const currentMinutes = String(now.getMinutes()).padStart(2, '0'); // Current minutes as a 2-digit string
    const currentTime = `${currentHours}:${currentMinutes}`; // Current time in HH:mm format

    // Set the minimum allowed date to today
    dateInput.setAttribute('min', today); // Prevent past dates in the date picker

    // Function to handle disabling past times based on selected date
    function disablePastTimes() {
        const selectedDate = dateInput.value; // Get the selected date
        const options = timeInput.options; // Get the time options in the dropdown

        // Iterate over all time options to disable past times
        for (let i = 0; i < options.length; i++) {
            const option = options[i]; // Get each option in the dropdown
            const optionTime = option.value; // The time value of this option

            // If the selected date is today, disable past times
            if (selectedDate === today) {
                option.disabled = optionTime < currentTime; // Disable past times
            } else {
                // If the selected date is in the future, enable all time options
                option.disabled = false;
            }
        }
    }

    // Listen for changes on the date input to update available times
    dateInput.addEventListener('input', disablePastTimes); // Update time options when date changes

    // Run the function once when the page loads to handle the initial state
    disablePastTimes();
});