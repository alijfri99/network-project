import socket
import packet
import initiator
import pickle
import tools

def isok(pack):
	tempSum = tools.calcsum(pack.msg)
	if(int(tempSum,2) + int(pack.checksum,2)==255):
		return True
	else:
		return False

def printmsg(packets,init):
	msg = bytearray()
	for pack in packets:
		msg = msg + pack.msg
	print(pickle.loads(bytes(msg[init.redundant:len(msg)])))

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
seqNo = 0
numberOfPackets = 0
init = None
packets = []
try:
    server.bind(('127.0.0.1',8080))
    print("Server Started")
except:
    print("Error: Could not start the server")

while(True):
    data, addr = server.recvfrom(4096)
    pack = pickle.loads(data)
    if(type(pack) is initiator.initiator):
    	init = pack
    	packets = []
    	numberOfPackets = int(pack.length/394)
    	if(pack.length%394!=0):
    		numberOfPackets = numberOfPackets + 1
    	msg = "ACKINIT"
    	server.sendto(msg.encode("utf-8"), addr)
    elif(type(pack) is packet.packet):
        if(seqNo==pack.seqNo) and isok(pack):
            packets.append(pack)
            msg = "ACK" + str(pack.seqNo)
            server.sendto(msg.encode("utf-8"), addr)
            if(len(packets)!=numberOfPackets):
            	seqNo = 1 - seqNo
            else:
                printmsg(packets, init)
        else:
            msg = "ACK" + str(1-seqNo)
            server.sendto(msg.encode("utf-8"), addr)