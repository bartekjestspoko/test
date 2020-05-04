def setup():
    size(800,1000)
    textSize(150)
def draw():
    clear()
    print(hex(get(mouseX,mouseY)))
    print(keyPressed)
    print(keyCode)
    print(mouseX,mouseY)
    B = text("B",width/2-50, height/2)
    G = text("G", width/2+50, height/2)
    if keyPressed:
        if keyCode == 39:
            B=text("B", width/2+50, height/2)
            fill(100,200,300)
            G=text("G", width/2+50, height/2)
            fill(200,255,50)
        elif key =="B" or key=="b":
            B=text("B", width/2+50, height/2)
            fill(70,140,230)
            G=text("G", width/2-50, height/2)
            fill(23,25,77)
        elif keyCode == 37:
            G=text("G", width/2-50, height/2)
            fill(122,130,100)
            B=text("B", width/2+50, height/2)
            fill(122,222,2)
    elif (mouseX>(width/2-50)) and(mouseX<width/2) and (mouseY<height/2) and (mouseY>height/2-50):
        B=text("B",width/2-50,height/2)
        fill(23,130,150)
        G=text("G", width/2+50, height/2)
        fill(45,35,200)
    elif (mouseX>(width/2+50)) and (mouseX<width/2+50) and(mouseY<height/2) and (mouseY>height/2-50):
       G=text("G", width/2+50, height/2)
       fill(34,250,120)    
       B=text("B",width/2-50,height/2)  
       fill(250,26,254)   
    else:
        fill(42,100,250)
