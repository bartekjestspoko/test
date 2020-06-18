add_library('pdf')
def setup():
    global zdj, ok, wasy
    size(400,514)
    zdj = loadImage("zdj.jpg")
    imageMode(CORNER)
    beginRecord(PDF, "ZdjPDF.pdf")
    ok= loadImage("ok.png") # przez to, że mają tło - przykrywają zdjęcie chłopca
    wasy= loadImage("wasy.png")
def draw():
    global zdj, ok, wasy
    image(zdj, 15,15, 400, 500) 
    if key == "1":
        image(ok, 20,100, 400, 450)
    elif key == "2":
        image(wasy, 20, 10,150, 40, 490) # za dużo argumentów, a nawet jeśli nie, to nie rysuje
def mousePressed():
    endRecord()
    exit()
    
#1,5pkt
# szkoda, że nie napisałeś z problemem wcześniej, miałeś otwarte dwa pliki (patrz zakładki w processingu), bo w folderze były utworzone dwa typu pythona. Kod był w drugim, a pierwszy był pusty, gdzie to pierwszy zawsze steruje okienkiem, jeżeli jest więcej niż jeden.
