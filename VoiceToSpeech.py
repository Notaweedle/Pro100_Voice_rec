import time

import speech_recognition as sr

#index 1 for my laptop mic
# index

def listen_short():
    r = sr.Recognizer()
    #r.dynamic_energy_threshold = True
    r.pause_threshold = 0.8

    with sr.Microphone(device_index=1) as mic:
        print("listening...")
        audio = r.listen(mic)
    print("done listening!")

    # testing whisper
    try:
        return r.recognize_whisper(audio, language="english")
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        return ""

def listen_long():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    with mic as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(source=mic, callback=callback)
    return stop_listening

def callback(recognizer, audio):
    print("trying to recognize...")
    try:
        print(recognizer.recognize_whisper(audio, language="english"))
        print(recognizer.recognize_sphinx(audio, language="en-US"))
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")

if __name__ == "__main__":
    stop_listening = listen_long()
    print("listening!")

    for i in range(50): time.sleep(0.1)
    stop_listening(True)