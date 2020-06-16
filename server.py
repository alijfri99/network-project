import socket
import packet
import initiator
import pickle

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
seqNo = 0
try:
    server.bind(('127.0.0.1',8080))
    print("Server Started")
except:
    print("Error: Could not start the server")

while(True):
    data, addr = server.recvfrom(4096)
    pack = pickle.loads(data)
    if(type(pack) is initiator.initiator):
    	msg = "ACKINIT"
    	print(msg)
    	server.sendto(msg.encode("utf-8"), addr)
    elif(type(pack) is packet.packet):
        if(seqNo==pack.seqNo):
            print(str(pack))
            msg = "ACK" + str(pack.seqNo)
            print(msg)
            server.sendto(msg.encode("utf-8"), addr)
            seqNo = 1 - seqNo
        else:
            msg = "NAK"
            print(msg)
            server.sendto(msg.encode("utf-8"), addr)