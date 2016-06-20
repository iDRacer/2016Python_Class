# -*- coding: utf-8 -*-
import speech
import win32com.client
import webbrowser, sys, os
#import pygsr

#speech = Pygsr()
#speech.record(3)
#phrase, complete_respose = speech.speech_to_text('zh_TW')
	
def callback(phrase, listener):
    print(": %s"%phrase)
    if phrase == 'music':
        speech.say("Opening Youtube")
        webbrowser.open_new("https://www.youtube.com/?hl=zh-TW&gl=TW")
        sys.exit()
		
listener = speech.listenforanything(callback)
while listener.islistening():
	text = input()
	speech.say(text)