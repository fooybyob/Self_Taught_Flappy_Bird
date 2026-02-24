class Pipe():
    WIDTH=8
    HEIGHT=1000
    GAP_SIZE=20
    SPEED=8
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(200, 800)
        self.passed = False

    def update(self):
        self.x-=self.SPEED

    def is_offscreen(self):
        return self.x+self.WIDTH<0;

    def collide(self,bird):
        
        if self.x<bird.x and bird.x<self.x_self.WIDTH: 
            
            top_pipe_bottom=self.gap_y-self.GAPSIZE //2
            bottom_pipe_top=self.gap_y+self.GAPSIZE //2

            if bird.y<top_pipe_bottom or bird.y>bottom_pipe_top:
                return True

        return False