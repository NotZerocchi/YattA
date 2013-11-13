import os
from util import *
from func import *

def cond(opt):
	if "n0l" in opt:
		print "You didn't enter any text!"
	if "tl" in opt[0]:
		os.system('clear')
		limit = content(opt,"tl")
		if limit != "":
			tl(int(limit))			
		else:
			tl()
	elif "stream" in opt[0]:
		os.system('clear')
		stream()
	elif "mention" in opt[0]:
		os.system('clear')
		limit = content(opt,"mention")
		if limit != "":
			mention(int(limit))			
		else:
			mention()
	elif "id" in opt[0]:
		idnum = content(opt,"id")
		if idnum == "":
			print "You didn't enter an id"
			pass		
		else:
			view(idnum)
	else:
		text = final(opt)
		tweet(text)