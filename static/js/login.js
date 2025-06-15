const btnLogin = document.querySelector("#btn-login");
centerer = document.querySelector(".centerer");
overlay = document.getElementById("overlay");

const popupLogin = document.querySelector(".popup-login");
const loginOk = document.querySelector(".login-ok");

const popupIncomplete = document.querySelector(".popup-incomplete");
const incompleteOk = document.querySelector(".incomplete-ok");

const popupNotFound = document.querySelector(".popup-notfound");
const notFoundOk = document.querySelector(".notfound-ok");

loginOk.addEventListener("click", () => {
  popupLogin.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

incompleteOk.addEventListener("click", () => {
  popupIncomplete.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

notFoundOk.addEventListener("click", () => {
  popupNotFound.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

btnLogin.addEventListener("click", (e) => {
  e.preventDefault();

  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;

  if (username === "" || password === "") {
    popupIncomplete.classList.toggle("popup-toggled");
    overlay.classList.toggle("overlay-toggled");
    centerer.classList.toggle("centerer-toggled");
  } else {
    fetch("/login/loging", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        password: password,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.response == 404) {
          popupNotFound.classList.toggle("popup-toggled");
          overlay.classList.toggle("overlay-toggled");
          centerer.classList.toggle("centerer-toggled");
        } else if (data.response == 400) {
          popupLogin.classList.toggle("popup-toggled");
          overlay.classList.toggle("overlay-toggled");
          centerer.classList.toggle("centerer-toggled");
        } else if (data.response == 200) {
          window.location.href = "/index";
        }
      });
  }
});
