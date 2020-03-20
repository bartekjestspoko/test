def setup():
        size(1000,1000)
def draw():
    rectMode(CORNERS)
    if mousePressed:
        rect (mouseX, mouseY, width/2*3, height/2*3) 
        #wysokośćdzielona na 2 to 500, a później *3 to 1500, więc rysowany kształt jest większy od ekranu
    else:
        clear()
#def mousePressed():
#    clear()

#2pkt
