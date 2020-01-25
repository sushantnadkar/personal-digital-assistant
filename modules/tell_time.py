from datetime import datetime
from speech.tts import speak


def what_is_time():
	reply = "The time is" + datetime.strftime(datetime.now(), "%H:%M")
	print(reply)
	speak(reply)