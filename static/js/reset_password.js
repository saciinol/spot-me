const btnReset = document.querySelector("#btn-reset");
centerer = document.querySelector(".centerer");
overlay = document.getElementById("overlay");

const popupForgot = document.querySelector(".popup-forgot");
const forgotOk = document.querySelector(".forgot-ok");

const popupIncomplete = document.querySelector(".popup-incomplete");
const incompleteOk = document.querySelector(".incomplete-ok");

const popupErrorReset = document.querySelector(".popup-errorReset");
const ErrorResetOk = document.querySelector(".errorReset-ok");

const popupShort = document.querySelector(".popup-short");
const shortOk = document.querySelector(".short-ok");

const popupNotFound = document.querySelector(".popup-notfound");
const notFoundOk = document.querySelector(".notfound-ok");


forgotOk.addEventListener("click", () => {
  popupForgot.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

incompleteOk.addEventListener("click", () => {
  popupIncomplete.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

ErrorResetOk.addEventListener("click", () => {
  popupErrorReset.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

shortOk.addEventListener("click", () => {
  popupShort.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

notFoundOk.addEventListener("click", () => {
  popupNotFound.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

btnReset.addEventListener("click", (e) => {
  e.preventDefault();

  const password = document.querySelector("#password").value;
  const confirmPassword = document.querySelector("#confirm-password").value;

  if (!password || !confirmPassword) {
    popupIncomplete.classList.add("popup-toggled");
    overlay.classList.add("overlay-toggled");
    centerer.classList.add("centerer-toggled");
  } else if (password !== confirmPassword) {
    popupForgot.classList.add("popup-toggled");
    overlay.classList.add("overlay-toggled");
    centerer.classList.add("centerer-toggled");
  } else {
    fetch(window.location.href, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        password: password,
        confirmPassword: confirmPassword,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.response === 200) {
          window.location.href = "/login";
        } else if (data.response === 401) {
          popupShort.classList.toggle("popup-toggled");
          overlay.classList.toggle("overlay-toggled");
          centerer.classList.toggle("centerer-toggled");
        } else if (data.response === 400) {
          popupForgot.classList.add("popup-toggled");
          overlay.classList.add("overlay-toggled");
          centerer.classList.add("centerer-toggled");
        } else if (data.response === 404) {
          popupNotFound.classList.add("popup-toggled");
          overlay.classList.add("overlay-toggled");
          centerer.classList.add("centerer-toggled");
        } else {
          popupErrorReset.classList.add("popup-toggled");
          overlay.classList.add("overlay-toggled");
          centerer.classList.add("centerer-toggled");
        }
      });
  }
});
