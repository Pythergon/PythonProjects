import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def return_coord(self):
        return self.x, self.y

class vector2D:
    def __init__(self,u,v):
        self.x = 0
        self.y = 0
        self.u = u
        self.v = v
    
    def return_coord(self):
        return self.u, self.v

    def append_to_list(self, list_name):
        list_name[0].append(self.x)
        list_name[1].append(self.y)
        list_name[2].append(self.u)
        list_name[3].append(self.v)

def vector_addition(vector1, vector2):
    return vector1.u + vector2.u, vector1.v + vector2.v

def scalar_multiplication(scalar, vector):
    return vector.u*scalar, vector.v*scalar

# Matplot lib stuff
points = [[1], [1]]
vectors = [[], [], [], []]

# Point Stuff
print("Hello, World!")
myPoint = point(1, 3)
print(myPoint.return_coord())

# Vector Stuff
scalar = -1.3
vector1 = vector2D(1, 5)
vector2 = vector2D(2, -6)

print(scalar_multiplication(scalar, vector2))
print(vector_addition(vector1, vector2))
vector1.append_to_list(vectors)
vector2.append_to_list(vectors)

# End
plt.quiver(vectors[0], vectors[1], vectors[2], vectors[3], width=0.005)
# plt.scatter(points[0], points[1])
plt.show()
