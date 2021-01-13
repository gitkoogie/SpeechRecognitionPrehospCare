# Speech Recognition for ABCDE protocol

## Installation guide (Getting started)

*Install Ubuntu 64 but NORMAL installation (includes python3)*

1. Install pip
sudo apt install python3-pip

2. Install atom
sudo snap install atom

3. Install SpeechRecognition
pip3 install SpeechRecognition

4. Install pyAudio
sudo apt-get install python3-pyaudio

**You are now able to write speech recognition programs using the SpeechRecognition library, your microphone and Google API. (You might see some debug messages when creating the "Microphone" instance but do not worry**

## For using sphinx(offline) speech recognition

1. Install setuptools and wheel
python3 -m pip install --upgrade pip setuptools wheel

2. Install swig
sudo apt-get update -y
sudo apt-get install -y swig

3. Install libpulse
sudo apt-get install libpulse-dev

4. Install libsound
sudo apt-get install libsound2-dev

5. Install pocketsphinx (lightweight sphinx version)
pip3 install --upgrade pocketsphinx

**You should now be able to run recognize_sphinx in the SpeechRecognition library. You might need to setup your input device accordingly if your program fails to recognize sound**

*For further guides see guides.txt*
