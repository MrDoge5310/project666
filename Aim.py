import pygame
from random import randint


class Aim:
    def __init__(self, src):
        self.src = src
        self.x = randint(0, 300)
        self.y = randint(0, 300)
        self.color = (255, 0, 0)

    def draw(self):
        pygame.draw.rect(self.src, self.color, (self.x, self.y, 20, 20))
