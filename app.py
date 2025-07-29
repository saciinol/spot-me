from data.variables import *

################################################################################
#### FLASK SETUP
################################################################################
from flask import Flask, jsonify, render_template, redirect, request, url_for, \
    Response, session
from flask_font_awesome import FontAwesome
app = Flask(__name__)
app.secret_key  = "sikretong_susi"

font_awesome = FontAwesome(app)

################################################################################
#### DATABASE
################################################################################
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

import os
from dotenv import load_dotenv

load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)
dynamic_models = {}

class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

def create_table_name(username, exercise):
    return f"{username}_{exercise}".replace(" ", "")

def table_exists(table_name):
    inspector = inspect(db.engine)

    return table_name in inspector.get_table_names()

def create_table_class(table_name):
    if table_name in dynamic_models:
        return dynamic_models[table_name]

    model = type(
        table_name,
        (db.Model,),
        {
            "__tablename__": table_name,
            "id": db.Column(db.Integer, primary_key=True),
            "date": db.Column(db.String(200), nullable=False),
            "repetitions": db.Column(db.Integer, nullable=False)
        }
    )

    dynamic_models[table_name] = model
    return model

def create_tables():
    with app.app_context():
        for exercise in EXERCISES:
            table_name = create_table_name(session.get("username"), exercise)

            if not table_exists(table_name):
                model = create_table_class(table_name)
                model.__table__.create(bind=db.engine)

################################################################################
#### ACCOUNT MANAGEMENT
################################################################################
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login/loging", methods=["POST"])
def login_account():
    if request.method == "POST":
        data = request.get_json()
        user = Accounts.query.filter_by(username=data.get("username")).first()

        if not user:
            return jsonify({"response": 404})
        else:
            password = data.get("password")
            check = user.password

            if password == check:
                session["id"] = user.id
                session["username"] = user.username
                create_tables()

                return jsonify({"response": 200})
            else:
                return jsonify({"response": 400})

@app.route("/create-account")
def create_account():
    return render_template("create-account.html")

@app.route("/create-account/creating", methods=["POST"])
def creating():
    if request.method == "POST":
        data = request.get_json()

        password = data.get("password")
        confirmation = data.get("confirmPassword")
        username = data.get("username")
        user = Accounts.query.filter_by(username=username).first()

        if not user:
          if len(password) < 8:
                return jsonify({"response": 404})
          elif password == confirmation:
                user = Accounts(
                    email=data.get("email"),
                    username=username,
                    password=password
                )

                db.session.add(user)
                db.session.commit()

                return jsonify({"response": 200})
          else:
                return jsonify({"response": 400})
        else:
            return jsonify({"response": 405})

##########################################################################
### FLASK MAIL SETUP
##########################################################################

@app.route("/forgot-password")
def forgot_password():
    return render_template("forgot-password.html")

from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'spotme.webapp@gmail.com'
app.config['MAIL_PASSWORD'] = 'uivopefppwunyinv'
mail = Mail(app)

# Serializer for generating secure tokens
serializer = URLSafeTimedSerializer(app.secret_key)

@app.route("/forgot-password/send-link", methods=["POST"])
def send_reset_link():
    data = request.get_json()
    email = data.get("email")
    user = Accounts.query.filter_by(email=email).first()

    if not user:
        return jsonify({"response": 404})
    else:
        token = serializer.dumps(email, salt="password-reset-salt")
        reset_url = url_for("reset_password", token=token, _external=True)

        # Send email
        msg = Message("Password Reset Request", sender="spotme.webapp@gmail.com", recipients=[email])
        msg.body = f"Click the link to reset your password: {reset_url}"
        mail.send(msg)

        return jsonify({"response": 200})

@app.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    try:
        email = serializer.loads(token, salt="password-reset-salt", max_age=3600)
    except:
        return "The reset link is invalid or has expired.", 400

    if request.method == "POST":
        data = request.get_json()
        password = data.get("password")
        confirm_password = data.get("confirmPassword")

        if len(password) < 8:
                return jsonify({"response": 401})
        elif password == confirm_password:
            user = Accounts.query.filter_by(email=email).first()

            if not user:
              return jsonify({"response": 404})  # User not found
            else:
              user.password = password
              db.session.commit()
              return jsonify({"response": 200})
        else:
            return jsonify({"response": 400})  # Passwords do not match

    return render_template("reset-password.html", token=token)

