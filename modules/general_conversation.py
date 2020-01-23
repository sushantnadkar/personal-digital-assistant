import random

from speech.tts import speak


def who_are_you():
	replies = ["I am Natasha, your lovely personal assistant.", "Natasha, didnt I tell you before?", "You ask that so many times! I am Natasha"]
	speak(random.choice(replies))

def how_am_i():
	replies = ["You are goddamn handsome!", "My knees go weak when I see you.", "You are sexy!", "You look like the kindest person that I have met."]
	speak(random.choice(replies))

def tell_joke():
	jokes = ['What happens to a frogs car when it breaks down? It gets toad away.', 'Why was six scared of seven? Because seven ate nine.', 'No, I always forget the punch line.'] 
	speak(random.choice(jokes)) 

def who_am_i(name): 
	speak('You are ' + name + ', a brilliant person. I love you!') 

def where_born(): 
	speak('I was created by a magician named Sushant, in India, the magical land of Himalayas.') 

def how_are_you(): 
	speak('I am fine, thank you.')

def undefined():
	speak("Sorry, I dont know what that means!")
