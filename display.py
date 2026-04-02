import pygame
import math
from serialRead import init_serial, read_serial


def main():
    SerialCom = init_serial()
    cx = 300
    cy = 300
    radius = 200
    angle = 90
    increment = 1

    pygame.init()

    screen = pygame.display.set_mode((600,600))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (0,255,0), (cx,cy), 200, 1)

        data = read_serial(SerialCom)
        if data:
            angle, distance = data
            distance_radius = distance_map(distance)
        else:
            distance_radius = 0


        rad = math.radians(angle)
        x = cx + radius * math.cos(rad)
        y = cy - radius * math.sin(rad)

        x_dist = cx + distance_radius * math.cos(rad)
        y_dist = cy - distance_radius * math.sin(rad)

        pygame.draw.line(screen, (0,255,0), (cx,cy), (x,y), 1)
        if distance_radius > 0:
            pygame.draw.circle(screen, (0,255,0), (x_dist, y_dist), 8)
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

def distance_map(distance):
    # Map the distance to a radius between 0 and 200
    max_distance = 100  # Adjust this based on your sensor's max range
    return (distance / max_distance) * 200 if distance <= max_distance else 200


if __name__ == "__main__":
    main()