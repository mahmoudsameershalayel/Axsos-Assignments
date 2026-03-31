function loadReport(){
    window.alert("We Will Load Report");
}

function removeCookieMessage(){
    document.querySelector('.cookie').remove();
}

function convertTemp() {
    let unit = document.getElementById("unit").value;
    let maxTemps = document.querySelectorAll(".max");
    let minTemps = document.querySelectorAll(".min");

    for (let i = 0; i < maxTemps.length; i++) {
        let max = parseInt(maxTemps[i].innerText);
        let min = parseInt(minTemps[i].innerText);

        if (unit === "F") {
        maxTemps[i].innerText = cToF(max) + "°";
        minTemps[i].innerText = cToF(min) + "°";
        } else {
        maxTemps[i].innerText = fToC(max) + "°";
        minTemps[i].innerText = fToC(min) + "°";
        }
    }
}

function cToF(c) {
  return Math.round((c * 9) / 5 + 32);
}

function fToC(f) {
  return Math.round(((f - 32) * 5) / 9);
}