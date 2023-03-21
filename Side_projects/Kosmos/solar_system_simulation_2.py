import pygame
import numpy as np
import sys

# Define the parameters for each planet
sun_mass = 1.989e30 # kg
sun_radius = 6.96e8 # m
sun_pos = np.array([0, 0, 0]) # m
sun_vel = np.array([0, 0, 0]) # m/s

earth_mass = 5.97e24 # kg
earth_radius = 6.37e6 # m
earth_pos = np.array([1.5e11, 0, 0]) # m
earth_vel = np.array([0, 2.98e4, 0]) # m/s

# Define the gravitational constant
G = 6.674e-11 # m^3 / (kg * s^2)

# Define the Pygame window dimensions
width, height = 800, 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))

# Define the colors for each planet
sun_color = (255, 255, 0)
earth_color = (0, 0, 255)

# Define the time step and duration of the simulation
dt = 1e3 # s
t_end = 3.154e7 # s

# Initialize the positions and velocities of the planets
sun_pos_history = [sun_pos]
sun_vel_history = [sun_vel]
earth_pos_history = [earth_pos]
earth_vel_history = [earth_vel]

# Define the main simulation loop
t = 0
while t < t_end:
    # Calculate the distance between the sun and earth
    r = np.linalg.norm(earth_pos - sun_pos)
    
    # Calculate the gravitational force between the sun and earth
    F_grav = G * sun_mass * earth_mass / r**2
    
    # Calculate the direction of the gravitational force
    F_dir = (sun_pos - earth_pos) / r
    
    # Calculate the gravitational force acting on the earth
    F_grav_earth = F_grav * F_dir
    
    # Calculate the gravitational force acting on the sun
    F_grav_sun = -F_grav_earth
    
    # Calculate the acceleration of the earth and sun
    a_earth = F_grav_earth / earth_mass
    a_sun = F_grav_sun / sun_mass
    
    # Update the velocity of the earth and sun
    earth_vel = earth_vel + a_earth * dt
    sun_vel = sun_vel + a_sun * dt
    earth_pos = earth_pos + earth_vel * dt
    sun_pos = sun_pos + sun_vel * dt
    
    # Record the positions and velocities of the earth and sun
    earth_pos_history.append(earth_pos)
    earth_vel_history.append(earth_vel)
    sun_pos_history.append(sun_pos)
    sun_vel_history.append(sun_vel)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the sun
    pygame.draw.circle(screen, sun_color, (int(width / 2), int(height / 2)), 10)

    # Draw the earth
    x = int(width / 2 + earth_pos[0] / 1e9)
    y = int(height / 2 + earth_pos[1] / 1e9)
    pygame.draw.circle(screen, earth_color, (x, y), 2)

    # Update the Pygame display
    pygame.display.update()

    # Check for Pygame events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
