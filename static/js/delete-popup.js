const deleteBtns = document.querySelectorAll(".btn-delete");
const popupDeletes = document.querySelectorAll(".popup-delete");
overlay = document.querySelector("#overlay");
const closeBtns = document.querySelectorAll(".delete-close");

deleteBtns.forEach((btn, i) => {
  btn.addEventListener("click", () => {
    popupDeletes[i].classList.toggle("popup-delete-toggled");
    overlay.classList.toggle("overlay-toggled");
  });
});

closeBtns.forEach((btn, i) => {
  btn.addEventListener("click", () => {
    popupDeletes[i].classList.remove("popup-delete-toggled");
    overlay.classList.remove("overlay-toggled");
  });
});
