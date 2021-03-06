from modules import general_conversation, tell_time, openweather, wiki


def brain(speech_text, **profile_data):
	def check_message(check):
		"""
		This function checks if the items in the list (specified in the arguments) are present in the user's input speech.
		"""

		words_of_message = speech_text.split()
		if set(check).issubset(set(words_of_message)):
			return True
		else:
			return False

	if check_message(["who", "are", "you"]):
		general_conversation.who_are_you()
	elif check_message(["how", "i", "look"]) or check_message(["how", "am", "i"]):
		general_conversation.how_am_i()
	elif check_message(["tell", "joke"]):
		general_conversation.tell_joke()
	elif check_message(["who", "am", "i"]):
		general_conversation.who_am_i(profile_data["name"])
	elif check_message(["where", "born"]):
		general_conversation.where_born()
	elif check_message(["how", "are", "you"]):
		general_conversation.how_are_you()
	elif check_message(["what", "time"]) or check_message(["whats", "time"]):
		tell_time.what_is_time()
	elif check_message(["what", "weather"]) or check_message(["whats", "weather"]) or check_message(["how", "weather"]) or check_message(["hows", "weather"]):
		openweather.what_weather(profile_data["location"], profile_data["api"]["openweather_key"])
	elif check_message(["define"]):
		wiki.define(speech_text, profile_data["is_cli"])
	else:
		general_conversation.undefined()
