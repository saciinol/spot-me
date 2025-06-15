import numpy as np
import math

def calculate_angle(a, b, c):
    # Calculate the angle between three points.
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(
        c[1] - b[1], c[0] - b[0]
        ) - np.arctan2(
        a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

def calculate_distance(a, b):
    distance = round(math.sqrt((b[1] - b[0]) ** 2 + (a[1] - a[0]) ** 2), 2)

    return distance