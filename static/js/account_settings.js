const accountSettings = document.querySelector(".account-settings");

accountSettings.addEventListener("click", () => {
  document
    .querySelector(".account-settings__content")
    .classList.toggle("account-settings__content-toggled");
  document
    .querySelector(".sidebar-chevron-down")
    .classList.toggle("sidebar-chevron-down-toggled");
  document
    .querySelector(".sidebar-chevron-up")
    .classList.toggle("sidebar-chevron-up-toggled");
});
