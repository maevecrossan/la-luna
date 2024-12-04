// Contains function linked solely to base.html

/* Toggle between showing and hiding the mobile menu links when the user clicks on the hamburger menu / bar icon */
document.addEventListener("DOMContentLoaded", function() {
    // Function to toggle mobile menu
    function displayMobileMenu() {
        var nav = document.getElementById("mobile-navigation");
        if (nav) {
            nav.classList.toggle("active"); // Toggle the active class
        } else {
            console.error("Navigation element not found!");
        }
    }

    // Attach event listener to the hamburger icon
    document.getElementById("burger-icon").addEventListener("click", displayMobileMenu);
});
