import pygame # pip install pygame
import os # Elérési útvonalakat tudjuk jól kezelni
import math
import random
pygame.mixer.init()
pygame.font.init()

# Ha egy változó csupa nagybetű, akkor azzal jelezzük, hogy ez egy konstans
# A konstansoknak nem változtatunk az értékén
WIDTH = 900
HEIGHT = 500
FPS = 60 # Frames per Second
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 80
VELOCITY = 5 # Az  úrhajók sebessége (pixel per frame)
BULLET_WIDTH = 10
BULLET_HEIGHT = 5
BULLET_VELOCITY = 8

HEALTH_FONT = pygame.font.SysFont("Arial", 24)

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

clock = pygame.time.Clock() # példányosítjuk a Clock osztályt

window = pygame.display.set_mode((WIDTH, HEIGHT)) # létrehozzuk az ablakot
pygame.display.set_caption("Space War") # ablak neve

# Melyik mappában található az a file ami most fut?
ASSETS_PATH = os.path.dirname(os.path.abspath(__file__)) 
ASSETS_PATH = os.path.join(ASSETS_PATH, "Assets")

HIT_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_PATH, "explosion.wav"))
FIRE_SOUND = pygame.mixer.Sound(os.path.join(ASSETS_PATH, "laser.wav"))

BACKGROUND = pygame.image.load(os.path.join(ASSETS_PATH, "space.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

RED_SPACESHIP = pygame.image.load(os.path.join(ASSETS_PATH, "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 90)

YELLOW_SPACESHIP = pygame.image.load(os.path.join(ASSETS_PATH, "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 270)

def draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    window.blit(BACKGROUND, (0,0))
    
    window.blit(RED_SPACESHIP, (red.x, red.y))
    window.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), True, (255, 255, 255))
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), True, (255, 255, 255))
    window.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    window.blit(yellow_health_text, (10, 10))
    
    for bullet in red_bullets:
        pygame.draw.rect(window, (255, 0, 0), bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(window, (255, 255, 0), bullet)
    
    pygame.display.update() # frissíti a megjelenítést

def red_control(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x >= WIDTH // 2:
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x <= WIDTH - SPACESHIP_WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y >= 0:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y <= HEIGHT - SPACESHIP_HEIGHT:
        red.y += VELOCITY

def yellow_control(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x >= 0:
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x <= WIDTH // 2 - SPACESHIP_WIDTH:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y >= 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y <= HEIGHT - SPACESHIP_HEIGHT:
        yellow.y += VELOCITY

def handle_bullets(red_bullets, yellow_bullets, red, yellow):
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
    
def main():
    red = pygame.Rect(WIDTH - 150, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(150 - SPACESHIP_WIDTH, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    red_health = 10
    yellow_health = 10
    
    while True:
        clock.tick(FPS) # FPS = 60 -> 1 másodperc 60-ad részét 'várakozunk'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    bullet = pygame.Rect(yellow.x + SPACESHIP_WIDTH, 
                                         yellow.y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2, 
                                         BULLET_WIDTH, BULLET_HEIGHT)
                    yellow_bullets.append(bullet)
                    FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(red.x, 
                                         red.y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2,
                                         BULLET_WIDTH, BULLET_HEIGHT)
                    red_bullets.append(bullet)
                    FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                HIT_SOUND.play()
        
        keys_pressed = pygame.key.get_pressed()
        red_control(keys_pressed, red)
        yellow_control(keys_pressed, yellow)
        handle_bullets(red_bullets, yellow_bullets, red, yellow)
        draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        
# Ez a program belépési pontja
if __name__ == "__main__":
    main()


