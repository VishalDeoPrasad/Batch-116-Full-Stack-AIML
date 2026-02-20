let button = document.getElementById("btn")
let image = document.getElementById("image")

function hideImage(){
    image.style.display = "none";
}

button.addEventListener("click", hideImage);