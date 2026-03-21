function changeName(name){
    document.getElementById("card-username").innerText = name;
}

function removeRequest(num){
    var userRequest = document.getElementById("user-requst-"+num);
    var requestsCount = Number(document.getElementById("requests-count").innerText);
    requestsCount--;
    document.getElementById("requests-count").innerText = requestsCount;
    userRequest.remove();
}

function acceptRequest(num){
    removeRequest(num);
    var connectionsCount = Number(document.getElementById("connections-count").innerText);
    connectionsCount++;
    document.getElementById("connections-count").innerText = connectionsCount;
}


