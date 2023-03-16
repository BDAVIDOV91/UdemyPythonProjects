import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D



# Define the constants
G = 6.67430e-11
m_sun = 1.989e30

# Define the masses and initial positions and velocities of the planets
m_earth = 5.972e24
m_mars = 6.39e23
x_earth = np.array([147e9, 0, 0])
x_mars = np.array([0, 228e9, 0])
v_earth = np.array([0, 30.29e3, 0])
v_mars = np.array([24.077e3, 0, 0])

# Set up the simulation
t = 0
dt = 3600
nsteps = 365 * 24
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
for i in range(nsteps):
    # Calculate the gravitational force
    r_earth = np.linalg.norm(x_earth)
    r_mars = np.linalg.norm(x_mars)
    F_earth = G * m_sun / r_earth ** 2 * x_earth / r_earth
    F_mars = G * m_sun / r_mars ** 2 * x_mars / r_mars
    
    # Update the positions and velocities using the Euler method
    x_earth += v_earth * dt
    x_mars += v_mars * dt
    v_earth += F_earth / m_earth * dt
    v_mars += F_mars / m_mars * dt
    
    # Update the time
    t += dt
    
    # Plot the positions of the planets in 3D
    ax.scatter(x_earth[0], x_earth[1], x_earth[2], c = 'b', marker = 'o')
    ax.scatter(x_mars[0], x_mars[1], x_mars[2], c = 'r', marker = 'o')
    ax.set_xlim(-2e11, 2e11)
    ax.set_ylim(-2e11, 2e11)
    ax.set_zlim(-2e11, 2e11)
    plt.pause(0.01)
    ax.cla()
    
plt.show()