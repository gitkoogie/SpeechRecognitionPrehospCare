import speech_recognition as sr

r = sr.Recognizer()

# list all available input devices
print(sr.Microphone.list_microphone_names())

mic = sr.Microphone() # device_index = 1

# lets capture some input
print("lets capture some sound")

# here we can also use the r.adjust_for_ambient_noise(source) (default 1 second capture duration)
# before r.listen(source) to capture surrounding noise first
with mic as source:
    audio = r.listen(source)

# recognize it
print(r.recognize_sphinx(audio))
