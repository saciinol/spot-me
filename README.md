# SpotMe 🏋️‍♂️

A computer vision-based fitness tracker that provides **real-time voice feedback** to help users correct their form while exercising. Designed to assist with posture awareness during strength training.

---

## 🧠 Features

- Real-time body joint detection via webcam
- Voice feedback for correcting form
- Progress tracking for completed workouts

---

## 🔧 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Database**: PostgreSQL
- **Computer Vision**: Mediapipe Pose Estimation
- **Others**: Web Speech API (Text-to-Speech)

---

## 📸 Screenshots

<img src="./static/images/ss/login.png" alt="Screenshot" width="250"/>
<img src="./static/images/ss/dashboard.png" alt="Screenshot" width="250"/>
<img src="./static/images/ss/pose-detection.png" alt="Screenshot" width="250"/>

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saciinol/spot-me.git
   cd spot-me

2. **Create a virtual environment & install dependencies**
  python -m venv venv
  source venv/bin/activate  # or venv\Scripts\activate on Windows
  pip install -r requirements.txt

3. **Run the app**
  flask run

4. **Open in browser**
  Open in browser
