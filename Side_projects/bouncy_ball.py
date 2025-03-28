import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Ball Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Character
character = pygame.Rect(screen_width // 2 - 50, screen_height - 50, 100, 10)

# Ball
ball = pygame.Rect(random.randint(0, screen_width - 20), 0, 20, 20)
ball_speed_x = 7  # Initial horizontal speed
ball_speed_y = 7  # Initial vertical speed

# Initialize variables
character_speed = 10
score = 0
missed_balls = 0
font = pygame.font.Font(None, 36)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character.left > 0:
        character.x -= character_speed
    if keys[pygame.K_RIGHT] and character.right < screen_width:
        character.x += character_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.left <= 0 or ball.right >= screen_width:
        # Reverse horizontal direction when hitting walls
        ball_speed_x = -ball_speed_x
        score += 1  # Gain points for bouncing off the board

    if ball.top <= 0:
        # Reverse vertical direction when hitting the top wall
        ball_speed_y = -ball_speed_y

    if ball.top > screen_height:
        ball = pygame.Rect(random.randint(0, screen_width - 20), 0, 20, 20)
        missed_balls += 1

        if missed_balls == 5:
            game_over_text = font.render("Game Over", True, white)
            score_text = font.render("Final Score: " + str(score), True, white)
            screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 20))
            screen.blit(score_text, (screen_width // 2 - 100, screen_height // 2 + 20))
            pygame.display.flip()
            pygame.time.delay(2000)  # Display the game over screen for 2 seconds
            pygame.quit()
            sys.exit()

    if character.colliderect(ball):
        # Reverse vertical direction when hitting the character
        ball_speed_y = -ball_speed_y

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, white, character)
    pygame.draw.ellipse(screen, red, ball)

    # Display missed ball tracker in the upper right corner
    missed_balls_text = font.render("Missed: " + str(missed_balls), True, white)
    screen.blit(missed_balls_text, (screen_width - 150, 10))

    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(30)
