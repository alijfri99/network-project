class Agent:
    def __init__(self, X, Y,state):
        global id
        self.id = id
        self.X = X
        self.Y = Y
        self.state = state
        id = id+1
    def __str__(self):
        return ("X: " + str(self.X) + ", " + "Y: " + str(self.Y) + ", " + "ID: " + str(self.id))