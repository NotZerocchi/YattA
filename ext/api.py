import tweepy
from twitter import *
import webbrowser
import os
import time

def gettoken():

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	try:
		webbrowser.open(auth.get_authorization_url())
		time.sleep(2)
	except tweepy.TweepError:
		print "Failed to request token. Request here: " + auth.get_authorization_url()

	verifier = raw_input("Enter the pin here: ").strip()

	try:
		auth.get_access_token(verifier)
	except:
		print "Failed to get access token."

	oauth_token = auth.access_token.key
	oauth_token_secret = auth.access_token.secret

	token = open("token.txt",'w')
	token.write(oauth_token)
	token.write("\n")
	token.write(oauth_token_secret)
	token.close()

	return oauth_token, oauth_token_secret

consumer_key = "scMhZpaXu5dJ8T6zak3Q"
consumer_secret = "ykMQ49YB8Mk5lTs6AN0UWiUALFKdpuN0pECMgeDaOkg"
 
if not os.path.exists("token.txt"):
	oauth_token, oauth_token_secret = gettoken()
else:
	token = open("token.txt",'r')
	token.seek(0)
	check = token.read(1)
	if not check:
		oauth_token, oauth_token_secret = gettoken()
	else:
		token.seek(0)
		oauth_token = token.readline()
		oauth_token_secret = token.readline()
	token.close()

api = Twitter(
	auth=OAuth(oauth_token, oauth_token_secret,
	consumer_key, consumer_secret)
)

stream = TwitterStream(
	auth=OAuth(oauth_token, oauth_token_secret,
	consumer_key, consumer_secret)
)