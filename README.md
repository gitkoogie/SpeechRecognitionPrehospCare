# Speech Recognition for ABCDE protocol

## Installation guide (Getting started)

IF you want Ubuntu as main Operating system
*Install Ubuntu 64 but NORMAL installation (includes python3)*
ELSE IF you want ubuntu on a virtual machine
*Install Virtualbox and Ubuntu on the virtual machine*
ELSE IF you use macbook 
*you can install python3 and (probably) follow the guide below*
ELSE
*you use windows and in which you will need to install a terminal etc*


### Install pip
sudo apt install python3-pip

### Install atom
sudo snap install atom

### Install SpeechRecognition
pip3 install SpeechRecognition

### Install pyAudio
sudo apt-get install python3-pyaudio

**You are now able to write speech recognition programs using the SpeechRecognition library, your microphone and Google API. (You might see some debug messages when creating the "Microphone" instance but do not worry**

## For using sphinx(offline) speech recognition

### Install setuptools and wheel
python3 -m pip install --upgrade pip setuptools wheel

### Install swig
sudo apt-get update -y
sudo apt-get install -y swig

### Install libpulse
sudo apt-get install libpulse-dev

### Install libsound
sudo apt-get install libsound2-dev

### Install pocketsphinx (lightweight sphinx version)
pip3 install --upgrade pocketsphinx

**You should now be able to run recognize_sphinx in the SpeechRecognition library. You might need to setup your input device accordingly if your program fails to recognize sound**

*For further guides see sources.txt*
