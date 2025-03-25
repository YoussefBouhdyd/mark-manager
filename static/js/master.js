function pushSide() {
    document.querySelector(".insert").classList.toggle("insert-push");
    document.querySelector(".list-students").classList.toggle("list-shrink");
    document.querySelector(".push-btn > i").classList.toggle("btn-rotate");
}

let media = window.matchMedia("(max-width: 991px)");

media.addEventListener("change", (_) => {
    if (media.matches)
        document.querySelector(".push-btn").style.display = "none";
    else document.querySelector(".push-btn").style.display = "block";
});

document.querySelector(".links-btn").onclick = (_) => document.querySelector(".links").classList.toggle("toggle");

document.querySelectorAll(".crud.update").forEach(element => {
    element.onclick = _ => {
        document.querySelector(".update-form").style.display = "block";
        document.querySelector(".container").style.filter = "blur(5px)";
        document.querySelector("input[name='id']").value = element.dataset.id;
        let name = element.parentElement.previousElementSibling.querySelector("div:nth-child(2)").lastChild.textContent.trim()
        let math = element.parentElement.previousElementSibling.querySelector("div:nth-child(3)").lastChild.textContent.trim()
        let info = element.parentElement.previousElementSibling.querySelector("div:nth-child(4)").lastChild.textContent.trim()
        document.querySelector("input[name='name-update']").value = name;
        document.querySelector("input[name='math-update']").value = math;
        document.querySelector("input[name='info-update']").value = info;
    }
});

document.getElementById("out-update").onclick = _ => {
    document.querySelector(".update-form").style.display = 'none';
    document.querySelector(".container").style.filter = "blur(0px)";
}

document.querySelector(".avatar").onclick = _ => {
    document.querySelector(".options").classList.toggle("show-options");
}