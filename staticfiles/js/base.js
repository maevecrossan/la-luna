// Contains function linked solely to base.html

/* Toggle between showing and hiding the mobile menu links 
when the user clicks on the hamburger menu / bar icon */
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


/* Dropdown nav links: toggle between adding and removing the 
"responsive" class to topnav when the user clicks on the icon */
document.querySelectorAll('.dropbtn').forEach(button => {
    button.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default link behavior
        const dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === 'block') {
            dropdownContent.style.display = 'none';
        } else {
            dropdownContent.style.display = 'block';
        }
    });
});