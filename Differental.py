import numpy as np
from matplotlib import pyplot as plt

class vector2D:
    def __init__(self,u,v):
        self.x = 0
        self.y = 0
        self.u = u
        self.v = v

    def addVectorToList(self, list):
        list[0].append(self.x)
        list[1].append(self.y)
        list[2].append(self.u)
        list[3].append(self.v)

class point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addPointToList(self, list):
        list[0].append(self.x)
        list[1].append(self.y)

g = 9.8
L = 2
mu = 0.1

thetaStart = np.pi / 3
thetaDotStart = 0

def thetaDoubleDot(theta, thetaDot):        
    return -mu * thetaDot - (g / L) * np.sin(theta)

points = [[], []]
points_point = []

def theta(t):
    theta = thetaStart
    thetaDot = thetaDotStart
    delta_t = 0.01
    for time in np.arange(0, t, delta_t):
        theta_Double_Dot = thetaDoubleDot(theta, thetaDot)
        theta += thetaDot * delta_t
        newPoint = point2D(theta, thetaDot)
        points_point.append(newPoint)
        thetaDot += theta_Double_Dot * delta_t
    return theta

print(theta(10))
for point in points_point:
    point.addPointToList(points)

plt.scatter(points[0], points[1])
plt.show()

"""  Later for vector field!
vectors = [[],[],[],[]]

# Let u be angle and v be angular velocity (the derivative of theta)
vector1 = vector2D(1,2)
vector1.addVectorToList(vectors)

plt.quiver(vectors[0], vectors[1], vectors[2], vectors[3])
plt.show()
"""