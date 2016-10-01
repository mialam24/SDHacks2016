import string, sys
from Read import getUser, getMessage, PONG
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			if "*ping" == line:
				sendMessage(s,"PONG!")
				break
			if "PING" in line:
				PONG(s);
				#s.send(line.replace("PING", "PONG"))
				break
			
			user = getUser(line)
			message = getMessage(line)
			print user + " typed :" + message
			if "You Suck" in message:
				sendMessage(s, "No, you suck!")
				break
			
