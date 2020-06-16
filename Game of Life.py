# This code is
#   based on https://nostarch.com/download/samples/PythonPlayground_sampleCh3.pdf
#   prepared for Computer Networking Class: Ferdowsi University of Mashhad

import matplotlib; matplotlib.use("TkAgg")  # For pycharm IDE only
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import socket
import agent
import packet
import initiator
import pickle

N = 30  # Grid size is N*N
live = 255
dead = 0
state = [live, dead]
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
seqNo = 0

# Create random population (more dead than live):
grid = np.random.choice(state, N * N, p=[0.3, 0.7]).reshape(N, N)
# To learn more about not uniform random visit:
# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html

def udt_send(data):
    client.sendto(pickle.dumps(data),("127.0.0.1",8080))

def send(pack,ackmsg):
	udt_send(pack)
	while(True):
		try:
			data, addr = client.recvfrom(500)
			client.settimeout(1)
			if(data.decode("utf-8")==ackmsg):
				print(data.decode("utf-8"))
				return
		except socket.timeout as e:
			udt_send(pack)


def update(data):
    global grid
    global seqNo
    temp = grid.copy()
    result = []
    for i in range(N):
        for j in range(N):
            # Compute 8-neighbor sum
            total = (grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                     grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                     grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                     grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255
            # Apply Conway's Rules:
            # 1- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            # 2- Any live cell with two or three live neighbours lives on to the next generation.
            # 3- Any live cell with more than three live neighbours dies, as if by overpopulation.
            # 4- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if grid[i, j] == live:
                if (total < 2) or (total > 3):
                    temp[i, j] = dead
                    result.append((i,j))
            else:
                if total == 3:
                    temp[i, j] = live
    if(len(result)>0):
        (a,b) = random.choice(result)
        selectedAgent = agent.Agent(b,a,dead)
        msg = bytearray(pickle.dumps(selectedAgent))
        actualLen = len(msg)
        redundant = random.randint(500, 1500)
        redundantBytes = bytearray(redundant)
        for i in range(redundant):
            redundantBytes[i] = random.randint(0, 255)
        msg = redundantBytes + msg
        init = initiator.initiator(redundant+actualLen,redundant)
        send(init, "ACKINIT")
        numberOfPackets = int(len(msg)/394)
        if(len(msg)%394!=0):
            numberOfPackets = numberOfPackets + 1
        packets = []
        for i in range(numberOfPackets):
            if(i<numberOfPackets-1):
                pack = packet.packet(msg[i*394:(i+1)*394], seqNo)
                seqNo = 1 - seqNo
                packets.append(pack)
            else:
            	pack = packet.packet(msg[i*394:len(msg)], seqNo)
            	packets.append(pack)

        for pack in packets:
            send(pack, "ACK"+str(pack.seqNo))

        mat.set_data(temp)
        grid = temp
    return mat


# Animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=500)
plt.show()

'''
class packet():
    checksum = 0;
    length = 0;
    seqNo = 0;
    msg = 0;

    def make(self, data):
        self.msg = data
        self.length = str(len(data))
        self.checksum=hashlib.sha1(data).hexdigest()
'''