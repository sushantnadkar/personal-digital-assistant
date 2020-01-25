import re
import wikipedia

from speech.tts import speak


def define(subject):
	words = subject.split()
	words.remove("define")
	subject = " ".join(words)

	try:
		wiki_data = wikipedia.summary(subject, sentences = 5)

		regex = re.compile(r"([^\(]*)\([^\)]*\) *(.*)")
		m = regex.match(wiki_data)
		while m:
			wiki_data = m.group(1) + m.group(2)
			m = regex.match(wiki_data)
		
		wiki_data = wiki_data.replace("'", "")
		print("Defination of " + subject + ":\n" + wiki_data)
		speak(wiki_data)
	except wikipedia.exceptions.DisambiguationError as e:
		print("Can you please be more specific? You may choose from the following: {0}".format(e))
		speak("Can you please be more specific?")

