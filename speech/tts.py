import os, sys


def speak(text):
	"""
	This function takes `text` as argument and converts it to speech
	"""

	return os.system("espeak -v en+f2 -s 150 '" + text + "'")
