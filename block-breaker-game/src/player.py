class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = 0

    def move_left(self, distance):
        self.x -= distance

    def move_right(self, distance):
        self.x += distance

    def draw(self, surface):
        # Code to draw the player on the given surface
        pass