class Agent:
    def __init__(self, id, X, Y,state):
        self.id = id
        id = id+1
        self.X = X
        self.Y = Y
        self.state = state
    def __str__(self):
    	return("X: " + str(self.X) + ", Y: " + str(self.Y) + ", ID: " + str(self.id))