from matplotlib import pyplot as plt

# Inital
X_0 = 0
Y_0 = 0

# Steps, final, and delta cal
N = 20
x1 = 5
delta = (x1-X_0)/N

# Our differental, takes in the x, y, and delta
def differental1(x, y, d):
    return y + d * (x + 1/5 * y)

def differental2(x, y, d):
    return y + d * (2 * x)

#Mattty lib
xvals = []
yvals = []

# Enumerate
Xpos = X_0
Ypos = Y_0
for i in range(0, N):
    Ypos = differental2(Xpos, Ypos, delta)
    Xpos += delta
    print(Xpos)
    yvals.append(Ypos)
    xvals.append(Xpos)

# Finish him!
print(Ypos)
plt.scatter(xvals, yvals)
plt.show()