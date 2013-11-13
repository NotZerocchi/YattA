import sys
import os
sys.path.append("ext")
import time

opt = []

def cmd(txt):
	spl = txt.split()
	for word in spl:
		opt.append(word)
	return opt

def content(opt, key):
	keyword = opt[opt.index(key) + 1:]
	keyword = " ".join(keyword)
	return keyword

def final(opt):
	keyword = opt[:]
	keyword = " ".join(keyword)
	return keyword

def tw(txt, sl=0.03):
	for letters in txt:
				sys.stdout.write(letters)
				sys.stdout.flush()
				time.sleep(sl)

def cls():
    return os.system('cls' if os.name == 'nt' else 'clear')