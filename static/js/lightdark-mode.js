const themeToggleButton = document.getElementById("theme-toggle");
const body = document.body;

const savedTheme = localStorage.getItem("theme");
if (savedTheme) {
  body.classList.toggle("dark-mode", savedTheme === "dark");
}

themeToggleButton.addEventListener("click", () => {
  const isDarkMode = body.classList.toggle("dark-mode");
  localStorage.setItem("theme", isDarkMode ? "dark" : "light");
});