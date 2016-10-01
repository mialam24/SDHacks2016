import string, sys
from Read import getUser, getMessage, PONG
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""
kappaCount=0

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			#print(line)
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
			if "asdfl;aksjo" in line:
				
				break
			if "PING" in line:
				PONG(s);
				#s.send(line.replace("PING", "PONG"))
				break
			
			user = getUser(line)
			message = getMessage(line)
			print user + ":" + message
			if "you suck" in message.lower():
				#sendMessage(s, "No, you suck!")
				break
			
