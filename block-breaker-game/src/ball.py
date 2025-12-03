class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = 0
        self.dy = 0

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0