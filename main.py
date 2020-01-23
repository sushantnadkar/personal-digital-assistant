import sys
import yaml
import speech_recognition as sr 

from speech.tts import speak


profile = open("profile.yaml")
profile_data = yaml.safe_load(profile)
profile.close()

name = profile_data["name"]
location = profile_data["location"]

speak("Welcome" + name + ", systems are now ready to run. How may i help you?")

def main():
	r = sr.Recognizer() 
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)

	try:
		speech_text = r.recognize_sphinx(audio).lower().replace("'", "")
		print("Sphinx thinks you said " + speech_text)
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))

	speak(speech_text)

main()