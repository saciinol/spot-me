const btnForgot = document.querySelector("#btn-forgot");
centerer = document.querySelector(".centerer");
overlay = document.getElementById("overlay");

const popupSent = document.querySelector(".popup-sent");
const SentOk = document.querySelector(".sent-ok");

const popupFailedLink = document.querySelector(".popup-failedLink");
const FailedLinkOk = document.querySelector(".failedLink-ok");

const popupIncomplete = document.querySelector(".popup-incomplete");
const incompleteOk = document.querySelector(".incomplete-ok");

const popupNotFound = document.querySelector(".popup-notfound");
const notFoundOk = document.querySelector(".notfound-ok");

SentOk.addEventListener("click", () => {
  popupSent.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

FailedLinkOk.addEventListener("click", () => {
  popupFailedLink.classList.remove("popup-toggled");
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

btnForgot.addEventListener("click", (e) => {
  e.preventDefault();

  const email = document.querySelector("#email").value;

  if (email === "") {
    popupIncomplete.classList.add("popup-toggled");
    overlay.classList.add("overlay-toggled");
    centerer.classList.add("centerer-toggled");
  } else {
    fetch("/forgot-password/send-link", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email: email }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.response === 404) {
          popupNotFound.classList.add("popup-toggled");
          overlay.classList.add("overlay-toggled");
          centerer.classList.add("centerer-toggled");
        } else if (data.response === 200) {
          popupSent.classList.add("popup-toggled");
          overlay.classList.add("overlay-toggled");
          centerer.classList.add("centerer-toggled");
        } else {
          popupFailedLink.classList.add("popup-toggled");
          overlay.classList.add("overlay-toggled");
          centerer.classList.add("centerer-toggled");
        }
      });
  }
});