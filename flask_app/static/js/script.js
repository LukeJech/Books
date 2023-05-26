// JavaScript code to show/hide the dropdown menu on hover
const dropdowns = document.querySelectorAll('.dropdown_menu');

dropdowns.forEach(function(authorDropdown) {
    const dropdownMenu = authorDropdown.querySelector('ul');

    authorDropdown.addEventListener('mouseenter', function() {
        dropdownMenu.classList.remove('hidden');
    });

    authorDropdown.addEventListener('mouseleave', function() {
        dropdownMenu.classList.add('hidden');
    });
});