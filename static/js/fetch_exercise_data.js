const prm1 = document.currentScript.dataset.param1;
let currentExercise = prm1;

function fetchExerciseData() {
  fetch(`/exercise_data/${currentExercise}`)
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("reps-count").innerText = data.counter;
      document.getElementById("critique-text").innerText = data.critique;
      document.getElementById("stage").innerText = data.stage;

      if (currentExercise === "squat" || currentExercise === "deadlift") {
        document.getElementById("knees-distance-status").innerText =
          data.kneesDistanceStatus;
        document.getElementById("ankles-distance-status").innerText =
          data.anklesDistanceStatus;
      } else {
        document.getElementById("wrists-distance-status").innerText =
          data.wristsDistanceStatus;
        document.getElementById("elbows-distance-status").innerText =
          data.elbowsDistanceStatus;
      }
      console.log(data.kneesDistanceStatus);
      console.log(data.anklesDistanceStatus);
    })
    .catch((error) => console.error("Error fetching exercise data:", error));
}

setInterval(fetchExerciseData, 1000);
