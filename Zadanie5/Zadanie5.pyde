global cWidth
global cHeight
q = 600
g = 1000
class player(object):
    def __init__(self):
        self.x = 290
        self.y = 470
        self.left = 0
        self.right= 0
        self.down = 0
        self.up = 0
        self.speed= 10
        self.b = 35
        self.g = 35
    def show(self):
        fill(1)
        rect(self.x,self.y,self.g,self.b)
    def update(self):
        self.x = self.x + (self.right - self.left)*self.speed
        self.y = self.y + (self.down - self.up)*self.speed
        if not (self.x >= 0):
            self.x = 0
        if not (self.x <= (q - self.g)):
            self.x = (q - self.g)
        if not (self.y >= 0):
            self.y = 0
        if not (self.y <= (g - self.b)):
            self.y = (g - self.b)
def setup():
    size(q,g)
    global t
    t = player() # miały być dwa obiekty tej klasy
    
def draw():
    background(412414)
    t.show()
    t.update()
    
def keyPressed():
    if keyCode == UP:
        t.up=1
    if keyCode == DOWN:
        t.down=1
    if keyCode == LEFT:
        t.left=1
    if keyCode == RIGHT:
        t.right=1
        
def keyReleased():
    if keyCode == UP:
        t.up=0
    if keyCode == DOWN:
        t.down=0
    if keyCode == LEFT:
        t.left=0
    if keyCode == RIGHT:
        t.right=0

# 1,75pkt, choć nie pierwszy raz widzę ten kod...
