class Block:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.is_hit = False

    def draw(self, surface):
        if not self.is_hit:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def hit(self):
        self.is_hit = True