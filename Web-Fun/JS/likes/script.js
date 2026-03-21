var likes = [0 ,0 ,0]
function like(index){
    likes[index]++;
    document.getElementById("likes-"+index).innerText = likes[index] + " Like(s)";
}