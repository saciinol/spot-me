const btnDeleteAcc = document.querySelector("#btn-deleteAcc");
centerer = document.querySelector(".centerer");
overlay = document.getElementById("overlay");

const popupDeleteAcc = document.querySelector(".popup-deleteAcc");
const deleteAccClose = document.querySelector(".deleteAcc-close");
const deleteAccYes = document.querySelector(".deleteAcc-yes");

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

btnDeleteAcc.addEventListener("click", (e) => {
  e.preventDefault();

  const email = document.querySelector("#email").value;
  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;

  if (email === "" || username === "" || password === "") {
    popupIncomplete.classList.toggle("popup-toggled");
  } else {
    popupDeleteAcc.classList.toggle("popup-toggled");
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

deleteAccClose.addEventListener("click", () => {
  popupDeleteAcc.classList.remove("popup-toggled");
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

deleteAccYes.addEventListener("click", () => {
  popupDeleteAcc.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");

  const email = document.querySelector("#email").value;
  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;

  fetch("/delete-account/deleting", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email: email,
      username: username,
      password: password
    })
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
      } else if (data.response == 401) {
        popupNotYours.classList.toggle("popup-toggled");
        overlay.classList.toggle("overlay-toggled");
        centerer.classList.toggle("centerer-toggled");
      } else if (data.response == 200) {
        window.location.href = "/login";
      }
    })
});