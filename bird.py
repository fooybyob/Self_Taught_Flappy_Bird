class Bird:
    GRAVITY = 0.5
    HEIGHT=1000

    def __init__(self):
        self.x=100
        self.y = 200
        self.velocity = 0
        self.alive = True
        self.score = 0
        self.fitness = 0

    def jump(self):
        self.velocity = -8

    def update(self):
        self.velocity += self.GRAVITY
        self.y += self.velocity

    def check_bounds(self):
        if self.y<0 or self.y> self.HEIGHT:
            self.alive=False
