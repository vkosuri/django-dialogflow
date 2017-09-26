#!/usr/bin/env python

# NOTE: this example requires PyAudio because it uses the Microphone class
# If you stuck with any erros try to install these pacakges
# sudo apt-get install libjack-jackd2-dev portaudio19-dev
# sudo apt-get install jackd2
# First you need to kill the existing pulseaudio process,
# start the jack_control process and re-start the pulseaudio process.
# Please use the below commands:
# pulseaudio --kill
# jack_control start
# jack_control exit
# pulseaudio --start
# For more information See https://pypi.python.org/pypi/SpeechRecognition/

import speech_recognition


def attempt_jack_control_start():
    """
    Jack is a program that can be used to get audio
    input from your system. This command will try
    to start it when your program runs.
    """
    import subprocess
    import warnings
    try:
        subprocess.call(['jack_control', 'start'])
    except Exception:
        # Note: jack_control is not a valid command in Windows
        warnings.warn(
            'Unable to start jack control.',
            RuntimeWarning
        )

recognizer_function = 'recognize_sphinx'

# Start jack control
# print("Jack control about to start")
# # attempt_jack_control_start()
# print("Jack control started")
#
# print("Lising default devices")
# for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

recognizer = speech_recognition.Recognizer()
print("Starting Microphone")
with speech_recognition.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Speak something")
    audio = recognizer.listen(source)
    print("Speech recognized")

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + recognizer.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

