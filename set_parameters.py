def setParameters():
    workoutLengthInMinutes = int(input("How many minutes would you like to workout? "))
    workoutInterval = int(input("Choose an interval (in seconds): "))
    restInterval = int(input("How many seconds would you like to rest? "))
    parameters = [workoutLengthInMinutes, restInterval, workoutInterval]
    return parameters
