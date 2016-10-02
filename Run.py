import string, sys, threading, time
from os import execv
from Defs import *
from Settings import RCRDINT, IDENT, MODS
from Socket import openSocket, sendMessage
from Initialize import joinRoom


s = openSocket()
joinRoom(s)
readbuffer = ""
kappaCount=0
interval=0
tempMsgCount=0
gameStarted=0
recording=False
msgCount={}
createEmotes()

class TimerClass(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.event = threading.Event()
		self.count = 0

	def run(self):
		global tempMsgCount
		global interval
		global msgCount
		while not self.event.is_set():
			#print str(self.count)+"s "+str(tempMsgCount)
			if (self.count%RCRDINT==0):
				msgCount[interval]=tempMsgCount
				print str((interval-1)*RCRDINT)+"s to "+str(interval*RCRDINT)+"s \t"+str(tempMsgCount)
				interval+=1
				tempMsgCount=0
			self.count += 1
			self.event.wait(1)

	def stop(self):
		total=0
		for i in msgCount:
			print("add "+str(msgCount[i]))
			total+=msgCount[i]
		print("recorded "+str(self.count)+"s \t"+"total messages: "+str(total))
		self.event.set()

tmr = TimerClass()

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			if(recording):
				tempMsgCount+=1

			user = getUser(line)
			message = getMessage(line)
			words=message.split()
			if "PING" in message:
				PONG(s)

			if "Kappa" in  message:
				kappaCount+=1

			if("!" not in message or user !=IDENT):
				fillQueue(message)
				# addNew(message)

			if("!restart" in message):
				if(verifymod(user)):
					#CHANGE HARDCODED NAME
					print("Redo")
					sendMessage(s,"GivePLZ Restarting TakeNRG")
					execv(sys.executable, ['python'] + sys.argv)

			if "!shutdown" in message:
				user = getUser(line);
				if(verifymod(user)):
					sendMessage(s,"GoodBye!")
					print("Exiting")
					sys.exit();
				else:
					#sendMessage(s,"how about no")
					break

			if ("!msgrecord" in message) and (verifymod(user)):
				#TODO ABOVE SHOULD CHANGE HARDCODED NAME
				if(recording):
					tmr.stop()
					print("stop counting")
					# try:
					# 	if (words[1].lower()=="kappa"):
					# 		sendMessage(s,"Stop:  \t"+str(kappaCount)+" Kappas posted")

					# except Exception, e:
					# 	sendMessage(s,"Stop recording")

					recording=False
					interval=0
					tempMsgCount=0

				else:
					print("starting msg count")
					# sendMessage(s,"Starting recording...")
					recording=True
					interval=0
					tempMsgCount=0
					tmr.start()

			if "!red" in message:
				sendMessage(s, "me me")
				time.sleep(1)
				sendMessage(s, getRed(GAME))

			if "!ping" in  message:
				try:
					if (words[1]):
						sendMessage(s,"pong "+words[1])
						break
				except Exception, e:
					print("no param")
					break

				sendMessage(s,"PONG!")

			if "!liquidslam" in message:
				sentence = cmdSillySentence()
				if sentence:
					sendMessage(s, sentence)
					#exit()
				else:
					sendMessage(s, "Need more words!!!")
					#sendMessage(s,"Not enough souls Kappa")
				break
			if ("!Kappa" in message):
					sendMessage(s,kappaCount+" kappas")

def verifymod(user):
	for name in MODS:
		if(user == name):
			return True
	return False



