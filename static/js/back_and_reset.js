const back = document.querySelector("#btn-back");
const justBack = document.querySelector("#btn-just-back");
const previous = document.querySelector("#btn-previous");
const popupReturn = document.querySelector(".popup-return");
overlay = document.querySelector("#overlay");
const saveCloseReturn = document.querySelector(".save-close-return");
const saveSaveReturn = document.querySelector(".save-save-return");

function backAndReset() {
  fetch(`/reset_counter`, { method: "POST" }).then(() => {
    history.back(-1);
  });
}

function justGoBack() {
  history.back(-1);
}

if (back) {
  back.addEventListener("click", () => {
    popupReturn.classList.toggle("popup-return-toggled");
    overlay.classList.toggle("overlay-toggled");
  });

  saveCloseReturn.addEventListener("click", () => {
    popupReturn.classList.remove("popup-return-toggled");
    overlay.classList.remove("overlay-toggled");
  });

  previous.addEventListener("click", () => {
    popupReturn.classList.remove("popup-save-toggled");
    overlay.classList.remove("overlay-toggled");
    backAndReset();
  });
} else if (justBack){
  justBack.addEventListener("click", () => {
    justGoBack();
  });
}
