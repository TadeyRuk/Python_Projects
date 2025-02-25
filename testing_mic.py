import time
import webbrowser
import pyautogui
import whisper
import sounddevice as sd
import numpy as np

model = whisper.load_model("base")

def send_a_msg ():
    webbrowser.open("https://www.facebook.com/messages/e2ee/t/7418173101605052")
    time.sleep(10)
    pyautogui.write("Hi, This is my first Siri-like automation", interval=0.2)
    pyautogui.press("enter")

def listen_for_command():
    print("Say something bai....")

    samplerate = 16000 #16khz

    duration = 5
    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1, dtype=np.float32)
    sd.wait()

    audio = audio.flatten()

    result = model.transcribe(audio)

    command = result["text"].lower()

    if "send my message" in command:
        send_a_msg()
    else:
        print("No commands for that request bai. Try again")

while True:
    listen_for_command()


