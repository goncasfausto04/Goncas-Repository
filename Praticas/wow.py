import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Define screen dimensions and colors
screen_width, screen_height = 800, 600
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Create a display surface
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flashing Colors and Messages")

# List of random messages
messages = ["NIGGAS"]

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get a random color and message
    random_color = random.choice(colors)
    random_message = random.choice(messages)

    # Fill the screen with the random color
    screen.fill(random_color)

    # Create a font and text
    font = pygame.font.Font(None, 36)
    text = font.render(random_message, True, (255, 255, 255))

    # Get the text dimensions
    text_rect = text.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)

    # Blit the text onto the screen
    screen.blit(text, text_rect)

    pygame.display.flip()

    # Wait for a while (adjust the delay as needed)
    pygame.time.wait(1000)

# Quit pygame and exit the program
pygame.quit()
sys.exit()
