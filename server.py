import socket
import packet
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
    print(str(pack))
    msg = "ACK" + str(pack.seqNo)
    print(msg)
    server.sendto(msg.encode("utf-8"), addr)