@app.route("/change-password")
def change_password():
    return render_template("change-password.html")

@app.route("/change-password/changing", methods = ["POST"])
def changing_change():
    if request.method == "POST":
        data = request.get_json()
        user = Accounts.query.filter_by(username=data.get("username")).first()

        if not user:
            return jsonify({"response": 404})
        elif user.id != session.get("id"):
            return jsonify({"response": 401})
        else:
            email = data.get("email")
            oldPassword = data.get("oldPassword")
            newPassword = data.get("newPassword")

            if email != user.email:
                return jsonify({"response": 403})
            elif oldPassword != user.password:
                return jsonify({"response": 405})
            elif len(newPassword) < 8:
                return jsonify({"response": 400})
            else:
                user.password = newPassword

                db.session.add(user)
                db.session.commit()

                return jsonify({"response": 200})

@app.route("/delete-account")
def delete_account():
    return render_template("delete-account.html")

@app.route("/delete-account/deleting", methods = ["POST"])
def deleting():
    if request.method == "POST":
        data = request.get_json()
        user = Accounts.query.filter_by(username=data.get("username")).first()

        if not user:
            return jsonify({"response": 404})
        elif user.id != session.get("id"):
            return jsonify({"response": 401})
        else:
            email = data.get("email")
            password = data.get("password")

            if email != user.email:
                return jsonify({"response": 403})
            elif password != user.password:
                return jsonify({"response": 405})
            else:
                db.session.delete(user)
                db.session.commit()

                return jsonify({"response": 200})

@app.route("/logout")
def logout():
    session.clear()

    return redirect(url_for("login"))

################################################################################
#### FORM ANALYSIS
################################################################################
import cv2
import mediapipe as mp
import numpy as np

from threading import Event

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
camera = cv2.VideoCapture(0)

from functions.face_detection.face_detection import detect_face
from functions.coordinates.coordinates import get_coords
from functions.angle_distance.angle_distance import get_angles, get_distances
from functions.statuses.statuses import get_distance_wrists_status, \
    get_distance_elbows_status, get_distance_knees_status, \
    get_distance_ankles_status
# from functions.critique.critique import get_critique_upper, get_critique_lower
from functions.text_to_speech.text_to_speech import text_to_speech

pause_event = Event()

def get_critique_upper(
                 exercise,
                 distance_wrists_status,
                 distance_elbows_status):
    global last_critique

    voice_critique = None


    if distance_wrists_status == "Wide" and distance_elbows_status == "Wide":
        voice_critique = "You're arms are too wide narrow them"
    elif distance_wrists_status == "Narrow" and distance_elbows_status == "Narrow":
        voice_critique = "You're arms are too narrow widen them"
    elif distance_wrists_status == "High" and distance_elbows_status == "High":
        voice_critique = "You're arms are too high lower them"
    else:
        voice_critique = "Perfect form"

    if voice_critique and voice_critique != last_critique[exercise]:
        text_to_speech(voice_critique)
        last_critique[exercise] = voice_critique

def get_critique_lower(
                 exercise,
                 distance_knees_status,
                 distance_ankles_status):
    global last_critique

    voice_critique = None

    if distance_knees_status == "Wide" and distance_ankles_status == "Wide":
        voice_critique = "You're legs are too wide narrow them"
    elif distance_knees_status == "Narrow" and distance_ankles_status == "Narrow":
        voice_critique = "You're legs are too narrow widen them"
    else:
        voice_critique = "Perfect form"

    if voice_critique and voice_critique != last_critique[exercise]:
        text_to_speech(voice_critique)
        last_critique[exercise] = voice_critique

