# Facial recognition
import cv2
import time
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

reference_face_embedding = None # Storing reference face
last_seen_time = time.time() # Track when last face was seen
face_lost_threshold = 10 # Time till face reauthentication

def get_face_embedding(face):
    # Convert face into embedding for comparison
    blob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96), (0, 0, 0),
                                swapRB=True, crop=False)

    return blob

def cosine_similarity(emb1, emb2):
    # Compare cosine similarity between faces
    return np.dot(
        emb1.flatten(), emb2.flatten()) / (
        np.linalg.norm(emb1) * np.linalg.norm(emb2))

def detect_face(image):
    global reference_face_embedding, last_seen_time
    similar = True

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    if len(faces) == 0:
        if reference_face_embedding is not None and time.time() - last_seen_time > face_lost_threshold:
            reference_face_embedding = None

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    x, y, w, h = faces[0]
    face_frame = image[y:y+h, x:x+w]

    face_embedding = get_face_embedding(face_frame) # Getting the reference face
    
    if reference_face_embedding is None:
        # If no reference face yet, assign the newly detected face
        reference_face_embedding = face_embedding
        last_seen_time = time.time() # Reset since we have new ref
    else:
        similarity = cosine_similarity(reference_face_embedding, face_embedding)

        if similarity < 0.71: # Checks for anyone else in view
            similar = False

    last_seen_time = time.time()

    return similar