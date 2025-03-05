window.addEventListener("load", () =>{
    // page loader
    document.querySelector(".js-page-loader").classList.add("fade-out");

    setTimeout(() =>{
        document.querySelector(".js-page-loader").style.display = "none";
    }, 600);
})



// testimonial slider
function testimonialSlider() {
    const carousel = document.getElementById('carouselOne');
    if (carousel) {
        carousel.addEventListener('slide.bs.carousel', function () {
            const activeItem = this.querySelector('.carousel-item.active');
            if (activeItem) {
                const newImageSrc = activeItem.getAttribute('data-js-testimonial-img');
                const testimonialImg = document.querySelector('.js-testimonial-img');
                if (testimonialImg && newImageSrc) {
                    testimonialImg.src = newImageSrc;
                }
            }
        });
    }
}


testimonialSlider();

// course preview video

function coursePreviewVideo() {
    const coursePreviewModal = document.querySelector('.js-course-preview-modal')
    if (coursePreviewModal) { //if it exists
        coursePreviewModal.addEventListener("shown.bs.modal", function () {
            this.querySelector(".js-course-preview-video").play();
            this.querySelector(".js-course-preview-video").currentTime = 0;
        });

        coursePreviewModal.addEventListener("hide.bs.modal", function () {
            this.querySelector(".js-course-preview-video").pause();
        });
    }
}

coursePreviewVideo();

// header menu
function headerMenu() {
    const menu = document.querySelector(".js-header-menu"),

    backdrop = document.querySelector(".js-header-backdrop"),
    menuCollapseBreakpoint = 991;

    function toggleMenu(){
        menu.classList.toggle("open")
        backdrop.classList.toggle("active")
        document.body.classList.toggle("overflow-hidden")
    }

    document.querySelectorAll(".js-header-menu-toggler").forEach((item) => {
        item.addEventListener("click", toggleMenu);
    })
    // close the menu by clicking outside of the box
    backdrop.addEventListener("click", toggleMenu);

    function collapse(){
        menu.querySelector(".active .js-sub-menu").removeAttribute("style");
        menu.querySelector(".active").classList.remove("active");
    }

    menu.addEventListener("click", (event) => {
        const {target} = event;
        

        if (target.classList.contains("js-toggle-sub-menu") && window.innerWidth <= menuCollapseBreakpoint) {
            event.preventDefault();

            // if menu item is already expanded, collapse it and exit
            if (target.parentElement.classList.contains("active")) {
                collapse();
                return;
            }

            // if not already expanded ... run below

            // collapse the other menu items if exists
            if (menu.querySelector(".active")) {
                collapse()
            }

            // expand new menu items
            target.parentElement.classList.add("active");
            target.nextElementSibling.style.maxHeight =
            target.nextElementSibling.scrollHeight + "px";
        }
    })
    // when resizing windows
    window.addEventListener("resize", function () {
        if (this.innerWidth > menuCollapseBreakpoint && menu.classList.contains("open")) {
            toggleMenu()
        }
        if (this.innerWidth > menuCollapseBreakpoint && menu.querySelector(".active")) {
            collapse()
        }
    })
}


headerMenu();


// style switcher

function styleSwitcherToggler() {
    const styleSwitcher = document.querySelector(".js-style-switcher"),
    styleSwitcherToggler = document.querySelector(".js-style-switcher-toggler");

    styleSwitcherToggler.addEventListener('click', function () {
        styleSwitcher.classList.toggle("open");
        this.querySelector("i").classList.toggle("fa-times")
        this.querySelector("i").classList.toggle("fa-cog")
    });
}


styleSwitcherToggler();


// theme colors
// to change the theme of the webpage
function themeColors() {
    const colorStyle = document.querySelector(".js-color-style"),
    themeColorContainer = document.querySelector(".js-theme-colors")

    themeColorContainer.addEventListener("click", ({target}) => {
        if (target.classList.contains("js-theme-color-item")) {
            localStorage.setItem("color", target.getAttribute("data-js-theme-color"));
            setColor()
        }
    })

    function setColor(){
        let path = colorStyle.getAttribute("href").split("/")
        path = path.slice(0, path.length-1)
        colorStyle.setAttribute("href", path.join("/") + "/" + localStorage.getItem("color") + ".css")

        if (document.querySelector(".js-theme-color-item.active")) {
            document.querySelector(".js-theme-color-item.active").classList.remove("active")
        }
        document.querySelector("[data-js-theme-color=" + localStorage.getItem("color") + "]").classList.add("active")
    }
    if (localStorage.getItem("color") !== null) {
        setColor()
    }else{
        const defaultColor = colorStyle.getAttribute("href").split("/").pop().split(".").shift();
        document.querySelector("[data-js-theme-color=" + defaultColor + "]").classList.add("active")
        console.log(defaultColor)
    }
}


themeColors();


// theme light and dark mode
function themeLightDarkMode(){
    const darkModeCheckBox = document.querySelector(".js-dark-mode")

    darkModeCheckBox.addEventListener("click", function(){
        if (this.checked) {
            localStorage.setItem("theme-dark", "true")
        }else{
            localStorage.setItem("theme-dark", "false")
        }
        themeMode();
    })
    function themeMode(){
        if (localStorage.getItem("theme-dark") === "false") {
            document.body.classList.remove("t-dark")
        }else{
            document.body.classList.add("t-dark")
        }
    }
    if (localStorage.getItem("theme-dark") !== null) {
        themeMode();
    }
    if (document.body.classList.contains("t-dark")) {
        darkModeCheckBox.checked = true;
    }
}

themeLightDarkMode();


// theme glass effect

function themeGlassEffect(){
    const glassEffectCheckbok = document.querySelector(".js-glass-effect"),
    glassStyle = document.querySelector(".js-glass-style")

    glassEffectCheckbok.addEventListener("click", function (){
        if (this.checked) {
            localStorage.setItem("glass-effect", "true");
        }else{
            localStorage.setItem("glass-effect", "false");
        }
        glass();
    })
    function glass(){
        if (localStorage.getItem("glass-effect") === "true") {
            glassStyle.removeAttribute("disabled");
        }else{
            glassStyle.disabled =true;
        }
    }
    if (localStorage.getItem("glass-effect") !== null) {
        glass();
    }
    if (!glassStyle.hasAttribute("disabled")) {
        glassEffectCheckbok.checked = true;
    }
}

themeGlassEffect();