def analyze_barbell_curl(results, image, exercise):
    global counter, stage, last_critique, distance_wrists, \
        distance_elbows, distance_wrists_status, distance_elbows_status

    if exercise == "barbell_curl":
        exercise = "barbell_curl"
    elif exercise == "dumbbell_bicep_curl":
        exercise = "dumbbell_bicep_curl"

    try:
        coords = get_coords("upper", results)
        left_angle, right_angle, avg_angle = get_angles("upper", coords)

        # Visualize angles
        if "left_elbow" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_elbow" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        # Count reps based on angle
        if similar and avg_angle >= 150:
            stage[exercise] = "down"

        if similar and avg_angle <= 30 and stage[exercise] == "down" and \
            distance_wrists_status == "Neutral" and \
            distance_elbows_status == "Neutral":
            stage[exercise] = "up"
            counter[exercise] += 1

        distance_wrists, distance_elbows = get_distances("upper", coords)

        distance_wrists_status = get_distance_wrists_status(
            exercise, distance_wrists)
        distance_elbows_status = get_distance_elbows_status(
            exercise, distance_elbows)



        # Count reps based on angle
        if avg_angle >= 150:
            stage[exercise] = "down"

        if avg_angle <= 30 and stage[exercise] == "down" and \
            distance_wrists_status == "Neutral" and \
            distance_elbows_status == "Neutral":
            stage[exercise] = "up"
            counter[exercise] += 1

        get_critique_upper(exercise, distance_wrists_status,
            distance_elbows_status)

    except Exception as e:
        print("Error in barbell curl analysis:", e)
        return "Error", counter[exercise]

def analyze_bench_press(results, image):
    global counter, stage, last_critique, distance_wrists, \
        distance_elbows, distance_wrists_status, distance_elbows_status

    exercise = "bench_press"

    try:
        coords = get_coords("upper", results)
        left_angle, right_angle, avg_angle = get_angles("upper", coords)

        # Visualize angles
        if "left_elbow" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_elbow" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        distance_wrists, distance_elbows = get_distances("upper", coords)

        distance_wrists_status = get_distance_wrists_status(
            exercise, distance_wrists)
        distance_elbows_status = get_distance_elbows_status(
            exercise, distance_elbows)

        if similar and avg_angle >= 130 and stage[exercise] == "up" and \
            distance_wrists_status == "Neutral" and \
            distance_elbows_status == "Neutral":
            stage[exercise] = "down"
            counter[exercise] += 1

        if avg_angle <= 100:
            stage[exercise] = "up"

        get_critique_upper(exercise, distance_wrists_status,
            distance_elbows_status)

    except Exception as e:
        print("Error in analysis:", e)
        return "Error", counter["bench_press"]

def analyze_dumbbell_bench_press(results, image):
    global counter, stage, last_critique, distance_wrists, \
        distance_elbows, distance_wrists_status, distance_elbows_status

    exercise = "dumbbell_bench_press"

    try:
        coords = get_coords("upper", results)
        left_angle, right_angle, avg_angle = get_angles("upper", coords)

        if "left_elbow" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_elbow" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        distance_wrists, distance_elbows = get_distances("upper", coords)


        distance_wrists_status = get_distance_wrists_status(exercise,
            distance_wrists)
        distance_elbows_status = get_distance_elbows_status(exercise,
            distance_elbows)


        # Count reps based on angle
        if similar and avg_angle >= 110 and stage[exercise] == "up" and \
        distance_wrists_status == "Neutral" and \
            distance_elbows_status == "Neutral":
            stage[exercise] = "down"
            counter[exercise] += 1

        if avg_angle <= 60:
            stage[exercise] = "up"

        get_critique_upper(exercise, distance_wrists_status,
                           distance_elbows_status)

    except Exception as e:
        print("Error in analysis:", e)
        return "Error", counter[exercise]

