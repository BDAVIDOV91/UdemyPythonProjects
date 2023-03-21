import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


# Define constants
G = 6.67430e-11  # gravitational constant
m_earth = 5.9722e24  # mass of Earth
m_sun = 1.989e30  # mass of Sun

# Define initial conditions
r_earth = np.array([147e9, 0])  # position of Earth (m)
v_earth = np.array([0, 30e3])  # velocity of Earth (m/s)
r_sun = np.array([0, 0])  # position of Sun (m)
v_sun = np.array([0, 0])  # velocity of Sun (m/s)

# Define simulation parameters
dt = 60  # time step (s)
t_max = 365 * 24 * 3600  # maximum simulation time (s)

# Define empty arrays to store positions and velocities
sun_pos = np.zeros((int(t_max/dt)+1, 3))
sun_vel = np.zeros((int(t_max/dt)+1, 3))
earth_pos = np.zeros((int(t_max/dt)+1, 3))
earth_vel = np.zeros((int(t_max/dt)+1, 3))
mars_pos = np.zeros((int(t_max/dt)+1, 3))
mars_vel = np.zeros((int(t_max/dt)+1, 3))
mercury_pos = np.zeros((int(t_max/dt)+1, 3))
mercury_vel = np.zeros((int(t_max/dt)+1, 3))
venus_pos = np.zeros((int(t_max/dt)+1, 3))
venus_vel = np.zeros((int(t_max/dt)+1, 3))
jupiter_pos = np.zeros((int(t_max/dt)+1, 3))
jupiter_vel = np.zeros((int(t_max/dt)+1, 3))
saturn_pos = np.zeros((int(t_max/dt)+1, 3))
saturn_vel = np.zeros((int(t_max/dt)+1, 3))
uranus_pos = np.zeros((int(t_max/dt)+1, 3))
uranus_vel = np.zeros((int(t_max/dt)+1, 3))
neptune_pos = np.zeros((int(t_max/dt)+1, 3))
neptune_vel = np.zeros((int(t_max/dt)+1, 3))



# Define the masses and initial positions and velocities of the planets
m_earth = 5.972e24
m_mars = 6.39e23
m_mercury = 3.285e23
m_venus = 4.867e24
m_jupiter = 1.898e27
m_saturn = 5.683e26
m_uranus = 8.681e25
m_neptune = 1.024e26


x_sun = np.array([0, 0, 0])
x_earth = np.array([147e9, 0, 0])
x_mars = np.array([0, 228e9, 0])
x_mercury = np.array([0, 58e9, 0])
x_venus = np.array([108e9, 0, 0])
x_jupiter = np.array([0, 778e9, 0])
x_saturn = np.array([1.429e12, 0, 0])
x_uranus = np.array([0, 2.871e12, 0])
x_neptune = np.array([4.498e12, 0, 0])


v_sun = np.array([0, 0, 0])
v_earth = np.array([0, 30.29e3, 0])
v_mars = np.array([24.077e3, 0, 0])
v_mercury = np.array([0, 47.87e3, 0])
v_venus = np.array([35.02e3, 0, 0])
v_jupiter = np.array([0, 13.07e3, 0])
v_saturn = np.array([9.69e3, 0, 0])
v_uranus = np.array([0, 6.80e3, 0])
v_neptune = np.array([5.43e3, 0, 0])

a_earth = np.array([-x_earth, -y_earth, -z_earth]).reshape(3, 1)


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

# Define the simulation loop
for i in range(int(t_max/dt)+1):

    # Calculate the distance between the Earth and the Sun
    x_sun = r_earth - r_sun
    r_sun = np.sqrt(x_sun[0]**2 + x_sun[1]**2)

    # Calculate the gravitational force on the Earth due to the Sun
    if r_sun == 0:
        F_sun = np.zeros(2)
    else:
        F_sun = G * m_earth / r_sun ** 2 * x_sun / r_sun

    # Calculate the acceleration of the Earth
    a_earth = F_sun / m_earth

    # Update the velocity and position of the Earth
    v_earth += a_earth * dt
    r_earth += v_earth * dt

    # Update the position and velocity arrays
    earth_pos[i] = r_earth
    earth_vel[i] = v_earth
    sun_pos[i] = r_sun
    sun_vel[i] = v_sun

