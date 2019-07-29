from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler
import json
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


class RfidWriter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('query.intent')
    def handle_login(self):
        info = []
        text = self.get_response('what\'s the full name of the employee')
        info.append(text)
        try:
            self.speak("Now place your tag on the reader to write the information you added")
            reader.write(info)
            self.speak_dialog("writing.successful", data={'name': text})
        finally:
            GPIO.cleanup()


def create_skill():
    return RfidWriter()
