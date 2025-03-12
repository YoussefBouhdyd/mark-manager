document.getElementById("log-out").onclick = () => {
let request = new XMLHttpRequest;
request.open("GET","/log-out");
request.send();
request.onreadystatechange = _ => {
    if(request.readyState === 4 && request.status === 200) {
        window.location.href = "/"
    }
}
}