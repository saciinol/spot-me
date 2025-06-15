import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def get_landmark_coords(results, landmarks_to_track):
    # Extracts specified landmark coordinates from Mediapipe results.
    coords = {}

    try:
        landmarks = results.pose_landmarks.landmark
        for name, index in landmarks_to_track.items():
            coords[name] = [landmarks[index].x, landmarks[index].y]
    except Exception as e:
        print("Error extracting landmark coordinates:", e)

    return coords

def get_coords(section, results):
    if section == "upper":
        landmarks_to_track = {
            "left_shoulder": mp_pose.PoseLandmark.LEFT_SHOULDER.value,
            "left_elbow": mp_pose.PoseLandmark.LEFT_ELBOW.value,
            "left_wrist": mp_pose.PoseLandmark.LEFT_WRIST.value,
            "right_shoulder": mp_pose.PoseLandmark.RIGHT_SHOULDER.value,
            "right_elbow": mp_pose.PoseLandmark.RIGHT_ELBOW.value,
            "right_wrist": mp_pose.PoseLandmark.RIGHT_WRIST.value
        }
    elif section == "lower":
        landmarks_to_track = {
            "left_hip": mp_pose.PoseLandmark.LEFT_HIP.value,
            "left_knee": mp_pose.PoseLandmark.LEFT_KNEE.value,
            "left_ankle": mp_pose.PoseLandmark.LEFT_ANKLE.value,
            "right_hip": mp_pose.PoseLandmark.RIGHT_HIP.value,
            "right_knee": mp_pose.PoseLandmark.RIGHT_KNEE.value,
            "right_ankle": mp_pose.PoseLandmark.RIGHT_ANKLE.value        
        }
        
    coords = get_landmark_coords(results, landmarks_to_track)

    return coords