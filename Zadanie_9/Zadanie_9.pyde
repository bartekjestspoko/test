def setup():

    global zdjecie 
    size(1250/2,1300/2)
    noFill()

def draw():
 
    global zdjecie
    zdjecie = loadImage("ptaszek.png")

    try:
        image(zdjecie,80,98,450,464)
        f = open("ptaszek.png")
        if f.name == 'ptaszek.png':
            raise Exception


    
    except:
        print ("Error!")
        rect(20, 40,580,580)
        fill (10,55,500,80)
        stroke(10,5,183,405)
    
    else:
        rect(50, 50,490,550)
        
        stroke(155,100,15,10)
        

               

    

    
