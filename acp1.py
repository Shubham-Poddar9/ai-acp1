import pyaudio
import wave
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt

rate = 16000
chunk = 1024
frames = []

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate,
                input=True, frames_per_buffer=chunk)

print("Speak now. Press Enter to stop.")

import threading
stop = False

def stop_recording():
    global stop
    input()
    stop = True

threading.Thread(target=stop_recording).start()

while not stop:
    frames.append(stream.read(chunk))

stream.stop_stream()
stream.close()
p.terminate()

data = b"".join(frames)

with wave.open("my_audio.wav", "wb") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(rate)
    f.writeframes(data)

recognizer = sr.Recognizer()
audio = sr.AudioData(data, rate, 2)

try:
    text = recognizer.recognize_google(audio)
    print("Transcription:", text)
except:
    print("Could not understand audio.")

samples = np.frombuffer(data, dtype=np.int16)
time = np.linspace(0, len(samples) / rate, len(samples))

plt.plot(time, samples)
plt.title("Voice Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()