def analyze_barbell_press(results, image, exercise):
    global counter, stage, last_critique, distance_wrists, \
        distance_elbows, distance_wrists_status, distance_elbows_status

    if exercise == "barbell_press":
        exercise = "barbell_press"
    elif exercise == "dumbbell_press":
        exercise = "dumbbell_press"

    try:
        coords = get_coords("upper", results)
        left_angle, right_angle, avg_angle = get_angles("upper", coords)

        # Visualize angles
        if "left_elbow" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_elbow" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        distance_wrists, distance_elbows = get_distances("upper", coords)

        distance_wrists_status = get_distance_wrists_status(
            exercise, distance_wrists)
        distance_elbows_status = get_distance_elbows_status(
            exercise, distance_elbows)

        # Count reps based on angle
        if similar and avg_angle >= 140 and stage[exercise] == "up" and \
            distance_wrists_status == "Neutral" and \
            distance_elbows_status == "Neutral":
            stage[exercise] = "down"
            counter[exercise] += 1

        if avg_angle <= 30:
            stage[exercise] = "up"

        get_critique_upper(
            exercise,
            distance_wrists_status,
            distance_elbows_status)

    except Exception as e:
        print("Error in analysis:", e)
        return "Error", counter[exercise]

def analyze_lateral_raises(results, image):
    global counter, stage, last_critique, distance_wrists, \
        distance_elbows, distance_wrists_status, distance_elbows_status

    exercise = "lateral_raises"

    try:
        coords = get_coords("upper", results)
        left_angle, right_angle, avg_angle = get_angles("lateral_raises", coords)

        if "left_elbow" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_elbow" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        distance_left, distance_right = get_distances("lateral_raises", coords)

        distance_wrists_status = get_distance_wrists_status(
            exercise, distance_left)
        distance_elbows_status = get_distance_elbows_status(
            exercise, distance_right)


        # Count reps based on angle
        if similar and avg_angle <= 7 and stage[exercise] == "up" and \
            distance_wrists_status == "Neutral" and \
            distance_elbows_status == "Neutral":
            stage[exercise] = "down"
            counter[exercise] += 1

        if avg_angle >= 19:
            stage[exercise] = "up"

        get_critique_upper(
            exercise,
            distance_wrists_status,
            distance_elbows_status)

    except Exception as e:
        print("Error in analysis:", e)
        return "Error", counter[exercise]

def analyze_barbell_rows(results, image):
    global counter, stage, last_critique, distance_wrists, \
        distance_elbows, distance_wrists_status, distance_elbows_status

    exercise = "barbell_rows"

    try:
        coords = get_coords("upper", results)
        left_angle, right_angle, avg_angle = get_angles("upper", coords)

        if "left_elbow" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_elbow" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        distance_wrists, distance_elbows = get_distances("upper", coords)

        distance_wrists_status = get_distance_wrists_status(
            exercise, distance_wrists)
        distance_elbows_status = get_distance_elbows_status(
            exercise, distance_elbows)


        if similar and avg_angle <= 130 and stage[exercise] == "up" and \
            distance_wrists_status == "Neutral" and \
            distance_elbows_status == "Neutral":
            stage[exercise] = "down"
            counter[exercise] += 1

        if avg_angle >= 170:
            stage[exercise] = "up"

        get_critique_upper(
            exercise,
            distance_wrists_status,
            distance_elbows_status)

    except Exception as e:
        print("Error in analysis:", e)
        return "Error", counter[exercise]

def analyze_pullups(results, image):
    global counter, stage, last_critique, distance_wrists, \
        distance_elbows, distance_wrists_status, distance_elbows_status

    exercise = "pull_ups"

    try:
        coords = get_coords("upper", results)
        left_angle, right_angle, avg_angle = get_angles("upper", coords)

        if "left_elbow" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_elbow" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_elbow"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        distance_wrists, distance_elbows = get_distances("upper", coords)

        distance_wrists_status = get_distance_wrists_status(
            exercise, distance_wrists)
        distance_elbows_status = get_distance_elbows_status(
            exercise, distance_elbows)



        # Count reps based on angle
        if avg_angle >= 160:
            stage[exercise] = "up"

        if avg_angle <= 50 and stage[exercise] == "up" and \
            distance_wrists_status == "Neutral" and \
            distance_elbows_status == "Neutral":
            stage[exercise] = "down"
            counter[exercise] += 1

        get_critique_upper(
            exercise,
            distance_wrists_status,
            distance_elbows_status)

    except Exception as e:
        print("Error in analysis:", e)
        return "Error", counter[exercise]

