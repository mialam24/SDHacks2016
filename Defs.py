import string, threading

from collections import deque

queue=deque([], maxlen=30)
sentence=""

wordDict = {}
# order=["noun", "adverb", "verb", "adjective", "noun", "chat"]
# order=["chat", "chat", "chat", "chat", "chat", "chat"]
index=0

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
	print("PONG SENT!")
	threading.Timer(300, PONG).start()

# Creates dictionaries
def createDict():
	global wordDict
	f = open('dictAdjs.txt' , 'r')
	str = f.readline()
	while str :
		str = str[:-1]
		wordDict[str] = 'adjective'
		str = f.readline()
	f.close()

	f = open('dictAdvs.txt' , 'r')
	str = f.readline()
	while str :
		str = str[:-1]
		wordDict[str] = 'adverb'
		str = f.readline()
	f.close()
	
	f = open('dictVerbs.txt' , 'r')
	str = f.readline()
	while str :
		str = str[:-1]
		wordDict[str] = 'verb'
		str = f.readline()
	f.close()

	f = open('dictNouns.txt' , 'r')
	str = f.readline()
	while str :
		str = str[:-1]
		wordDict[str] = 'noun'
		str = f.readline()
	f.close()
	print("Dictionary done :)")

# Fills queue with messages. Once filled pushes and pops.
def fillQueue(msg):
	queue.append(msg)

def addNew(msg):
	global wordDict
	words = msg.split()
	for word in words:
		try:
			if (wordDict[word]):
				print("found word")
				wordDict[word.lower()] += 1
		except Exception, e:
			print(word+" not found")
			if(len(word) >= 3 and len(word) <10):
				wordDict[word.lower()] = 1
				print(word + " added")

# Find out if word of "type" exists in message
def findWordType(msg, wtype):
	global sentence
	global index
	words = msg.split()
	for word in words:
		
		if (checkType(word.lower(), wtype)):
			sentence+=" "+ word.lower()
			index+=1
			return
# Check if word is of type
def checkType(word, wtype):
	global wordDict
	try:
		if (wordDict[word] == wtype):
			return True
		else:
			return False
	except Exception, e:
		print(word+" not found")
		

# Do the cool thing (puts smaller functions together)
def cmdSillySentence():
	global index
	global sentence 
	count = 0
	max_count = len(queue)
	while(count<6):
		if(count == max_count):
			print("not enough souls")
			print("--------" + sentence)
			return ""
		count+=1
		message=queue.popleft()
		tempWord=max(wordDict,key=wordDict.get)
		sentence+=" "+ "|" + tempWord
		del(wordDict[tempWord])
		#findWordType(message,order[index])
		queue.append(message)
	print("-------->" + sentence)
	wordDict.clear()
	index=0
	return sentence
