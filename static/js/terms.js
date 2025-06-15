const termsBtns = document.querySelectorAll(".btn-terms");

termsBtns.forEach((btn, index) => {
  btn.addEventListener("click", () => {
    function open() {
      document
        .querySelectorAll(".terms-content")
        [index].classList.toggle("terms-content-toggled");
      document
        .querySelectorAll(".chevron-down")
        [index].classList.toggle("chevron-down-toggled");
      document
        .querySelectorAll(".chevron-up")
        [index].classList.toggle("chevron-up-toggled");
    }

    setTimeout(open, 0);
  });
});
