import sys

#workouts
five_min_wake_up = [5, 1, 30]

def loadWorkOut(argv1):
   
    workoutParameters = [0,0,0]

    if argv1 == "five_min_wake_up":
        workoutParameters[0] = five_min_wake_up[0]
        workoutParameters[1] = five_min_wake_up[1]
        workoutParameters[2] = five_min_wake_up[2]
        return workoutParameters
    else:
        return workoutParameters

chest_exercises = [
    "standard push ups",
    "diamond push ups",
    "wide push ups"
]

cardio = [
    "jumping jacks",
    "knee ups"
]



    



