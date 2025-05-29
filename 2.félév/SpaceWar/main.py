import pygame # pip install pygame
import os # Elérési útvonalakat tudjuk jól kezelni
import math
import random

# Ha egy változó csupa nagybetű, akkor azzal jelezzük, hogy ez egy konstans
# A konstansoknak nem változtatunk az értékén
WIDTH = 900
HEIGHT = 500
FPS = 60 # Frames per Second
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 80
VELOCITY = 5 # Az  úrhajók sebessége (pixel per frame)

clock = pygame.time.Clock() # példányosítjuk a Clock osztályt

window = pygame.display.set_mode((WIDTH, HEIGHT)) # létrehozzuk az ablakot
pygame.display.set_caption("Space War") # ablak neve

# Melyik mappában található az a file ami most fut?
ASSETS_PATH = os.path.dirname(os.path.abspath(__file__)) 
ASSETS_PATH = os.path.join(ASSETS_PATH, "Assets")

BACKGROUND = pygame.image.load(os.path.join(ASSETS_PATH, "space.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

RED_SPACESHIP = pygame.image.load(os.path.join(ASSETS_PATH, "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 90)

YELLOW_SPACESHIP = pygame.image.load(os.path.join(ASSETS_PATH, "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 270)

def draw_frame():
    window.blit(BACKGROUND, (0,0))
    
    window.blit(RED_SPACESHIP, (675, 250))
    window.blit(YELLOW_SPACESHIP, (225, 250))
    
    pygame.display.update() # frissíti a megjelenítést

def main():
    while True:
        clock.tick(FPS) # FPS = 60 -> 1 másodperc 60-ad részét 'várakozunk'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        draw_frame()
        
# Ez a program belépési pontja
if __name__ == "__main__":
    main()


