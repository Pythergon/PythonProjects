import numpy as np
from matplotlib import pyplot as plt

class vector2D:
    def __init__(self,x,y,u,v):
        self.x = x
        self.y = y
        self.u = u
        self.v = v

    def addVectorToList(self, list):
        list[0].append(self.x)
        list[1].append(self.y)
        list[2].append(self.u)
        list[3].append(self.v)

g = 9.8
L = 2
mu = 0.1

vector_list = []
vectors = [[],[],[],[]]

def thetaDoubleDot(theta, thetaDot):        
    return -mu * thetaDot - (g / L) * np.sin(theta)

thetaRange = np.linspace(-2 * np.pi, 2 * np.pi, 20)
thetaDotRange = np.linspace(-5, 5, 20)

# Get vector values and append them to list
for thetaVal in thetaRange:
    for thetaDotVal in thetaDotRange:
        dTheta = thetaDotVal
        dThetaDot = thetaDoubleDot(thetaVal, thetaDotVal)

        newVector = vector2D(thetaVal, thetaDotVal, dTheta, dThetaDot)
        vector_list.append(newVector)

# Put object varibles into the final list
for vector in vector_list:
    vector.addVectorToList(vectors)

# Plotting stuf  
plt.quiver(vectors[0], vectors[1], vectors[2], vectors[3], color='purple')
plt.grid(True)
plt.show()