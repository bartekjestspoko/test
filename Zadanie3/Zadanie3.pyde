def setup():
    size(800,1000)
    textSize(150)
def draw():
    clear()
    B = text("B",width/2-50, height/2)
    G = text("G", width/2+50, height/2)
    print(hex(get(mouseX,mouseY)))
    print(keyPressed)
    print(keyCode)
    print(mouseX,mouseY)
    B
    G
    if keyPressed:
        if keyCode == 39: # to miało działąć tylko gdy coś już zaznaczone
            # dużo łatwiej jest najpierw wybrać kolor a później w nim napisać
            fill(100,200,300)
            B
            fill(200,255,50)
            G
        elif key =="B" or key=="b":
            fill(70,140,230)
            B
            fill(23,25,77)
            G
        elif keyCode == 37:
            fill(122,130,100)
            G
            fill(122,222,2)
            B
    elif (mouseX>(width/2-50)) and(mouseX<width/2) and (mouseY<height/2) and (mouseY>height/2-50):
        fill(23,130,150)
        B
        fill(45,35,200)
        G
    elif (mouseX>(width/2+50)) and (mouseX<width/2+50) and(mouseY<height/2) and (mouseY>height/2-50):
       fill(34,250,120)    
       G
       fill(250,26,254)
       B 
    else:
        fill(42,100,250)
    # miały reagować pojedyncze litery, a nie zawsze obie, ale ok
    # brak kształtu własnego podkreślającego
1pkt
