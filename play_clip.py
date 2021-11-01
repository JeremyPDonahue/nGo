from playsound import playsound

def begin():
    playsound("audio/Get_Ready.wav")
    playsound("audio/mario.wav")
    playsound("audio/Begin.wav")

def rest():
    playsound('audio/Rest.wav')

def complete():
    playsound("audio/mario.wav")

def intervalStart():
    playsound('audio/Begin.wav')