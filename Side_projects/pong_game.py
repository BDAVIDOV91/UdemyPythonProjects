import pygame
import random
import sys

# Initialize Pygame 
pygame.init()

# Setup the game window
window_width = 600
window_height = 400

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pong Game')

# Game objects

# Ball 
ball = pygame.Rect(window_width / 2 - 15, window_height / 2 - 15, 30, 30)
ball_speed_x = 1 * random.choice((1, -1))
ball_speed_y = 1 * random.choice((1, -1))

# Paddles
player_paddle = pygame.Rect(10, window_height/ 2 - 60, 10, 120)
opponent_paddle = pygame.Rect(window_width - 20, window_height / 2 - 60, 10, 120)
paddle_speed = 2

# Score variables
player_score = 0
opponent_score = 0

# Text Variables
game_font = pygame.font.Font(None, 50)


# Main Loop update the game objects and check for collisions and user input
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.move_ip(0, - paddle_speed)
    if keys[pygame.K_s] and player_paddle.bottom < window_height:
        player_paddle.move_ip(0, paddle_speed)
        
    # Move opponent paddle
    if opponent_paddle.centery < ball.centery and opponent_paddle.bottom < window_height:
        opponent_paddle.move_ip(0, paddle_speed)
    elif opponent_paddle.centery > ball.centery and opponent_paddle.top > 0:
        opponent_paddle.move_ip(0, - paddle_speed)
        
    # Move the ball
    ball.move_ip(ball_speed_x, ball_speed_y)
    
    # Check for collisions with the walls
    if ball.top <= 0 or ball.bottom >= window_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        opponent_score += 1
        ball.center = (window_width / 2, window_height / 2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    if ball.right >= window_width:
        player_score += 1
        ball.center = (window_width /2, window_height /2)
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
        
    # Check for collisions with paddles
    if ball.colliderect(player_paddle):
        ball_speed_x *= -1
        
    if ball.colliderect(opponent_paddle):
        ball_speed_x *= -1
        
    # Making the screen black
    window.fill((0, 0, 0))

    # Draw the game objects
    pygame.draw.rect(window, (255, 255, 255), player_paddle)
    pygame.draw.rect(window, (255, 255, 255), opponent_paddle)
    pygame.draw.ellipse(window, (255, 255, 255), ball)
    pygame.draw.aaline(window, (255, 255, 255), (window_width / 2, 0), (window_width / 2, window_height))
    
    # Draw the scores
    player_text = game_font.render(str(player_score), True, (255, 255, 255))
    opponent_text = game_font.render(str(opponent_score), True, (255, 255, 255))
    window.blit(player_text, (window_width / 4, 10))
    window.blit(opponent_text, (3*window_width / 4, 10))
    
    # Update the screen
    pygame.display.flip()

