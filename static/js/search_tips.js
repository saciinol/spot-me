const search = document.querySelector("#search");
const tips = document.querySelector("#tips-list");

if (search.value === "") {
  fetch("/all_tips", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);

      data.forEach((entry) => {
        const node = document.createElement("li");
        node.classList.toggle("terms-tips");

        const dropdownHeader = document.createElement("div");
        dropdownHeader.classList.toggle("dropdown-header");
        node.appendChild(dropdownHeader);

        const heading = document.createElement("h3");
        heading.classList.toggle("btn-terms");
        heading.textContent = `${entry[1]}`;
        dropdownHeader.appendChild(heading);

        const downIcon = document.createElement("span");
        downIcon.classList.toggle("termstips-chevron-down");
        downIcon.classList.add("fas", "fa-chevron-down");
        dropdownHeader.appendChild(downIcon);

        const upIcon = document.createElement("span");  
        upIcon.classList.toggle("termstips-chevron-up");
        upIcon.classList.add("fas", "fa-chevron-up");
        dropdownHeader.appendChild(upIcon);


        const div = document.createElement("div");
        div.classList.toggle("terms-content");
        node.appendChild(div);

        const hr = document.createElement("hr");
        div.appendChild(hr);

        const info = document.createElement("p");
        info.textContent = `${entry[2]}`;
        div.appendChild(info);

        tips.appendChild(node);
      });

      const termsBtns = document.querySelectorAll(".dropdown-header");

      termsBtns.forEach((btn, index) => {
        btn.addEventListener("click", () => {
          function open() {
            document
              .querySelectorAll(".terms-content")
              [index].classList.toggle("terms-content-toggled");
            document
              .querySelectorAll(".termstips-chevron-down")
              [index].classList.toggle("termstips-chevron-down-toggled");
            document
              .querySelectorAll(".termstips-chevron-up")
              [index].classList.toggle("termstips-chevron-up-toggled");
          }

          setTimeout(open, 0);
        });
      });
    });
}

search.addEventListener("keyup", () => {
  const tip = search.value;

  fetch("/search/tips", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ searchTerm: tip }),
  })
    .then((response) => response.json())
    .then((data) => {
      tips.innerHTML = "";

      if (data.length === 0) {
        const node = document.createElement("li");
        node.textContent = "No results found";
        tips.appendChild(node);
        return;
      }

      data.forEach((entry) => {
        const node = document.createElement("li");
        node.classList.toggle("terms-tips");

        const dropdownHeader = document.createElement("div");
        dropdownHeader.classList.toggle("dropdown-header");
        node.appendChild(dropdownHeader);

        const heading = document.createElement("h3");
        heading.classList.toggle("btn-terms");
        heading.textContent = `${entry[0]}`;
        dropdownHeader.appendChild(heading);

        const downIcon = document.createElement("span");
        downIcon.classList.toggle("termstips-chevron-down");
        downIcon.classList.add("fas", "fa-chevron-down");
        dropdownHeader.appendChild(downIcon);

        const upIcon = document.createElement("span");  
        upIcon.classList.toggle("termstips-chevron-up");
        upIcon.classList.add("fas", "fa-chevron-up");
        dropdownHeader.appendChild(upIcon);

        const div = document.createElement("div");
        div.classList.toggle("terms-content");
        node.appendChild(div);

        const hr = document.createElement("hr");
        div.appendChild(hr);

        const info = document.createElement("p");
        info.textContent = `${entry[1]}`;
        div.appendChild(info);

        tips.appendChild(node);
      });

      const termsBtns = document.querySelectorAll(".dropdown-header");

      termsBtns.forEach((btn, index) => {
        btn.addEventListener("click", () => {
          function open() {
            document
              .querySelectorAll(".terms-content")
              [index].classList.toggle("terms-content-toggled");
            document
              .querySelectorAll(".termstips-chevron-down")
              [index].classList.toggle("termstips-chevron-down-toggled");
            document
              .querySelectorAll(".termstips-chevron-up")
              [index].classList.toggle("termstips-chevron-up-toggled");
          }

          setTimeout(open, 0);
        });
      });
    });
});
