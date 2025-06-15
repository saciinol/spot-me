const toggleMenu = document.querySelector(".toggle-menu");
let burgerSidebar = document.getElementById("burger-sidebar");
let overlay = document.getElementById("overlay");
let burgerX = document.getElementById("burger-x");

let bodyOverflow = document.querySelector("body");

toggleMenu.addEventListener("click", () => {
  burgerSidebar.classList.toggle("burger-sidebar-toggled");
  overlay.classList.toggle("overlay-toggled");
  burgerX.classList.toggle("burger-x-toggled");
  bodyOverflow.classList.add("body-toggled");
});

burgerX.addEventListener("click", () => {
  burgerSidebar.classList.remove("burger-sidebar-toggled");
  overlay.classList.remove("overlay-toggled");
  burgerX.classList.remove("burger-x-toggled");
  bodyOverflow.classList.remove("body-toggled");
});

const instructionBTN = document.querySelector(".btn-burger");
const instructions = document.getElementById("instructions");
const instructionsX = document.getElementById("instructions-x");

instructionBTN.addEventListener("click", () => {
  instructions.classList.toggle("instructions-toggled");
  instructionsX.classList.toggle("instructions-x-toggled");
});

instructionsX.addEventListener("click", () => {
  instructions.classList.remove("instructions-toggled");
  instructionsX.classList.remove("instructions-x-toggled");
});
