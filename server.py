import socket
import packet

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
seqNo = 0
try:
    server.bind(('127.0.0.1',8080))
    print("Server Started")
except:
    print("Error: Could not start the server")

while(True):
    data, addr = server.recvfrom(4096)
    pack = data.decode("utf-8")
    print(str(pack))
    msg = "ACK" + str(seqNo)
    seqNo = 1 - seqNo
    print(msg)
    server.sendto(msg.encode("utf-8"), addr)