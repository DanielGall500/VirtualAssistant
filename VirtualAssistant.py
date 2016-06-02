import speech_recognition as sr
import os
import webbrowser
import pyttsx
import time

img_file = "C:/Users/dano/Desktop/Theory of Everything/AIBRAIN.jpg"

def output_assist(text):
	print text
	engine.say(text)
	engine.runAndWait()

def mic_input(r):
	with sr.Microphone() as mic_input:
		audio = r.listen(mic_input)
		speech_output = r.recognize_google(audio)
	return speech_output

def waitForCommand():
	assistance = ''
	while 'yes' not in assistance:
		assistance = raw_input('Activate Command?(yes/no)')
	return True

def listen_response(recognizer, engine, name):
		yes = 'How can I be of assistance, {}?'.format(name)
		output_assist(yes)

		command = mic_input(recognizer)

		try:
			affirm = 'Will Do That For You Now, {}'.format(name)
			output_assist(affirm)
			return command
		except sr.UnknownValueError:
			unknown = "Didn't quite catch that"
			output_assist(unknown)
		except sr.RequestError:
			misunderstand = "I don't fully understand"
			output_assist(misunderstand)

def open_applications(apps_to_open, app_dirs):
	for app in apps_to_open:
		os.startfile(app_dirs[app])

def parse_speech(speech, app_dirs, websites):
	speech = speech.lower()

	for word in speech.split(' '):
		if word == 'open':
			[os.startfile(app_dirs[app]) for app in app_dirs.keys() \
				if app in speech]
		elif word == 'search':
			[webbrowser.open(websites[wbst]) for wbst in websites.keys() \
				if wbst in speech]


app_dirs = {"spotify" : "C:/Users/dano/AppData/Roaming/Spotify/Spotify.exe", "google" : "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe" }
websites = {"youtube" : "https://www.youtube.com/"}

r = sr.Recognizer()
engine = pyttsx.init()

waitForCommand()

welcome = 'Welcome, what is your name?'

engine.say(welcome)
engine.runAndWait()
name = raw_input(welcome + '\n')

for i in range(10): #loops an arbitrary number of times

	speech_output = listen_response(r, engine, name)

	parse_speech(speech_output, app_dirs, websites)

	waitForCommand()
































