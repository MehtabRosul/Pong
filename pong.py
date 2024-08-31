import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pong Game")

# Paddle setup
paddle_width = 100
paddle_height = 10
paddle_x = (SCREEN_WIDTH - paddle_width) // 2
paddle_y = SCREEN_HEIGHT - 30
paddle_speed = 10

# Ball setup
ball_size = 20
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = random.choice([-5, 5])
ball_speed_y = -5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH - ball_size:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if paddle_y < ball_y + ball_size and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # Ball falls off the screen
    if ball_y >= SCREEN_HEIGHT:
        ball_x = SCREEN_WIDTH // 2
        ball_y = SCREEN_HEIGHT // 2
        ball_speed_y = -ball_speed_y

    # Clear screen
    screen.fill(BLACK)

    # Draw paddle
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.ellipse(screen, RED, (ball_x, ball_y, ball_size, ball_size))

    # Update screen
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