#for i in range(nsteps):
    # Calculate the gravitational force
   # r_sun = np.linalg.norm(x_sun)
   # r_earth = np.linalg.norm(x_earth)
   # r_mars = np.linalg.norm(x_mars)
   # r_mercury = np.linalg.norm(x_mercury)
   # r_venus = np.linalg.norm(x_venus)
   # r_jupiter = np.linalg.norm(x_jupiter)
   # r_saturn = np.linalg.norm(x_saturn)
   # r_uranus = np.linalg.norm(x_uranus)
   # r_neptune = np.linalg.norm(x_neptune)
    
   # F_sun = G * m_earth / r_sun ** 2 * x_sun / r_sun
   # F_mars = G * m_sun / r_mars ** 2 * x_mars / r_mars
   # F_mercury = G * m_sun / r_mercury ** 2 * x_mercury / r_mercury
   # F_venus = G * m_sun / r_venus ** 2 * x_venus / r_venus
   # F_jupiter = G * m_sun / r_jupiter ** 2 * x_jupiter / r_jupiter
   # F_saturn = G * m_sun / r_saturn ** 2 * x_saturn / r_saturn
   # F_uranus = G * m_sun / r_uranus ** 2 * x_uranus / r_uranus
   # F_neptune = G * m_sun / r_neptune ** 2 * x_neptune / r_neptune
    
    # Calculate the acceleration
   # a_sun = F_sun / m_sun
   # a_earth = F_earth / m_earth
   # a_mars = F_mars / m_mars
   # a_mercury = F_mercury / m_mercury
   # a_venus = F_venus / m_venus
   # a_jupiter = F_jupiter / m_jupiter
   # a_saturn = F_saturn / m_saturn
   # a_uranus = F_uranus / m_uranus
   # a_neptune = F_neptune / m_neptune
   
    # Update the positions and velocities using the Euler method
   # x_sun += v_sun * dt
   # x_earth += v_earth * dt
   # x_mars += v_mars * dt
   # x_mercury += v_mercury * dt
   # x_venus += v_venus * dt
   # x_jupiter += v_jupiter * dt
   # x_saturn += v_saturn * dt
   # x_uranus += v_uranus * dt
   # x_neptune += v_neptune * dt
    
   # v_sun += a_sun * dt
   # v_earth += a_earth * dt
   # v_mars += a_mars * dt
   # v_mercury += a_mercury * dt
   # v_venus += a_venus * dt
   # v_jupiter += a_jupiter * dt
   # v_saturn += a_saturn * dt
   # v_uranus += a_uranus * dt
   # v_neptune += a_neptune * dt

    
    
    # Plot the positions of the planets in 3D
    ax.scatter(x_earth[0], x_earth[1], x_earth[2], c='b', marker='o')
    ax.scatter(x_mars[0], x_mars[1], x_mars[2], c='r', marker='o')
    ax.scatter(x_mercury[0], x_mercury[1], x_mercury[2], c='y', marker='o')
    ax.scatter(x_venus[0], x_venus[1], x_venus[2], c='g', marker='o')
    ax.scatter(x_jupiter[0], x_jupiter[1], x_jupiter[2], c='k', marker='o')
    ax.scatter(x_saturn[0], x_saturn[1], x_saturn[2], c='c', marker='o')
    ax.scatter(x_uranus[0], x_uranus[1], x_uranus[2], c='m', marker='o')
    ax.scatter(x_neptune[0], x_neptune[1], x_neptune[2], c='orange', marker='o')


    
plt.plot(earth_pos[:,0], earth_pos[:,1])
plt.show()