def setup():

    global zdjecie 
    size(1250/2,1300/2)
    noFill()
    strokeWeight(10)

def draw():
 
    global zdjecie
    zdjecie = loadImage("ptaszek.png")

    try:
        image(zdjecie,80,98,450,464)
    except:
        print ("Error!")
        stroke(155,100,15,10)
    else:
        stroke(10,55,500,80)
    finally:
        rect(20, 40,580,580)
# 1,25pkt    

               

    

    
