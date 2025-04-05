import pygame
import time

# Initialize pygame
pygame.init()

# Constants
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 20
ERASER_SIZE = 20

# Colors
BLUE = (0, 0, 255)    # grid cells
GREEN = (0, 255, 0)   # background
RED = (255, 0, 0)     # eraser

# Set up screen
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))   
pygame.display.set_caption("Drawing App")

# Create grid
grid = []
for row in range(0, CANVA_HEIGHT // CELL_SIZE):
    for col in range(0, CANVA_WIDTH // CELL_SIZE):
        rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

# Create eraser
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

# Main loop
running = True
while running:
    screen.fill(GREEN)

    # Draw grid
    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    # Update eraser position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)

    # Erase grid cells under eraser
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):  # Correct method
            new_grid.append(rect)
    grid = new_grid

    # Draw eraser
    pygame.draw.rect(screen, RED, eraser)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.05)  # Small delay

# Quit pygame
pygame.quit()
