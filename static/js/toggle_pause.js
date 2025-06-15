document.querySelector("#btn-pause").addEventListener("click", () => {
  togglePause();
});

document.querySelector("#btn-tutorial").addEventListener("click", () => {
  toggleTutorial();
});

document.querySelector(".btn-save").addEventListener("click", () => {
  toggleTutorial();
});

function togglePause() {
  fetch("/toggle_pause", {
    method: "POST",
  }).then((_) => {
    const icon = document.getElementById("btn-pause").firstElementChild;
    const btn = document.getElementById("btn-pause");

    if (icon.classList.contains("fa-play")) {
      btn.innerHTML = '<i class="fas fa-pause"></i>';
    } else if (icon.classList.contains("fa-pause")) {
      btn.innerHTML = '<i class="fas fa-play"></i>';
    }
  });
}

function toggleTutorial() {
  fetch("/toggle_tutorial", {
    method: "POST",
  }).then((_) => {
    const btn = document.getElementById("btn-pause");
    btn.innerHTML = '<i class="fas fa-play"></i>';
  });
}
