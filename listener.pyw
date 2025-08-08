# ----------------------------------NOTES------------------------------------------------------------
# .pyw allows the script to run in the background and detect it in general
# Slow start because it's a big trained model, only slow on start
# very basic and not 100% accurate on the words it picks up. However, it does a good job when up close.
# ----------------------------------------------------------------------------------------------------

import keyboard, threading, commands, sounddevice as sd, queue, sys, json, os
from vosk import Model, KaldiRecognizer


model = Model(r"offline_model/model")
q = queue.Queue()

listening_thread = None
stop_listening = None

def listen_model():
    global stop_listening
    stream = sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',channels=1, callback=callback)

    with stream:
        print("🎤 Say something...")

        rec = KaldiRecognizer(model, 16000)


        while True:

            if stop_listening == True:
                print("🛑 Stopped listening.")
                result = json.loads(rec.FinalResult())
                text = result.get("text", "").strip()
                if text:
                    print("📝 Final result:", text)
                    commands.commands(text)
                break

            try:
                data = q.get(timeout=0.1)
            except queue.Empty:
                continue

            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                print("📝 You said:", result.get("text", ""))
                text = result.get("text", "")
                commands.commands(text)
                break


def callback(indata, frame, time, status):
    # Do not touch this it's for the model.
    global q, model
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def on_key_event(event):
    global listening_thread, stop_listening
 # Logic to see when the button is pressed, then does that action based on it.
 # [sub-note: detects the press even outside the script, need to edit to a hotkey.]
    if event.name == 'page up':
        if event.event_type == keyboard.KEY_DOWN:
            if listening_thread is None:
                listening_thread = threading.Thread(target=listen_model)
                listening_thread.start()
                stop_listening = False

        elif event.event_type == keyboard.KEY_UP:
            listening_thread = None
            stop_listening = True


keyboard.hook(on_key_event)


print(f'Hello {os.getlogin()}')
print("➡️ Hold 'page up' to speak.\n➡️ Press 'esc' to exit.")
keyboard.wait('esc')
