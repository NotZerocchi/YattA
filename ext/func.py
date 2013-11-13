from api import *
from util import *
import time
import sys

def tl(limit=3):
	try:
		home = api.statuses.home_timeline()
		for x in range(0,limit):
			txt = home[x]['text']
			usr = home[x]['user']['name'], "(@" + home[x]['user']['screen_name'] + ")\n"
			usr = " ".join(usr)
			tw(usr)			
			tw(txt)
			print "\n"
			time.sleep(0.5)
	except TwitterHTTPError:
		tw("Rate limit exceeded.\n")

def tweet(text):
	try:
		api.statuses.update(status=text)
		time.sleep(2)
		print "Tweet sent!"
	except:
		print "Failed to send your tweet. Please try again."
		pass

def mention(limit=1):
	try:
		home = api.statuses.mentions_timeline()
		for x in range(0,limit):
			txt = home[x]['text']
			usr = home[x]['user']['name'], "(@" + home[x]['user']['screen_name'] + ")\n"
			usr = " ".join(usr)
			tw(usr)
			tw(txt)
			print "\n"
			time.sleep(0.5)
	except:
		pass

def view(idnum):
	try:
		home = api.statuses.oembed(_id=id)
		print home['user']['screen_name']
		print home['text']
	except:
		pass

def stream():
	tweet_iter = stream.statuses.sample()
	for tweet in tweet_iter:
		if tweet.get('text'):
			print tweet['text']