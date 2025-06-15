const btnChange = document.querySelector("#btn-change");
centerer = document.querySelector(".centerer");
overlay = document.getElementById("overlay");

const popupChangePW = document.querySelector(".popup-changePW");
const changePWClose = document.querySelector(".changePW-close");
const changePWYes = document.querySelector(".changePW-yes");

const popupWrong = document.querySelector(".popup-wrong");
const wrongOk = document.querySelector(".wrong-ok");

const popupWrongPassword = document.querySelector(".popup-wrongpassword");
const wrongPasswordOk = document.querySelector(".wrongpassword-ok");

const popupIncomplete = document.querySelector(".popup-incomplete");
const incompleteOk = document.querySelector(".incomplete-ok");

const popupNotFound = document.querySelector(".popup-notfound");
const notFoundOk = document.querySelector(".notfound-ok");

const popupNotYours = document.querySelector(".popup-notyours");
const notYoursOk = document.querySelector(".notyours-ok");

const popupShort = document.querySelector(".popup-short");
const shortOk = document.querySelector(".short-ok");

btnChange.addEventListener("click", (e) => {
  e.preventDefault();

  const email = document.querySelector("#email").value;
  const username = document.querySelector("#username").value;
  const oldPassword = document.querySelector("#old-password").value;
  const newPassword = document.querySelector("#new-password").value;

  if (
    email === "" ||
    username === "" ||
    oldPassword === "" ||
    newPassword === ""
  ) {
    popupIncomplete.classList.toggle("popup-toggled");
  } else {
    popupChangePW.classList.toggle("popup-toggled");
  }

  overlay.classList.toggle("overlay-toggled");
  centerer.classList.toggle("centerer-toggled");
});

wrongOk.addEventListener("click", () => {
  popupWrong.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

wrongPasswordOk.addEventListener("click", () => {
  popupWrongPassword.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

changePWClose.addEventListener("click", () => {
  popupChangePW.classList.remove("popup-toggled");
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

notYoursOk.addEventListener("click", () => {
  popupNotYours.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

shortOk.addEventListener("click", () => {
  popupShort.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

changePWYes.addEventListener("click", () => {
  popupChangePW.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");

  const email = document.querySelector("#email").value;
  const username = document.querySelector("#username").value;
  const oldPassword = document.querySelector("#old-password").value;
  const newPassword = document.querySelector("#new-password").value;

  fetch("/change-password/changing", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: email,
      username: username,
      oldPassword: oldPassword,
      newPassword: newPassword,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.response == 405) {
        popupWrongPassword.classList.toggle("popup-toggled");
        overlay.classList.toggle("overlay-toggled");
        centerer.classList.toggle("centerer-toggled");
      } else if (data.response == 404) {
        popupNotFound.classList.toggle("popup-toggled");
        overlay.classList.toggle("overlay-toggled");
        centerer.classList.toggle("centerer-toggled");
      } else if (data.response == 403) {
        popupWrong.classList.toggle("popup-toggled");
        overlay.classList.toggle("overlay-toggled");
        centerer.classList.toggle("centerer-toggled");
      } else if (data.response == 400) {
        popupShort.classList.toggle("popup-toggled");
        overlay.classList.toggle("overlay-toggled");
        centerer.classList.toggle("centerer-toggled");
      } else if (data.response == 401) {
        popupNotYours.classList.toggle("popup-toggled");
        overlay.classList.toggle("overlay-toggled");
        centerer.classList.toggle("centerer-toggled");
      } else if (data.response == 200) {
        window.location.href = "/logout";
      }
    });
});
