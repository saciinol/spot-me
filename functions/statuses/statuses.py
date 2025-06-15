def get_distance_wrists_status(exercise, distance_wrists):
    match exercise:
        case "barbell_curl":
            if distance_wrists > 2.00:
                distance_wrists_status = "Wide"
            elif distance_wrists < 0.20:
                distance_wrists_status = "Narrow"
            else:
                distance_wrists_status = "Neutral"
        case "dumbbell_bicep_curl":
            if distance_wrists > 0.45:
                distance_wrists_status = "Wide"
            elif distance_wrists < 0.30:
                distance_wrists_status = "Narrow"
            else:
                distance_wrists_status = "Neutral"
        case "bench_press":
            if distance_wrists > 0.8:
                distance_wrists_status = "Wide"
            elif distance_wrists < 0.3:
                distance_wrists_status = "Narrow"
            else:
                distance_wrists_status = "Neutral"
        case "dumbbell_bench_press":
            if distance_wrists > 0.65:
                distance_wrists_status = "Wide"
            elif distance_wrists < 0.3:
                distance_wrists_status = "Narrow"
            else:
                distance_wrists_status = "Neutral"
        case "barbell_press":
            if distance_wrists > 0.70:
                distance_wrists_status = "Wide"
            elif distance_wrists < 0.40:
                distance_wrists_status = "Narrow"
            else:
                distance_wrists_status = "Neutral"
        case "dumbbell_press":
            if distance_wrists > 0.70:
                distance_wrists_status = "Wide"
            elif distance_wrists < 0.40:
                distance_wrists_status = "Narrow"
            else:
                distance_wrists_status = "Neutral"
        case "lateral_raises":
            if distance_wrists > 0.4:
                distance_wrists_status = "High"
            else:
                distance_wrists_status = "Neutral"
        case "barbell_rows":
            if distance_wrists > 0.4:
                distance_wrists_status = "Wide"
            elif distance_wrists < 0.1:
                distance_wrists_status = "Narrow"
            else:
                distance_wrists_status = "Neutral"
        case "pull_ups":
            if distance_wrists > 0.5:
                distance_wrists_status = "Wide"
            elif distance_wrists < 0.1:
                distance_wrists_status = "Narrow"
            else:
                distance_wrists_status = "Neutral"

    return distance_wrists_status

def get_distance_elbows_status(exercise, distance_elbows):
    match exercise:
        case "barbell_curl":
            if distance_elbows > 0.50:
                distance_elbows_status = "Wide"
            elif distance_elbows < 0.15:
                distance_elbows_status = "Narrow"
            else:
                distance_elbows_status = "Neutral"            
        case "dumbbell_bicep_curl":
            if distance_elbows > 0.30:
                distance_elbows_status = "Wide"
            elif distance_elbows < 0.15:
                distance_elbows_status = "Narrow"
            else:
                distance_elbows_status = "Neutral"            
        case "bench_press":
            if distance_elbows > 0.8:
                distance_elbows_status = "Wide"
            elif distance_elbows < 0.3:
                distance_elbows_status = "Narrow"
            else:
                distance_elbows_status = "Neutral"   
        case "dumbbell_bench_press":
            if distance_elbows > 0.7:
                distance_elbows_status = "Wide"
            elif distance_elbows < 0.3:
                distance_elbows_status = "Narrow"
            else:
                distance_elbows_status = "Neutral"            
        case "barbell_press":
            if distance_elbows > 0.50:
                distance_elbows_status = "Wide"
            elif distance_elbows < 0.20:
                distance_elbows_status = "Narrow"
            else:
                distance_elbows_status = "Neutral"            
        case "dumbbell_press":
            if distance_elbows > 0.50:
                distance_elbows_status = "Wide"
            elif distance_elbows < 0.20:
                distance_elbows_status = "Narrow"
            else:
                distance_elbows_status = "Neutral"            
        case "lateral_raises":
            if distance_elbows > 0.3:
                distance_elbows_status = "High"
            else:
                distance_elbows_status = "Neutral"            
        case "barbell_rows":
            if distance_elbows > 0.4:
                distance_elbows_status = "Wide"
            elif distance_elbows < 0.1:
                distance_elbows_status = "Narrow"
            else:
                distance_elbows_status = "Neutral"            
        case "pull_ups":
            if distance_elbows > 0.5:
                distance_elbows_status = "Wide"
            elif distance_elbows < 0.1:
                distance_elbows_status = "Narrow"
            else:
                distance_elbows_status = "Neutral"            

    return distance_elbows_status

def get_distance_knees_status(exercise, distance_knees):
    match exercise:
        case "squat":
            if distance_knees > 0.6:
                distance_knees_status = "Wide"
            elif distance_knees < 0.2:
                distance_knees_status = "Narrow"
            else:
                distance_knees_status = "Neutral"
        case "deadlift":
            if distance_knees > 0.5:
                distance_knees_status = "Wide"
            elif distance_knees < 0.1:
                distance_knees_status = "Narrow"
            else:
                distance_knees_status = "Neutral"
    
    return distance_knees_status

def get_distance_ankles_status(exercise, distance_ankles):
    match exercise:
        case "squat":
            if distance_ankles > 0.6:
                distance_ankles_status = "Wide"
            elif distance_ankles < 0.2:
                distance_ankles_status = "Narrow"
            else:
                distance_ankles_status = "Neutral"            
        case "deadlift":
            if distance_ankles > 0.7:
                distance_ankles_status = "Wide"
            elif distance_ankles < 0.2:
                distance_ankles_status = "Narrow"
            else:
                distance_ankles_status = "Neutral"            
    
    return distance_ankles_status