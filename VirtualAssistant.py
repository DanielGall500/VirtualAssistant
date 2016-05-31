import speech_recognition as sr
import easygui as gui
import Tkinter as tk
import os
import webbrowser
import pyttsx

class Application(tk.Frame):
	def __init__(self, master=None):

		tk.Frame.__init__(self, master)

		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.text_output = tk.Text(self)
		self.text_output.grid()

		self.begin_button = tk.Button(self, text='I Need Assistance')
		self.begin_button.grid()

app = Application()

app.master.title('Virtual Assistant')

app.mainloop()


def listen_response(recognizer):
	speech_output = ""
	
	with sr.Microphone() as mic_input:
		print 'listening'
		audio = recognizer.listen(mic_input)
		speech_output = recognizer.recognize_google(audio)

		if 'jam' in speech_output:

			print 'Yes, Daniel?'
			engine = pyttsx.init()

			engine.say('Yes, Daniel?')

			engine.runAndWait()

			audio = recognizer.listen(mic_input)
			speech_output = recognizer.recognize_google(audio)

			try:
				return speech_output
			except sr.UnknownValueError:
				return "Didn't quite catch that"
			except sr.RequestError:
				return "I don't fully understand"

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
speech = listen_response(r)

engine = pyttsx.init()

engine.say('Will do that now for you, Daniel')

engine.runAndWait()

parse_speech(speech, app_dirs, websites)































