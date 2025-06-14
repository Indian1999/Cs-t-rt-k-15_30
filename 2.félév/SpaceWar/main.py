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
METEOR_VELOCITY = 3

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

# class-on belül lévő függvények első paramétere: self
# self - meteorra utal (c# -ban a this)
class Meteor:
    # Konstruktór függvénynek, akkor fut le amikor létrehozunk egy meteort
    def __init__(self):
        MARGIN = 150
        METEOR_SIZE = 50
        x = random.randint(-MARGIN, WIDTH + MARGIN)
        y = random.randint(-MARGIN, HEIGHT + MARGIN)
        while x > 0 and x < WIDTH and y > 0 and y < HEIGHT:
            x = random.randint(-MARGIN, WIDTH + MARGIN)
            y = random.randint(-MARGIN, HEIGHT + MARGIN)   
        self.pos = (x,y)
        self.image = pygame.image.load(os.path.join(ASSETS_PATH, "meteor.png"))
        self.image = pygame.transform.scale(self.image, (METEOR_SIZE, METEOR_SIZE))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], METEOR_SIZE, METEOR_SIZE)
        self.new_direction()
    
    def new_direction(self):
        x = random.randint(100, WIDTH-100)
        y = random.randint(100, HEIGHT-100)
        v_x = x - self.pos[0]
        v_y = y - self.pos[1]
        v_length = (v_x**2 + v_y**2)**0.5 # feledik hatvány = gyökvonás
        self.x_vel = v_x / v_length * METEOR_VELOCITY
        self.y_vel = v_y / v_length * METEOR_VELOCITY
        
    def move(self):
        self.pos = (self.pos[0] + self.x_vel, self.pos[1] + self.y_vel)
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        if self.rect.x < -150 or self.rect.x > WIDTH + 150 or self.rect.y < -150 or self.rect.y > HEIGHT + 150:
            self.new_direction()


def draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, meteors):
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
        
    for meteor in meteors:
        window.blit(meteor.image, meteor.rect)
    
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

def handle_bullets(red_bullets, yellow_bullets, red, yellow, meteors):
    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.x < 0 - BULLET_WIDTH:
            red_bullets.remove(bullet)
        
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
            
    for meteor in meteors:
        if red.colliderect(meteor.rect):
            pygame.event.post(pygame.event.Event(RED_HIT))
            meteors.remove(meteor)
            meteors.append(Meteor())
        if yellow.colliderect(meteor.rect):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            meteors.remove(meteor)
            meteors.append(Meteor())
    
def draw_winner(text):
    font = pygame.font.SysFont("Arial", 40)
    winner_text = font.render(text, True, (255, 255, 255))
    window.blit(winner_text,
                (WIDTH // 2 - winner_text.get_width() // 2,
                 HEIGHT // 2 - winner_text.get_height() //2)
                )
    pygame.display.update()
    pygame.time.delay(5000)
    
def main():
    red = pygame.Rect(WIDTH - 150, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(150 - SPACESHIP_WIDTH, HEIGHT // 2 - SPACESHIP_HEIGHT // 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets = []
    yellow_bullets = []
    
    red_health = 10
    yellow_health = 10
    
    meteors = []
    for i in range(3):
        meteors.append(Meteor())
    
    while True:
        clock.tick(FPS) # FPS = 60 -> 1 másodperc 60-ad részét 'várakozunk'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < 3:
                    bullet = pygame.Rect(yellow.x + SPACESHIP_WIDTH, 
                                         yellow.y + SPACESHIP_HEIGHT // 2 - BULLET_HEIGHT // 2, 
                                         BULLET_WIDTH, BULLET_HEIGHT)
                    yellow_bullets.append(bullet)
                    FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < 3:
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
        handle_bullets(red_bullets, yellow_bullets, red, yellow, meteors)
        for meteor in meteors:
            meteor.move()
        draw_frame(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health, meteors)
        
        if red_health <= 0:
            draw_winner("Yellow Wins!")
            break
        if yellow_health <= 0:
            draw_winner("Red Wins!")
            break
        
# Ez a program belépési pontja
if __name__ == "__main__":
    main()


