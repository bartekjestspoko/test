add_library('pdf')
def setup():
    global zdj, ok, wasy
    size(400,514)
    zdj = loadImage("zdj.jpg")
    imageMode(CORNER)
    beginRecord(PDF, "ZdjPDF.pdf")
    ok= loadImage("ok.png")
    wasy= loadImage("wasy.png")
def draw():
    global zdj, ok, wasy
    image(zdj, 15,15, 400, 500) 
    if key == "1":
        image(ok, 20,100, 400, 450) 
    elif key == "2":
        image(wasy, 20, 10,150, 40, 490)
def mousePressed():
    endRecord()
    exit()
