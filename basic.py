import sys
sys.path.append("ext")
import os
#import readline
from util import *
from cond import cond

cls()

opt = []

def inp():
	bool = True
	txt = raw_input("> ")
	while bool:
		try:
			opt = cmd(txt)
			if "exit" in opt:
				bool = False
				break
			else:
				cond(opt)
		except:
			pass
		del opt[:]
		bool = True
		txt = raw_input("> ")	
	print "Bye!"

inp()
