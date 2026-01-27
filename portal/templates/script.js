function showSection(sectionId) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.classList.remove('active');
    });

    document.getElementById(sectionId).classList.add('active');
}
function toggleNotifications() {
    const dropdown = document.getElementById("notif-dropdown");
    dropdown.style.display =
        dropdown.style.display === "block" ? "none" : "block";
}

/* Close when clicking outside */
document.addEventListener("click", function (e) {
    const notif = document.querySelector(".notification");
    if (!notif.contains(e.target)) {
        document.getElementById("notif-dropdown").style.display = "none";
    }
});


