import socket
from ..classes import agent

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
    server.bind(('127.0.0.1',8080))
    print("Server Started")
except:
    print("Error: Could not start the server")

while(True):
    data, addr = server.recvfrom(4096)
    myAgent = agent.Agent(data)