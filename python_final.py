# -*- coding: utf-8 -*-

import speech_recognition as sr
import mechanize

#cookie
cj = mechanize.CookieJar()

#browser 建立一個browser的物件
br = mechanize.Browser()

#options
#br.set_handle_equiv(True)
#br.set_handle_gzip(True)
#br.set_handle_redirect(True)
#br.set_handle_referer(True)
br.set_handle_robots(False) #有些網站會禁止機器人瀏覽，忽視它



#debug 除錯的設定 
br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)


br.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]

#cookie
br.set_cookiejar(cj)

br.open("https://m.facebook.com/")

br.select_form(nr = 0)

#抓取表單訊息
for form in br.forms():
	print "Form name",form.name
	print form

br.form['email'] = "johnson960095@kimo.com"
#br.select_form(name = "pass")
br.form['pass'] = 'johnson840218'

br.submit()

r = sr.Recognizer()
sr.energy_threshold = 4000
with sr.Microphone() as source:
	audio = r.listen(source)
print("Say something please.")
	
try:
	result = r.recognize_google(audio)
	print("You said %s"%result)
	br2 = mechanize.Browser()

#options
	#br2.set_handle_equiv(True)
	#br.set_handle_gzip(True)
	#br2.set_handle_redirect(True)
	#br2.set_handle_referer(True)
	br2.set_handle_robots(False)


#debugging?
	br2.set_debug_http(True)
	br2.set_debug_redirects(True)
	br2.set_debug_responses(True)

	br2.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')]

#cookie
	br2.set_cookiejar(cj)

	r = br2.open("https://m.facebook.com/")

	for form in br2.forms():
		print "Form name",form.name
		print form
	
	br2.select_form(nr = 1)

	br2.form['xc_message'] = "%s"%result
	#post_message = br.submit()
	#post_check = post_message.read()
	#br2.submit()
	submit_response = br2.submit(name='view_post')
	
	

except sr.UnknownValueError:
	print("Enable to recognize the audio file.")