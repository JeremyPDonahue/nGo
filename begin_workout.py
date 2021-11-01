import sys
import time
import set_parameters
from playsound import playsound

def beginWorkout():

    parameters = set_parameters.setParameters()
    workout = int(parameters[0])
    rest = int(parameters[1])
    interval = int(parameters[2])

    playsound("audio/Get_Ready.wav")
    playsound("audio/mario.wav")
    playsound("audio/Begin.wav")

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
                    playsound("audio/mario.wav")

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

                playsound('audio/Rest.wav')

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
                            playsound('audio/Begin.wav')

                    except KeyboardInterrupt:
                        break
            switch += 1

        except KeyboardInterrupt:
            break
