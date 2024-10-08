// Checks guest number input. Sends alert if 9 or more guests are being entered.
function checkGuests(input) {
    if (input.value > 8) {
      alert('For reservations of more than 8 guests, please call us directly to make arrangements.');
      input.value = 8; // Reset to maximum allowed value
    }
  }