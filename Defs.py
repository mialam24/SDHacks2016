import string, threading, random

from templates import *
from collections import deque

queue=deque([], maxlen=30)

wordDict = {}

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

# Fills queue with messages. Once filled pushes and pops.
def fillQueue(msg):
	queue.append(msg)

def addNew(msg):
	global wordDict
	words = msg.split()
	for word in words:
            try:
		if (wordDict[word]):
	            wordDict[word.lower()] += 1
            except Exception, e:
		if(len(word) >= 3 and len(word) <10):
		    wordDict[word.lower()] = 1

# Do the cool thing (puts smaller functions together)
def cmdSillySentence():
	global madlib_list
	global chatKey
        global wordDict
        chatWords=[]

	sentence = ""
	message=queue.popleft()

	mad=random.choice(madlib_list)
	madWords=mad.split()

	for word in madWords:
            if chatKey in word:
                if not wordDict:
                    return ""
                tempWord=max(wordDict,key=wordDict.get)
                sentence+=" |" + tempWord + "|"
                chatWords.append(tempWord)
                del(wordDict[tempWord])
            else:
                sentence+=" " + word

        for word in chatWords:
            print(word + " ")

	queue.append(message)
	print("-------->" + sentence)
	wordDict.clear()
	return sentence
