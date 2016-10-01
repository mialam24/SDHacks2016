import string, sys

from Defs import getUser, getMessage, PONG, fillQueue, cmdSillySentence,createDict
from Socket import openSocket, sendMessage
from Initialize import joinRoom


s = openSocket()
joinRoom(s)
readbuffer = ""
kappaCount=0
createDict()

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		
		for line in temp:

			user = getUser(line)
			message = getMessage(line)
			#print user + ":" + message

			#print(line)
			if("*" not in message):
				fillQueue(message)
			if "Kappa" in  line:
				kappaCount+=1
				#sendMessage(s,str(kappaCount)+ " kappas")
				break
			if "*ping" in  line:
				#sendMessage(s,"PONG!")
				break
			if "*shutdown" in line:
				user = getUser(line);
				if(user == "zo3h"):
					sendMessage(s,"GoodBye!")
					print("Exiting")
					sys.exit();
				else:
					#sendMessage(s,"how about no")
					break
			if "*liquidslam" in line:
				sentence = cmdSillySentence()
				if sentence:
					sendMessage(s,sentence)
				else:
					sendMessage(s,"Not enough souls Kappa")	
				break
			if "PING" in line:
				PONG(s)
				#s.send(line.replace("PING", "PONG"))
				break
			
			
			
			
