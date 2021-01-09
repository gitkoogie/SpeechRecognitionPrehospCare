# guide https://realpython.com/python-speech-recognition/

import speech_recognition as sr
print(sr.__version__)

print("Correct Text -------------")
str = "the stale smell of old beer lingers it takes heat to bring out the odor a cold dip restores health and zest a salt pickle taste fine with ham tacos al Pastore are my favorite a zestful food is be hot cross bun"
print(str)
print("---------------------------")

r = sr.Recognizer()

#r.recognize_google()

harvard = sr.AudioFile('audiofiles/harvard.wav')

# can use offset (start later in voice file) and duration (seconds to capture)
with harvard as source:
    audio = r.record(source)

# convert harvard audio to text
#print(r.recognize_google(audio))

# some noisy audiofiles
jackhammer = sr.AudioFile('audiofiles/jackhammer.wav')
with jackhammer as source:
    audio = r.record(source)

#print(r.recognize_google(audio))

# adjust for ambient noise
# can alsouse duration (to only capture ambient noise in first X seconds)
with jackhammer as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

# set "show_all" parameter to show all transcripts, the one most likely
# is always returned by default

#print(r.recognize_google(audio))
