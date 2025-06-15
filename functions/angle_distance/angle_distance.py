from ..calculations import calculations

def get_angles(section, coords):
    if section == "upper":
        left_angle = calculations.calculate_angle(coords["left_shoulder"], coords["left_elbow"], coords["left_wrist"])
        right_angle = calculations.calculate_angle(coords["right_shoulder"], coords["right_elbow"], coords["right_wrist"])
    elif section == "lower":
        left_angle = calculations.calculate_angle(coords["left_hip"], coords["left_knee"], coords["left_ankle"])
        right_angle = calculations.calculate_angle(coords["right_hip"], coords["right_knee"], coords["right_ankle"])
    elif section == "lateral_raises":
        neck = [(coords["left_shoulder"][0] + coords["right_shoulder"][0]) / 2,
                (coords["left_shoulder"][1] + coords["right_shoulder"][1]) / 2]

        left_angle = calculations.calculate_angle(coords["left_shoulder"], coords["left_elbow"], neck)
        right_angle = calculations.calculate_angle(coords["right_shoulder"], coords["right_elbow"], neck)

    avg_angle = (left_angle + right_angle) / 2

    return left_angle, right_angle, avg_angle
    
def get_distances(section, coords):
    if section == "upper":
        distance_wrists = calculations.calculate_distance(coords["left_wrist"], coords["right_wrist"])
        distance_elbows = calculations.calculate_distance(coords["left_elbow"], coords["right_elbow"])

        return distance_wrists, distance_elbows
    elif section == "lower":
        distance_knees = calculations.calculate_distance(coords["left_knee"], coords["right_knee"])
        distance_ankles = calculations.calculate_distance(coords["left_ankle"], coords["right_ankle"])

        return distance_knees, distance_ankles
    elif section == "lateral_raises":
        distance_left = calculations.calculate_distance(coords["left_elbow"], coords["left_shoulder"])
        distance_right = calculations.calculate_distance(coords["right_elbow"], coords["right_shoulder"])

        return distance_left, distance_right