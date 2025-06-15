const button = document.querySelector("#btn-tutorial");
const tutorial = document.querySelector(".tutorial");
const centererTutorial = document.querySelector(".centerer-tutorial");
overlay = document.querySelector("#overlay");
const close = document.querySelector(".tutorial-close");

button.addEventListener("click", () => {
  tutorial.classList.toggle("tutorial-toggled");
  centererTutorial.classList.toggle("centerer-tutorial-toggled");
  overlay.classList.toggle("overlay-toggled");
});

close.addEventListener("click", () => {
  tutorial.classList.remove("tutorial-toggled");
  centererTutorial.classList.remove("centerer-tutorial-toggled");
  overlay.classList.remove("overlay-toggled");
});
