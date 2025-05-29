import pygame # pip install pygame
import os # Elérési útvonalakat tudjuk jól kezelni
import math
import random

# Ha egy változó csupa nagybetű, akkor azzal jelezzük, hogy ez egy konstans
# A konstansoknak nem változtatunk az értékén
WIDTH = 900
HEIGHT = 500
FPS = 60 # Frames per Second

clock = pygame.time.Clock() # példányosítjuk a Clock osztályt

window = pygame.display.set_mode((WIDTH, HEIGHT)) # létrehozzuk az ablakot
pygame.display.set_caption("Space War") # ablak neve

# Melyik mappában található az a file ami most fut?
ASSETS_PATH = os.path.dirname(os.path.abspath(__file__)) 
ASSETS_PATH = os.path.join(ASSETS_PATH, "Assets")

BACKGROUND = pygame.image.load(os.path.join(ASSETS_PATH, "space.png"))

def main():
    while True:
        clock.tick(FPS) # FPS = 60 -> 1 másodperc 60-ad részét 'várakozunk'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
# Ez a program belépési pontja
if __name__ == "__main__":
    main()


