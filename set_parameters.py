def setParameters():
    workoutLengthInMinutes = input("How many minutes would you like to workout? ")
    workoutInterval = input("Choose an interval (in seconds): ")
    restInterval = input("How many seconds would you like to rest? ")
    parameters = [workoutLengthInMinutes, restInterval, workoutInterval]
    return parameters
