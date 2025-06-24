document.addEventListener("DOMContentLoaded", function () {
    let alertBox = document.querySelector(".custom-alert");
    if (alertBox) {
        animateAlert(alertBox);
    }
});

function animateAlert(alert) {
    setTimeout(() => {
        alert.style.transition = "transform 1s ease-out, opacity 0.5s ease-in";
        alert.style.transform = "translateX(-100%)"; // Move left
        alert.style.opacity = "0";

        setTimeout(() => {
            alert.remove();
        }, 500); // Remove after fade out
    }, 4000); // Start animation after 4 seconds
}
