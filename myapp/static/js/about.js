
// animated number field 
function animateCounters() {
    const counters = document.querySelectorAll('.stat');
    const speed = 200;

    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const increment = target / speed;

            if (count < target) {
                counter.innerText = Math.ceil(count + increment);
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = target;
            }
        };

        updateCount();
    });
}

function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-fill');
    
    progressBars.forEach(bar => {
        const percentage = bar.getAttribute('data-percentage');
        bar.style.width = percentage + '%';
    });
}

// Combined visibility check
function checkVisibility() {
    const statsSection = document.querySelector('.stats-container');
    const skillsSection = document.querySelector('.skills-section');
    const screenHeight = window.innerHeight;

    // Check if the stats section is visible
    if (statsSection.getBoundingClientRect().top < screenHeight) {
        animateCounters();
    }

    // Check if the skills section is visible
    if (skillsSection.getBoundingClientRect().top < screenHeight) {
        animateProgressBars();
    }

    // Remove scroll listener after animations trigger
    if (statsSection.getBoundingClientRect().top < screenHeight && skillsSection.getBoundingClientRect().top < screenHeight) {
        window.removeEventListener('scroll', checkVisibility);
    }
}

// Attach event listener
window.addEventListener('scroll', checkVisibility);
