from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft import MycroftSkill, intent_file_handler
import json
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()



class login(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_handler(IntentBuilder("").require("querry"))
    def handle_login(self):
        name = self.settings.get("name")
        family_name = self.settings.get("fname")
        email = self.settings.get("email")
        num = self.settings.get("num")
        try:
            print("Now place your tag to write")
            reader.write(name, family_name, email, num)
            print("Written")
        finally:
            GPIO.cleanup()


def create_skill():
    return login()
