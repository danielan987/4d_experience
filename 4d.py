# Import packages
import pygame
import numpy as np
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("4th Dimension Experience")

# Define colours
white = (255, 255, 255)
black = (0, 0, 0)

# Set up clock
clock = pygame.time.Clock()

# Tesseract vertices
vertices = np.array([
    [1, 1, 1, 1],
    [-1, 1, 1, 1],
    [1, -1, 1, 1],
    [-1, -1, 1, 1],
    [1, 1, -1, 1],
    [-1, 1, -1, 1],
    [1, -1, -1, 1],
    [-1, -1, -1, 1],
    [1, 1, 1, -1],
    [-1, 1, 1, -1],
    [1, -1, 1, -1],
    [-1, -1, 1, -1],
    [1, 1, -1, -1],
    [-1, 1, -1, -1],
    [1, -1, -1, -1],
    [-1, -1, -1, -1]
])

# Define edges
edges = [
    (0, 1), (0, 2), (0, 4), (0, 8),
    (1, 3), (1, 5), (1, 9),
    (2, 3), (2, 6), (2, 10),
    (3, 7), (3, 11),
    (4, 5), (4, 6), (4, 12),
    (5, 7), (5, 13),
    (6, 7), (6, 14),
    (7, 15),
    (8, 9), (8, 10), (8, 12),
    (9, 11), (9, 13),
    (10, 11), (10, 14),
    (11, 15),
    (12, 13), (12, 14),
    (13, 15),
    (14, 15)
]

# Run functions
def projection(point, angle_x, angle_y, angle_z):
    rotation_x = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x), 0],
        [0, np.sin(angle_x), np.cos(angle_x), 0],
        [0, 0, 0, 1]
    ])
    rotation_y = np.array([
        [np.cos(angle_y), 0, np.sin(angle_y), 0],
        [0, 1, 0, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y), 0],
        [0, 0, 0, 1]
    ])
    rotation_z = np.array([
        [np.cos(angle_z), -np.sin(angle_z), 0, 0],
        [np.sin(angle_z), np.cos(angle_z), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    rotated_point = np.dot(rotation_x, point)
    rotated_point = np.dot(rotation_y, rotated_point)
    rotated_point = np.dot(rotation_z, rotated_point)
    distance = 5
    factor = distance / (distance - rotated_point[3])
    projected_point = np.array([
        factor * rotated_point[0],
        factor * rotated_point[1],
        factor * rotated_point[2]
    ])
    return projected_point

def main():
    angle_x, angle_y, angle_z = 0, 0, 0
    running = True
    while running:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        angle_x += 0.01
        angle_y += 0.01
        angle_z += 0.01
        projected_points = [projection(v, angle_x, angle_y, angle_z) for v in vertices]
        for edge in edges:
            points = []
            for vertex in edge:
                x = int(projected_points[vertex][0] * 100) + width // 2
                y = int(projected_points[vertex][1] * 100) + height // 2
                points.append((x, y))
            pygame.draw.line(screen, white, points[0], points[1], 1)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
