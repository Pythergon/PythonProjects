import numpy as np
from matplotlib import pyplot as plt

# Point class because OOP is awesome :)
class point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addPointToList(self, list):
        list[0].append(self.x)
        list[1].append(self.y)

# Physical Constants
g = 9.8
L = 2
mu = 0.1

# Starting Points
thetaStart = np.pi / 3
thetaDotStart = 3

# Lists to hold data values
points = [[], []]
points_point = []

# Functions :)
def thetaDoubleDot(theta, thetaDot):        
    return -mu * thetaDot - (g / L) * np.sin(theta)

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

# Runnnn it up!
print(theta(100))
for point in points_point:
    point.addPointToList(points)

# Plot the points!
plt.scatter(points[0], points[1], s=1)
plt.show()