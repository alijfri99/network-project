# This code is
#   based on https://nostarch.com/download/samples/PythonPlayground_sampleCh3.pdf
#   prepared for Computer Networking Class: Ferdowsi University of Mashhad

import matplotlib; matplotlib.use("TkAgg")  # For pycharm IDE only
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import socket


N = 30  # Grid size is N*N
live = 255
dead = 0
state = [live, dead]
id = 0
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Create random population (more dead than live):
grid = np.random.choice(state, N * N, p=[0.3, 0.7]).reshape(N, N)
# To learn more about not uniform random visit:
# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.choice.html

class Agent:
    def __init__(self, X, Y,state):
        global id
        self.id = id
        id = id+1
        self.X = X
        self.Y = Y
        self.state = state

def choose(temp):
    result = []
    for i in range(N):
        for j in range(N):
            if(temp[i][j] == dead):
                result.append((i,j))
    (a,b) = random.choice(result)
    agent = Agent(b,a,dead)
    udt_send(agent)

def udt_send(data):
    client.sendto(str(data).encode("utf-8"),("127.0.0.1",8080))

def update(data):
    global grid
    temp = grid.copy()
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
            else:
                if total == 3:
                    temp[i, j] = live
            choose(temp)
    mat.set_data(temp)
    grid = temp
    return mat


# Animation
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=500)
plt.show()

# Can be useful:
'''

    # Need more features? Add them!
'''

'''
create unique ID for agent based on UUID:
    https://docs.python.org/3/library/uuid.html
'''

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
