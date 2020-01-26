import speech_recognition as sr


def to_text():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)

	try:
		speech_text = r.recognize_google(audio).lower().replace("'", "")
		print("Google thinks you said: " + speech_text)
		return speech_text
	except sr.UnknownValueError:
		print("Google could not understand audio")
		to_text()
	except sr.RequestError as e:
		print("Google error; {0}".format(e))
		to_text()
