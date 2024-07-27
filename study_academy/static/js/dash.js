window.addEventListener("load", () =>{
    // page loader
    document.querySelector(".js-page-loader").classList.add("fade-out");

    setTimeout(() =>{
        document.querySelector(".js-page-loader").style.display = "none";
    }, 600);
})






// add hovered class to selected list item

let list = document.querySelectorAll(".navigation li");

function activeLink(){
    list.forEach(item => {
        item.classList.remove("hovered");
    });
    this.classList.add("hovered");
}

list.forEach(item => item.addEventListener("mouseover", activeLink));


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

// function themeGlassEffect(){
//     const glassEffectCheckbok = document.querySelector(".js-glass-effect"),
//     glassStyle = document.querySelector(".js-glass-style")

//     glassEffectCheckbok.addEventListener("click", function (){
//         if (this.checked) {
//             localStorage.setItem("glass-effect", "true");
//         }else{
//             localStorage.setItem("glass-effect", "false");
//         }
//         glass();
//     })
//     function glass(){
//         if (localStorage.getItem("glass-effect") === "true") {
//             glassStyle.removeAttribute("disabled");
//         }else{
//             glassStyle.disabled =true;
//         }
//     }
//     if (localStorage.getItem("glass-effect") !== null) {
//         glass();
//     }
//     if (!glassStyle.hasAttribute("disabled")) {
//         glassEffectCheckbok.checked = true;
//     }
// }

// themeGlassEffect();


// menu toggle

let toggle = document.querySelector(".toggle")
let nav = document.querySelector(".navigation")
let main = document.querySelector(".main")

toggle.onclick = function(){
    nav.classList.toggle("active")
    main.classList.toggle("active")
    
}

document.addEventListener('DOMContentLoaded', (event) => {
    const videoThumbnails = document.querySelectorAll('.video-thumbnail');
    const modal = document.getElementById('videoModal');
    const modalVideo = document.getElementById('modalVideo');
    const span = document.getElementsByClassName('close')[0];

    videoThumbnails.forEach(thumbnail => {
        thumbnail.onclick = function() {
            const videoUrl = this.getAttribute('data-video-url');
            modal.style.display = 'block';
            modalVideo.src = videoUrl;
            modalVideo.load();
            modalVideo.play();
        }
    });

    span.onclick = function() {
        modal.style.display = 'none';
        modalVideo.pause();
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
            modalVideo.pause();
        }
    }
});