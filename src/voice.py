
import speech_recognition
import subprocess


class VoiceInput(object):

    def __init__(self, **kwargs):
        # Allow different speech recognition methods to be selected
        # See https://pypi.python.org/pypi/SpeechRecognition/
        self.recognizer_function = 'recognize_sphinx'

        # Start jack control
        self.attempt_jack_control_start()

    def get_input(self):
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        recognizer_function = getattr(recognizer, self.recognizer_function)

        try:
            result = recognizer_function(audio)
            return result
        except speech_recognition.UnknownValueError:
            return 'I am sorry, I could not understand that.'
        except speech_recognition.RequestError as e:
            m = 'My speech recognition service has failed. {0}'
            return m.format(e)

    def attempt_jack_control_start(self):
        """
        Jack is a program that can be used to get audio
        input from your system. This command will try
        to start it when your program runs.
        """
        try:
            subprocess.call(['jack_control', 'start'])
        except Exception:
            # Note: jack_control is not a valid command in Windows
            warnings.warn(
                'Unable to start jack control.',
                RuntimeWarning
            )


class VoiceOutput(OutputAdapter):

    def __init__(self, **kwargs):
        super(VoiceOutput, self).__init__(**kwargs)

        import platform

        self.platform = platform.system().lower()

    def speak(self, statement):
        import time

        if self.platform == 'darwin':
            # Use Mac's built-in say command to speak the response
            cmd = ['say', str(statement.text)]

            subprocess.call(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )

            return statement.text

        from espeak import espeak
        from espeak import core as espeak_core

        done_synth = [False]

        def synth_callback(event, pos, length):
            if event == espeak_core.event_MSG_TERMINATED:
                done_synth[0] = True

        espeak.set_SynthCallback(synth_callback)
        call_result = espeak.synth(statement)

        # Wait for the speech to stop
        while call_result and not done_synth[0]:
            time.sleep(0.05)

        return call_result

    def process_response(self, statement, confidence=None):
        self.speak(statement.text)
        return statement