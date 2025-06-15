const btnCreate = document.querySelector("#btn-create");
centerer = document.querySelector(".centerer");
overlay = document.getElementById("overlay");

const popupCreate = document.querySelector(".popup-create");
const createOk = document.querySelector(".create-ok");

const popupIncomplete = document.querySelector(".popup-incomplete");
const incompleteOk = document.querySelector(".incomplete-ok");

const popupFound = document.querySelector(".popup-found");
const foundOk = document.querySelector(".found-ok");

const popupShort = document.querySelector(".popup-short");
const shortOk = document.querySelector(".short-ok");

createOk.addEventListener("click", () => {
  popupCreate.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

incompleteOk.addEventListener("click", () => {
  popupIncomplete.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

foundOk.addEventListener("click", () => {
  popupFound.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

shortOk.addEventListener("click", () => {
  popupShort.classList.remove("popup-toggled");
  overlay.classList.remove("overlay-toggled");
  centerer.classList.remove("centerer-toggled");
});

btnCreate.addEventListener("click", (e) => {
  e.preventDefault();

  const email = document.querySelector("#email").value;
  const username = document.querySelector("#username").value;
  const password = document.querySelector("#password").value;
  const confirmPassword = document.querySelector("#confirm-password").value;

  if (
    email === "" ||
    username === "" ||
    password === "" ||
    confirmPassword === ""
  ) {
    popupIncomplete.classList.toggle("popup-toggled");
    overlay.classList.toggle("overlay-toggled");
    centerer.classList.toggle("centerer-toggled");
  } else {
    fetch("/create-account/creating", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        username: username,
        password: password,
        confirmPassword: confirmPassword,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.response == 405) {
          popupFound.classList.toggle("popup-toggled");
          overlay.classList.toggle("overlay-toggled");
          centerer.classList.toggle("centerer-toggled");
        } else if (data.response == 400) {
          popupCreate.classList.toggle("popup-toggled");
          overlay.classList.toggle("overlay-toggled");
          centerer.classList.toggle("centerer-toggled");
        } else if (data.response == 404) {
          popupShort.classList.toggle("popup-toggled");
          overlay.classList.toggle("overlay-toggled");
          centerer.classList.toggle("centerer-toggled");
        } else if (data.response == 200) {
          window.location.href = "/login";
        }
      });
  }
});
