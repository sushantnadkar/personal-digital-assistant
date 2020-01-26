import io
import random
import re
import string
import warnings
import nltk
import wikipedia
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from speech.tts import speak
from listen.stt import to_text

warnings.filterwarnings('ignore')

nltk.download('popular', quiet=True)

# uncomment the following only the first time
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only


def define(subject, cli):
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
		print("Do you have any more question? (y/N)")
		speak("Do you have any more question?")
		if cli == "true":
			reply = input().lower()
		else:
			reply = to_text()
		set(["yes"]).issubset(set(reply.split()))
		if set(["yes"]).issubset(set(reply.split())) or set(["sure"]).issubset(set(reply.split())) or reply == "y":
			init_chat(subject, cli)

	except wikipedia.exceptions.DisambiguationError as e:
		print("Can you please be more specific? You may choose from the following: {0}".format(e))
		speak("Can you please be more specific?")


def init_chat(subject, cli):

	raw = wikipedia.page(subject).content.replace("'", "").replace("\n", " ").replace("=", "")

	#TOkenisation
	sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
	word_tokens = nltk.word_tokenize(raw)# converts to list of words

	# Preprocessing
	lemmer = WordNetLemmatizer()
	def LemTokens(tokens):
		return [lemmer.lemmatize(token) for token in tokens]
	remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
	def LemNormalize(text):
		return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


	# Keyword Matching
	GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
	GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

	def greeting(sentence):
		"""If user's input is a greeting, return a greeting response"""
		for word in sentence.split():
			if word.lower() in GREETING_INPUTS:
				return random.choice(GREETING_RESPONSES)


	# Generating response
	def response(user_response):
		robo_response=''
		sent_tokens.append(user_response)
		TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
		tfidf = TfidfVec.fit_transform(sent_tokens)
		vals = cosine_similarity(tfidf[-1], tfidf)
		idx=vals.argsort()[0][-2]
		flat = vals.flatten()
		flat.sort()
		req_tfidf = flat[-2]
		if(req_tfidf==0):
			robo_response=robo_response+"Sorry! I don't understand you"
			return robo_response
		else:
			robo_response = robo_response+sent_tokens[idx]
			return robo_response

	def chat(subject):
		flag=True
		print("> What more queries do you have about " + subject + "?. If you want to exit, type Bye!")
		speak("What more queries do you have about " + subject + "?. If you want to exit, say Bye!")

		while(flag==True):
			if cli == "true":
				user_response = input()
				user_response=user_response.lower()
			else:
				user_response = to_text()

			if(user_response!='bye'):
				if(user_response=='thanks' or user_response=='thank you' ):
					flag=False
					print("> You are welcome..")
					speak("You are welcome.")
				else:
					if(greeting(user_response)!=None):
						reply_text = greeting(user_response)
						print("> " + reply_text)
						speak(reply_text)
					else:
						reply_text = response(user_response)
						print("> ",end="")
						print(reply_text)
						speak(reply_text)
						sent_tokens.remove(user_response)
			else:
				flag=False
				print("> Bye! take care..")
				speak("Bye! take care.")
	chat(subject)
