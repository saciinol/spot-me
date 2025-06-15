# Global variables for exercise tracking
EXERCISES = [
    "barbell_curl",
    "dumbbell_bicep_curl",
    "bench_press",
    "dumbbell_bench_press",
    "barbell_press",
    "dumbbell_press",
    "lateral_raises",
    "pull_ups",
    "barbell_rows",
    "squat",
    "deadlift"
]

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

stage = {
    "barbell_curl": "X", 
    "dumbbell_bicep_curl": "X", 
    "bench_press": "X", 
    "dumbbell_bench_press": "X",
    "barbell_press": "X",
    "dumbbell_press": "X",
    "lateral_raises": "X",
    "pull_ups": "X",
    "squat": "X",
    "deadlift": "X",        
    "barbell_rows": "X"
}

last_critique = {
    "barbell_curl": "X", 
    "dumbbell_bicep_curl": "X", 
    "bench_press": "X", 
    "dumbbell_bench_press": "X",
    "barbell_press": "X",
    "dumbbell_press": "X",
    "lateral_raises": "X",
    "pull_ups": "X",
    "squat": "X",
    "deadlift": "X",    
    "barbell_rows": "X"
}

distance_wrists = 0
distance_elbows = 0

distance_wrists_greater = 0
distance_wrists_lesser = 0

distance_elbows_greater = 0
distance_elbows_lesser = 0

distance_wrists_status = 0
distance_elbows_status = 0

distance_knees = 0
distance_ankles = 0

distance_knees_greater = 0
distance_knees_lesser = 0

distance_ankles_greater = 0
distance_ankles_lesser = 0

distance_knees_status = 0
distance_ankles_status = 0
