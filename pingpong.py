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
ball = GameSprite('ball.png', 100, 200, 100,100, 1)

stick1 = Player('stick.png', 20, 30, 50, 150, 2)
stick2 = Enemy('stick.png', 640, 30, 50, 150, 2)

font1 = font.Font(None, 35)
lose = font1.render('YOU LOSE', True, (255, 100, 100))


speed_x = 1
speed_y = 1


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
        ball.update()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        stick1.update()
        stick1.reset()
        stick2.update()
        stick2.reset()
        if ball.rect.y > win_height-30 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(stick1, ball) or sprite.collide_rect(stick2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.x > 700 or ball.rect.x < -20:
            finish = True
            window.blit(lose, (300,220))


    display.update()
       
