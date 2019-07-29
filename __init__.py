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
        name = self.get_response('what\'s the name of the employee')
        family_name = self.get_response('what\'s the family name of the employee')
        email = self.get_response('what\'s the email of the employee')
        job = self.get_response('what\'s the job title of the employee')
        try:
            self.speak("Now place your tag on the reader to write the information you added")
            reader.write(name, family_name, email, job)
            self.speak_dialog("writing.successful", data={'name': name})
        finally:
            GPIO.cleanup()


def create_skill():
    return RfidWriter()
