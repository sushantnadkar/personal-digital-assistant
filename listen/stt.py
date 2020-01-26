import speech_recognition as sr

from speech.tts import speak


def to_text():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Am listening!")
		audio = r.listen(source)

	try:
		speech_text = r.recognize_google(audio).lower().replace("'", "")
		print("I thinks you said: " + speech_text)
		speak("I thinks you said: " + speech_text)
		return speech_text
	except sr.UnknownValueError:
		print("Sorry, I could not understand the audio")
		speak("Sorry, I could not understand the audio")
		to_text()
	except sr.RequestError as e:
		print("Sorry, I ran into an error; {0}".format(e))
		speak("Sorry, I ran into an error; {0}".format(e))
		to_text()
