import random

from speech.tts import speak


def who_are_you():
	replies = ["I am Natasha, your lovely personal assistant.", "Natasha, didnt I tell you before?", "You ask that so many times! I am Natasha"]
	reply = random.choice(replies)
	print(reply)
	speak(reply)

def how_am_i():
	replies = ["You are goddamn handsome!", "My knees go weak when I see you.", "You are sexy!", "You look like the kindest person that I have met."]
	reply = random.choice(replies)
	print(reply)
	speak(reply)

def tell_joke():
	jokes = ['What happens to a frogs car when it breaks down? It gets toad away.', 'Why was six scared of seven? Because seven ate nine.', 'No, I always forget the punch line.'] 
	reply = random.choice(jokes)
	print(reply)
	speak(reply)

def who_am_i(name): 
	reply = "You are " + name + ", a brilliant person. I love you!"
	print(reply)
	speak(reply)

def where_born():
	reply = 'I was created by a magician named Sushant, in India, the magical land of Himalayas.'
	print(reply)
	speak(reply)

def how_are_you():
	reply = 'I am fine, thank you.'
	print(reply)
	speak(reply)

def undefined():
	reply = "Sorry, I dont know what that means!"
	print(reply)
	speak(reply)
