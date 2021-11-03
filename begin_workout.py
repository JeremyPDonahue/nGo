import sys
import time
import set_parameters
import play_clip
import workouts

def beginWorkout():

    workoutRoutine = workouts.loadWorkOut(sys.argv[1])

    if workoutRoutine == []:
        parameters = set_parameters.setParameters()
    else:
        parameters = workoutRoutine

    workout = parameters[0]
    rest = parameters[1]
    interval = parameters[2]

    play_clip.begin()

    mins = int(workout)
    secs = 0
    switch = 0

    print("\n")

    while (mins + secs > 0):


        try:
            sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=mins, seconds=secs))
            sys.stdout.flush()
            time.sleep(1)

            #
            if mins == 0:
                secs -= 1
                if secs == 0:
                    print("\n\nComplete!\n")
                    play_clip.complete()

            if mins == 1:
                if secs == 0:
                    secs = 59
                    mins = 0
                elif secs > 0:
                    secs -= 1

            if mins != 1 and mins != 0:
                if secs == 0:
                    mins -= 1
                    secs = 59
                elif secs > 0:
                    secs -= 1


            if (switch == interval):

                play_clip.rest()

                print("\n\nRest\n")
                countDown = rest
                switch = 0

                while (countDown > 0):
                    try:
                        sys.stdout.write("\r{rest}".format(rest=countDown))
                        sys.stdout.flush()
                        time.sleep(1)
                        countDown -= 1

                        if (countDown == 0):

                            sys.stdout.write("\r{rest}".format(rest=countDown))
                            sys.stdout.flush()
                            print("\n\nBegin\n")
                            play_clip.intervalStart()

                    except KeyboardInterrupt:
                        break
            switch += 1

        except KeyboardInterrupt:
            break
