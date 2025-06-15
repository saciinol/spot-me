const btnLogout = document.querySelector(".btn-logout");
centerer = document.querySelector(".centerer");
overlay = document.getElementById("overlay");

const popupLogout = document.querySelector(".popup-logout");
const logoutClose = document.querySelector(".logout-close");
const logoutYes = document.querySelector(".logout-yes");

btnLogout.addEventListener("click", () => {
  popupLogout.classList.toggle("popup-toggled");
  centerer.classList.toggle("centerer-toggled");
  overlay.style.zIndex = "5";
});

logoutClose.addEventListener("click", () => {
  popupLogout.classList.remove("popup-toggled");
  centerer.classList.remove("centerer-toggled");
  overlay.style.zIndex = "4";
});

logoutYes.addEventListener("click", () => {
  centerer.classList.remove("centerer-toggled");
  overlay.classList.remove("overlay-toggled");
  popupLogout.classList.remove("popup-toggled");
});

