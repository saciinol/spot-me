// document.querySelector(".btn-yesno").addEventListener("click", (e) => {
//     if (e.target.classList.contains("delete-delete")) {
//       const id = e.target.dataset.id;
//       const exercise = e.target.dataset.exercise;
//       alert(`${id}:${exercise}`);

//       function deleteSet(id, exercise) {
//         fetch(`/delete_set/${exercise}/${id}`, {
//           method: "POST",
//         }).then((_) => {
//           location.reload();
//         });
//       }

//       deleteSet(id, exercise);
//     }
// });

// document.querySelector(".popup-delete").addEventListener("click", (e) => {
//   if (e.target.classList.contains("delete-delete")) {
//     const id = e.target.dataset.id;
//     const exercise = e.target.dataset.exercise;
//     alert(`${id}:${exercise}`);

//     // function deleteSet(id, exercise) {
//     //   fetch(`/delete_set/${exercise}/${id}`, {
//     //     method: "POST",
//     //   }).then((_) => {
//     //     location.reload();
//     //   });
//     // }

//     // deleteSet(id, exercise);
//   }
// })

function deleteSet(id, exercise) {
  fetch(`/delete_set/${exercise}/${id}`, {
    method: "POST",
  }).then((_) => {
    location.reload();
  });
}
