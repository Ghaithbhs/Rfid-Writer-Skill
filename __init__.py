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
        fullname = self.get_response('what\'s the full name of the employee')
        job = self.get_response('what\'s the job title of the employee')
        try:
            self.speak("Now place your tag on the reader to write the information you added")
            reader.write(fullname,  job)
            self.speak_dialog("writing.successful", data={'name': fullname})
        finally:
            GPIO.cleanup()


def create_skill():
    return RfidWriter()
