# coding : utf - 8 -*-
import speech

while True:
    phrase = speech.input()
    speech.say("You said %s" %phrase)
    print phrase
    