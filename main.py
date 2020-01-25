import sys
import yaml
import speech_recognition as sr

from brain import brain
from speech.tts import speak


profile = open("profile.yaml")
profile_data = yaml.safe_load(profile)
profile.close()

speak("Welcome" + name + ", systems are now ready to run. How may i help you?")

def main():
	r = sr.Recognizer() 
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)

	try:
		speech_text = r.recognize_google(audio).lower().replace("'", "")
		print("Google thinks you said: " + speech_text)
	except sr.UnknownValueError:
		print("Google could not understand audio")
	except sr.RequestError as e:
		print("Google error; {0}".format(e))

	brain(speech_text, **kwargs)

main()