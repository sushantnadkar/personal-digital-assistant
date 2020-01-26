import sys
import yaml
import argparse

from listen.stt import to_text
from brain import brain
from speech.tts import speak


profile = open("profile.yaml")
profile_data = yaml.safe_load(profile)
profile.close()

speak("Welcome" + profile_data["name"] + ", systems are now ready to run. How may i help you?")

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--text", help="Provide text input instade of speech input using microphone.")
	args = parser.parse_args()

	if args.text:
		speech_text = args.text
		print("Your input: " + speech_text)
		brain(speech_text, **profile_data)
	else:
		speech_text = to_text()
		brain(speech_text, **profile_data)

main()