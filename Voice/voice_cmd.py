import os
import json
import vosk
import pyaudio
from threading import Thread  # Importing the Thread class for creating threads
import time

# Define the path to the Vosk model and the sample rate
MODEL_PATH = "/vosk-model-small-en-us-0.15"  # Update with actual path
SAMPLE_RATE = 16000

# Initialize the Vosk recognizer with the provided model
vosk.SetLogLevel(-1)  # Disable log messages (optional)
model = vosk.Model(MODEL_PATH)
recognizer = vosk.KaldiRecognizer(model, SAMPLE_RATE)

# Initialize PyAudio for audio input
audio = pyaudio.PyAudio()

# Find the index of the default PulseAudio microphone
mic_index = None
for i in range(audio.get_device_count()):
    info = audio.get_device_info_by_index(i)
    if "pulse" in info["name"].lower() and info["maxInputChannels"] > 0:
        mic_index = i
        break

if mic_index is None:
    print("No PulseAudio microphone found. Please ensure one is connected and try again.")
    exit()

# Open a stream from the microphone
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=SAMPLE_RATE, input=True,
                    input_device_index=mic_index, frames_per_buffer=2048)

# Initialize Pluto object for controlling the drone
my_pluto = pluto()

# Main loop for speech recognition
while True:
    data = stream.read(2048)  # Read audio data from the stream
    if len(data) == 0:
        break  # Stop if no data is received

    # Feed the audio data to the recognizer
    if recognizer.AcceptWaveform(data):
        result = json.loads(recognizer.Result())
        text = result['text'].lower()  # Convert recognized text to lowercase for case insensitivity
        print("Recognized:", text)

        # Execute drone commands based on recognized speech
        if "start" in text:
            my_pluto.arm()
        elif "stop" in text:
            my_pluto.disarm()
        elif "take off" in text:
            my_pluto.take_off()
        elif "land" in text:
            my_pluto.land()
        elif "up" in text:
            my_pluto.increase_height()
        elif "down" in text:
            my_pluto.decrease_height()
        elif "forward" in text:
            my_pluto.forward()
        elif "back" in text:
            my_pluto.backward()
        elif "left" in text:
            my_pluto.left()
        elif "right" in text:
            my_pluto.right()
        elif "yes" in text:
            my_pluto.left_yaw()
        elif "no" in text:
            my_pluto.right_yaw()
    else:
        result = json.loads(recognizer.PartialResult())
        text = result['partial'].lower()  # Convert partial text to lowercase for case insensitivity
        print("Partial:", text)

# Close the audio stream and PyAudio
stream.stop_stream()
stream.close()
audio.terminate()
