import string
import threading

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
def createDict(textFile):

# Fills queue with messages. Once filled pushes and pops.
def fillQueue(msg):

# Find out if word of "type" exists in message
def findWordType(msg, type):

# Check if word is of type
def checkType(word, type):

# Do the cool thing (puts smaller functions together)
def cmdSillySentence(msgQueue):

# Main
# 	var:Queue
#	var:Dict;
#	createDict;
#	while keep getting messages
#		fillQueue
#		If cmd has been made
#			CmdSillySentence
#				var:Sentence
#					Loop while sentence not complete
#						findWordType
#							checkType
#					If sentence not long enough: print out "you nub. use words"
