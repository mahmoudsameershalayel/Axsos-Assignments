function loggedIn(elem){
    elem.innerText = "Logout";
}
function removeElem(elem){
    elem.remove();  
}

function ninjaLiked(elem){
    elem.innerText = parseInt(elem.innerText) + 1 + " likes";
    alert("Ninja was liked");
}