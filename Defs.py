import string, threading, random

from templates import *
from collections import deque

emotesFile = "emotes.txt"

queue=deque([], maxlen=50)

wordDict = {}
emotesList = []

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line):
	separate = line.split(":", 2)
	try:
		message = separate[2]
		return message
	except Exception, e:
		print("error condition")
		return " "
def PONG(s):
	s.send(bytes('PONG :tmi.twitch.tv\r\n'))
	threading.Timer(300, PONG).start()

def createEmotes():
    global emotesList
    f = open(emotesFile, 'r')
    str = f.readline()
    while str :
        str = str[:-1]
        emotesList.append(str)
        str = f.readline()
    f.close()

# Fills queue with messages. Once filled pushes and pops.
def fillQueue(msg):
	queue.append(msg)

def addNew(msg):
	global wordDict
	words = msg.split()
	for word in words:
		try:
			if (wordDict[word.lower()]):
				wordDict[word.lower()] += 1
			elif(wordDict[word]):
				wordDict[word] += 1
		except Exception, e:
			if(len(word) >= 4 and len(word) <10 and word not in emotesList):
				wordDict[word.lower()] = 1
			elif(len(word) >= 4 and len(word) <10):
				wordDict[word] = 1

# Do the cool thing (puts smaller functions together)
def cmdSillySentence():
	global madlib_list
	global chatKey
	global wordDict

	sentence = ""

	q_len = len(queue)

	while(q_len > 0):
		message=queue.popleft() 
		addNew(message) 
		queue.append(message) 
		q_len -= 1 

	mad=random.choice(madlib_list)
	madWords=mad.split()

	for word in madWords:
		if chatKey in word:
			if not wordDict:
				return ""
			tempWord=max(wordDict,key=wordDict.get)
			sentence+=" " + tempWord
			del(wordDict[tempWord])
		else:
			sentence+=" " + word

	print("-------->" + sentence)
	wordDict.clear()
	return sentence
