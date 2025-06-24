//  navbar scroll  
 window.addEventListener("scroll", function () {
    const emailSection = document.getElementById("email-section");
    const navbarRow = document.querySelector("#navbar-row");

    // Check if the email section is scrolled out of view
    if (window.scrollY > emailSection.offsetHeight) {
      navbarRow.style.position = "sticky";
      navbarRow.style.top = "0";
      // navbarRow.style.width = "100%";
      navbarRow.style.zIndex = "1000";
    } else {
      navbarRow.style.position = "static";
    }
  });

  
  function toggleDropdown(event) {
    event.preventDefault();
    let btn = event.target.closest(".nav-item").querySelector(".btn");
    let dropdown = event.target.closest(".nav-item").querySelector(".dropdown-content");

    if (dropdown.classList.contains("show")) {
        dropdown.classList.remove("show");
        btn.textContent = "+"; 
        setTimeout(() => {
            dropdown.style.display = "none";
        }, 300);
    } else {
        dropdown.style.display = "block";
        setTimeout(() => {
            dropdown.classList.add("show");
            btn.textContent = "-";
        }, 10);
    }
}


