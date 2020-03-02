def setup():
        size(1000,1000)
def draw():
    rectMode(CORNERS)
    if mousePressed:
        rect (mouseX, mouseY, width/2*3, height/2*3)
def mousePressed():
    clear()
