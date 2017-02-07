print ("hello1")
import socket
import sys
import motorlibrary
print ("hello2")
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 25565)
print ("starting up on %s port %s" % server_address)
sock.bind(server_address)

while True:
	print ('\nWaiting to receive message')
	data, address = sock.recvfrom(4096)
	
	print ('received %s bytes from %s' % (len(data), address))
	print (data)
	if data == "r":
		motorlibrary.Turn("r")
	elif data == "space":
		motorlibrary.Turn("s")
	elif data == "l":
		motorlibrary.Turn("l")
	elif data == "w":
		motorlibrary.MoveBy("f", 0.1)
	elif data == "s":
		motorlibrary.MoveBy("b", 0.1)
	elif data == "end session":
		sock.close()
		break