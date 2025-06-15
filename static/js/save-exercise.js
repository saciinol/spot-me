const btnSave = document.querySelector(".btn-save");
const popupSave = document.querySelector(".popup-save");
overlay = document.querySelector("#overlay");
const saveClose = document.querySelector(".save-close");
const saveSave = document.querySelector(".save-save");

btnSave.addEventListener("click", () => {
  popupSave.classList.toggle("popup-save-toggled");
  overlay.classList.toggle("overlay-toggled");
});

saveClose.addEventListener("click", () => {
  popupSave.classList.remove("popup-save-toggled");
  overlay.classList.remove("overlay-toggled");
});

saveSave.addEventListener("click", () => {
  popupSave.classList.remove("popup-save-toggled");
  overlay.classList.remove("overlay-toggled");
});
