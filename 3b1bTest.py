import numpy as np

#Physical Constants
g = 9.8
L = 2
mu = 0.1

THETA_0 = np.pi / 3
THETA_DOT_0 = 0

# Definiton of ODE
def getThetaDoubleDot(theta, thetaDot):
    return -mu * thetaDot - (g / L) * np.sin(theta)

# Solution to the differental equation
def theta(t):
    # Initalize changing values
    theta = THETA_0
    thetaDot = THETA_DOT_0
    delta_t = 0.01
    for time in np.arange(0, t, delta_t):
        theta_double_dot = getThetaDoubleDot(theta, thetaDot)
        theta += thetaDot * delta_t
        thetaDot += theta_double_dot * delta_t
        print(f"{theta} | {thetaDot}")
    return theta

print(theta(10))