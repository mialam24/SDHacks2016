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