def analyze_squat(results, image):
    global counter, stage, last_critique, distance_knees, \
        distance_ankles, distance_knees_status, distance_ankles_status

    exercise = "squat"

    try:
        coords = get_coords("lower", results)
        left_angle, right_angle, avg_angle = get_angles("lower", coords)

        # Visualize angles
        if "left_knee" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_knee"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_knee" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_knee"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        distance_knees, distance_ankles = get_distances("lower", coords)

        distance_knees_status = get_distance_knees_status(
            exercise, distance_knees)
        distance_ankles_status = get_distance_ankles_status(
            exercise, distance_ankles)


        # Count reps based on angle
        if avg_angle >= 170:
            stage[exercise] = "down"

        # Squatting
        if similar and avg_angle <= 120 and stage[exercise] == "down" and \
            distance_knees_status == "Neutral" and \
            distance_ankles_status == "Neutral":
            stage[exercise] = "up"
            counter[exercise] += 1

        get_critique_lower(
            exercise,
            distance_knees_status,
            distance_ankles_status
        )

    except Exception as e:
        print("Error in analysis:", e)
        return "Error", counter[exercise]

def analyze_deadlift(results, image):
    global counter, stage, last_critique, distance_knees, \
        distance_ankles, distance_knees_status, distance_ankles_status

    exercise = "deadlift"

    try:
        coords = get_coords("lower", results)
        left_angle, right_angle, avg_angle = get_angles("lower", coords)

        # Visualize angles
        if "left_knee" in coords:
            cv2.putText(image, f"{int(left_angle)}",
                        tuple(np.multiply(coords["left_knee"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        if "right_knee" in coords:
            cv2.putText(image, f"{int(right_angle)}",
                        tuple(np.multiply(coords["right_knee"], [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        similar = detect_face(image)
        if not similar:
            cv2.putText(image, "Unauthorized person detected!",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 69, 255), 2, cv2.LINE_AA)

        distance_knees, distance_ankles = get_distances("lower", coords)

        distance_knees_status = get_distance_knees_status(
            exercise, distance_knees)
        distance_ankles_status = get_distance_ankles_status(
            exercise, distance_ankles)


        # Count reps based on angle
        if avg_angle <= 160:  # Standing
            stage[exercise] = "up"

        # Squatting
        if similar and avg_angle >= 160 and stage[exercise] == "up" and \
            distance_knees_status == "Neutral" and \
            distance_ankles_status == "Neutral":
            stage[exercise] = "down"
            counter[exercise] += 1

        get_critique_lower(
            exercise,
            distance_knees_status,
            distance_ankles_status
        )

    except Exception as e:
        print("Error in analysis:", e)
        return "Error", counter[exercise]

# Modular frame creation function
def create_frames(exercise):
    pause_event.clear()

    with mp_pose.Pose(
        min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

        while True:
            if not pause_event.is_set():
                continue

            ret, frame = camera.read()
            if not ret:
                break

            # if exercise == "dumbbell_bench_press":
            #     frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Analyze based on selected exercise
            match exercise:
                case "barbell_curl":
                    analyze_barbell_curl(results, image, exercise)
                case "dumbbell_bicep_curl":
                    analyze_barbell_curl(results, image, exercise)
                case "bench_press":
                    analyze_bench_press(results, image)
                case "dumbbell_bench_press":
                    analyze_dumbbell_bench_press(results, image)
                case "barbell_press":
                    analyze_barbell_press(results, image, exercise)
                case "dumbbell_press":
                    analyze_barbell_press(results, image, exercise)
                case "lateral_raises":
                    analyze_lateral_raises(results, image)
                case "barbell_rows":
                    analyze_barbell_rows(results, image)
                case "pull_ups":
                    analyze_pullups(results, image)
                case "squat":
                    analyze_squat(results, image)
                case "deadlift":
                    analyze_deadlift(results, image)

            # if exercise == "dumbbell_bench_press":
            #     image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

            # Draw pose landmarks
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            _, buffer = cv2.imencode(".jpg", image)
            frame = buffer.tobytes()

            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

################################################################################
#### EXERCISE ROUTES
################################################################################
@app.route("/chest")
def chest():
    return render_template("chest.html")

@app.route("/back")
def back():
    return render_template("back.html")

@app.route("/arms")
def arms():
    return render_template("arms.html")

@app.route("/legs")
def legs():
    return render_template("legs.html")

@app.route("/shoulders")
def shoulders():
    return render_template("shoulders.html")

@app.route("/barbell_curl")
def barbell_curl():
    exercise = "barbell_curl"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/dumbbell_bicep_curl")
def dumbbell_bicep_curl():
    exercise = "dumbbell_bicep_curl"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/bench_press")
def bench_press():
    exercise = "bench_press"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/dumbbell_bench_press")
def dumbbell_bench_press():
    exercise = "dumbbell_bench_press"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/barbell_press")
def barbell_press():
    exercise = "barbell_press"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/dumbbell_press")
def dumbbell_press():
    exercise = "dumbbell_press"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/lateral_raises")
def lateral_raises():
    exercise = "lateral_raises"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/pull_ups")
def pull_ups():
    exercise = "pull_ups"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/barbell_rows")
def barbell_rows():
    exercise = "barbell_rows"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/squat")
def squat():
    exercise = "squat"

    return render_template("video_feed.html", exercise=exercise)

@app.route("/deadlift")
def deadlift():
    exercise = "deadlift"

    return render_template("video_feed.html", exercise=exercise)

################################################################################
#### VIDEO FEED
################################################################################
@app.route("/video_feed")
def video_feed():
    return render_template("video_feed.html")

@app.route("/video/<exercise>")
def video(exercise):
    return Response(create_frames(exercise), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/toggle_pause", methods=["POST"])
def toggle_pause():
    if pause_event.is_set():
        pause_event.clear()
    else:
        pause_event.set()

    return {"status": "paused" if not pause_event.is_set() else "running"}

@app.route("/toggle_tutorial", methods=["POST"])
def toggle_tutorial():
    pause_event.clear()

    return {"status": "paused"}

@app.route("/exercise_data/<exercise>", methods=["GET"])
def exercise_data(exercise):
    global last_critique, counter, stage, distance_wrists_status, \
        distance_elbows_status, distance_knees_status, distance_ankles_status

    if exercise in counter:
        return jsonify({
            "critique": last_critique.get(exercise, "No critique yet"),
            "counter": counter.get(exercise, 0),
            "stage": stage.get(exercise, 0),
            "wristsDistanceStatus": distance_wrists_status,
            "elbowsDistanceStatus": distance_elbows_status,
            "kneesDistanceStatus": distance_knees_status,
            "anklesDistanceStatus": distance_ankles_status
        })
    else:
        return jsonify({"critique": "Invalid exercise", "counter": 0})

@app.route("/reset_counter", methods=["POST"])
def reset_counter():
    global counter

    counter = {
        "barbell_curl": 0,
        "dumbbell_bicep_curl": 0,
        "bench_press": 0,
        "dumbbell_bench_press": 0,
        "barbell_press": 0,
        "dumbbell_press": 0,
        "lateral_raises": 0,
        "pull_ups": 0,
        "squat": 0,
        "deadlift": 0,
        "barbell_rows": 0
    }

    return ("", 204)

################################################################################
#### EXERCISE STATS
################################################################################
import datetime

from typing import OrderedDict

@app.route("/save/<exercise>", methods=["GET", "POST"])
def save(exercise):
    table_name = create_table_name(session.get("username"), exercise)
    model_class = dynamic_models.get(table_name)

    if model_class is None:
        model_class = create_table_class(table_name)

    date = datetime.datetime.now()
    count = str(counter.get(exercise, 0))

    workout = model_class(
        date=date.strftime("%m/%d/%Y %I:%M:%S%p"),
        repetitions=count
    )

    db.session.add(workout)
    db.session.commit()

    return redirect(url_for("stats", exercise=exercise))

@app.route("/stats/<exercise>")
def stats(exercise):
    table_name = create_table_name(session.get("username"), exercise)
    model_class = dynamic_models.get(table_name)

    if model_class is None:
        model_class = create_table_class(table_name)

    if model_class:
        exercise_data = model_class.query.all()

    ids = []
    dates = []
    exercise_reps = []
    workouts = {}

    for row in exercise_data:
        ids.append(row.id)
        exercise_reps.append(row.repetitions)
        dates.append(row.date)

    for _id, date, reps in zip(ids, dates, exercise_reps):
        workouts[_id] = (date, reps)

    workouts = OrderedDict(reversed(list(workouts.items())))

    match exercise:
        case "barbell_curl":
            name_exercise = "Barbell Bicep Curl"
        case "dumbbell_bicep_curl":
            name_exercise = "Dumbbell Bicep Curl"
        case "bench_press":
            name_exercise = "Bench Press"
        case "dumbbell_bench_press":
            name_exercise = "Dumbbell Bench Press"
        case "barbell_press":
            name_exercise = "Barbell Press"
        case "dumbbell_press":
            name_exercise = "Dumbbell Press"
        case "pull_ups":
            name_exercise = "Pull Ups"
        case "barbell_rows":
            name_exercise = "Barbell Rows"
        case "squat":
            name_exercise = "Squat"
        case "deadlift":
            name_exercise = "Deadlift"
        case "lateral_raises":
            name_exercise = "Lateral Raises"

    return render_template(
        "stats.html",
        exercise=exercise,
        name_exercise=name_exercise,
        workouts=workouts
    )

@app.route("/get_progress/<exercise>/<duration>", methods=["POST"])
def get_progress(exercise, duration):
    table_name = create_table_name(session.get("username"), exercise)
    model_class = dynamic_models.get(table_name)

    if model_class is None:
        model_class = create_table_class(table_name)

    if model_class:
        exercise_data = model_class.query.all()

    collected_reps = []

    for row in exercise_data:
        collected_reps.append(row.repetitions)

    match duration:
        case "weekly":
            collected_reps = collected_reps[-7:]
        case "monthly":
            collected_reps = collected_reps[-30:]
        case _:
            pass

    return jsonify({"reps": collected_reps})

@app.route("/delete_set/<exercise>/<_id>", methods=["POST"])
def delete_set(exercise, _id):
    table_name = create_table_name(session.get("username"), exercise)
    model_class = dynamic_models.get(table_name)

    if model_class is None:
        model_class = create_table_class(table_name)

    workout = model_class.query.filter_by(id=_id).first()

    if workout:
        db.session.delete(workout)
        db.session.commit()

        return jsonify({"status": "deleted"})

################################################################################
#### ADDITIONAL INFO
################################################################################
@app.route("/search/terminologies", methods=["POST"])
def search_terminologies():
    data = request.get_json()
    term = data.get("searchTerm")
    terms = get_terminologies(term)

    return jsonify(terms)

@app.route("/all_terminologies", methods=["POST"])
def all_terminologies():
    terms = get_all_terminologies()

    return jsonify(terms)

@app.route("/all_tips", methods=["POST"])
def all_tips():
    terms = get_all_tips()

    return jsonify(terms)

@app.route("/search/tips", methods=["POST"])
def search_tips():
    data = request.get_json()
    tip = data.get("searchTerm")
    tips = get_tips(tip)

    return jsonify(tips)

################################################################################
#### MAIN PAGES
################################################################################
from functions.databases.terminologies import initialize_terminologies, \
    get_terminologies, get_all_terminologies
from functions.databases.tips import initialize_tips, get_tips, get_all_tips

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/disclaimer")
def disclaimer():
    return render_template("disclaimer.html")

@app.route("/index")
def index():
    initialize_terminologies()
    initialize_tips()

    return render_template("index.html")

@app.route("/categories")
def categories():

    return render_template("categories.html")

@app.route("/terminologies")
def terminologies():
    return render_template("terminologies.html")

@app.route("/tips")
def tips():
    return render_template("tips.html")

if __name__ == "__main__":
    app.run(debug=True)