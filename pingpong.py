from pygame import *
from random import randint
from time import time as timer
font.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_i] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < 350:
            self.rect.y += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Shooter Game')

background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))

stick1 = Player('stick.png', -20, 30, 200, 150, 2)
stick2 = Enemy('stick.png', 540, 30, 200, 150, 2)


game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        stick1.update()
        stick1.reset()
        stick2.update()
        stick2.reset()

    display.update()
       
