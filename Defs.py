import string, threading, random

from templates import *
from collections import deque

emotesFile = "emotes.txt"

queue=deque([], maxlen=100)

wordDict = {}
emotesList = []

def getUser(line):
	separate = line.split(":", 2)
	user = separate[1].split("!", 1)[0]
	return user
def getMessage(line):
	separate = line.split(":", 2)
	message = separate[2]
	return message
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
	chatWords=[]
	chatVals=[]

	sentence = ""

	q_len = len(queue)

	while(q_len > 0):###########
		message=queue.popleft() ###########
		addNew(message) ###########
		queue.append(message) ###########
		q_len -= 1 ###########

	mad=random.choice(madlib_list)
	madWords=mad.split()

	for word in madWords:
		if chatKey in word:
			if not wordDict:
				return ""
			tempWord=max(wordDict,key=wordDict.get)
			sentence+=" " + tempWord
			chatWords.append(tempWord)
			chatVals.append(wordDict[tempWord])
			del(wordDict[tempWord])
		else:
			sentence+=" " + word

		for word in chatWords:
			print(word + " ")
		for val in chatVals:
			print(val)
	print("-------->" + sentence)
	wordDict.clear()
	return sentence
