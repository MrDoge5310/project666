import pygame


class Robot:
    def __init__(self, src, x, y):
        self.src = src
        self.x = x
        self.y = y
        self.color = (255, 255, 0)

    def draw(self):
        pygame.draw.rect(self.src, self.color, (self.x, self.y, 20, 20))

    def move(self, dir_):
        # закрашиваем предыдущую позицию
        pygame.draw.rect(self.src, (0, 0, 0), (self.x, self.y, 20, 20))

        if dir_ == "влево":
            self.x -= 20
        elif dir_ == "вправо":
            self.x += 20
        elif dir_ == "вверх":
            self.y -= 20
        elif dir_ == "вниз":
            self.y += 20