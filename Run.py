import string, sys

from Defs import *
from Socket import openSocket, sendMessage
from Initialize import joinRoom


s = openSocket()
joinRoom(s)
readbuffer = ""
kappaCount=0

createEmotes()

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()


		for line in temp:

			user = getUser(line)
			message = getMessage(line)
			words=message.split()
			if("*" not in message or user !="z03hboot"):
				fillQueue(message)
				# addNew(message) #####
			if "Kappa" in  message:
				kappaCount+=1
				#sendMessage(s,str(kappaCount)+ " kappas")
				break
			if "*ping" in  message:
				try:
				    if (words[1] == "pong"):
					sendMessage(s,"kappa")
				except Exception, e:
				    print("no param")

				sendMessage(s,"PONG!")
				break
			if "*shutdown" in message:
				user = getUser(line);
				if(user == "zo3h"):
					sendMessage(s,"GoodBye!")
					print("Exiting")
					sys.exit();
				else:
					#sendMessage(s,"how about no")
					break
			if "*liquidslam" in message:
			        sentence = cmdSillySentence()
				if sentence:
					sendMessage(s, sentence)
					#exit()
				else:
					print("Need more words!!!")
					#sendMessage(s,"Not enough souls Kappa")
				break
			if "PING" in message:
				PONG(s)
				#s.send(line.replace("PING", "PONG"))
				break

