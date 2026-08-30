import pyaudio, wave, threading
import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt

rate = 16000
chunk = 1024
format = pyaudio.paInt16
filename = input("Enter file name: ") + ".wav"

p = pyaudio.PyAudio()
stream = p.open(format=format, channels=1, rate=rate,
                input=True, frames_per_buffer=chunk)

frames = []
stop = False

def stop_recording():
    global stop
    input("\nPress Enter to stop...")
    stop = True

threading.Thread(target=stop_recording).start()
print("Recording...")

while not stop:
    frames.append(stream.read(chunk))

stream.stop_stream()
stream.close()

with wave.open(filename, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b"".join(frames))

p.terminate()
print("Recording saved!")

r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio = r.record(source)

try:
    print("Transcription:", r.recognize_google(audio))
except:
    print("Could not transcribe!")

samples = np.frombuffer(b"".join(frames), dtype=np.int16)
time = np.arange(len(samples)) / rate

print("Maximum:", np.max(samples))
print("Minimum:", np.min(samples))
print("Peak:", np.max(np.abs(samples)))
print("Average:", round(np.mean(np.abs(samples)), 2))

plt.plot(time, samples)
plt.title("Audio Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()