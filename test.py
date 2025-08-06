'''
Jake Kostenko
Testing module for voice recognition project
'''
import os
import speech_recognition as sr

r = sr.Recognizer()
#r.dynamic_energy_threshold = True
r.pause_threshold = 0.8

with sr.Microphone(device_index=1) as mic:
    print("listening...")
    audio = r.listen(mic)
print("done listening!")

# testing sphinx
try:
    print("Sphinx result: ", r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("unable to transcribe thru sphinx")
except sr.RequestError as e:
    print("error: {0}".format(e))

# SEEMS QUITE UNRELIABLE AND SLOW!!!
'''
#vosk testing
try:
    print("Vosk result: ", r.recognize_vosk(audio))
except sr.UnknownValueError:
    print("unable to transcribe thru whisper")
except sr.RequestError as e:
    print("error: {0}".format(e))
'''

# testing whisper
try:
    print("Whisper result: ", r.recognize_whisper(audio, language="english"))
except sr.UnknownValueError:
    print("unable to transcribe thru whisper")
except sr.RequestError as e:
    print("error: {0}".format(e))
