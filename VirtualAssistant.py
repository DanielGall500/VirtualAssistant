import speech_recognition as sr
import easygui as gui
import pyttsx
import Tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):

		tk.Frame.__init__(self, master)

		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.text_output = tk.Text(self)
		self.text_output.grid()

		self.begin_button = tk.Button(self, text='Begin Assistance')
		self.begin_button.grid()

app = Application()

app.master.title('Virtual Assistant')

app.mainloop()


def listen():
	rec = sr.Recognizer()

	with sr.Microphone() as mic_input:
		print 'listening'
		audio_input = rec.listen(mic_input)

