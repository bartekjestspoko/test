from abc import ABCMeta, abstractmethod 
class Wild():
    __metaclass__=ABCMeta
    @abstractmethod 
    def definicja(self): 
        abc().__init__()
        return 'no sound'


class Monkey(Wild):
     def __init__(self, imie):
        self.imie = imie
     def definicja(self):
        text('wiifihi ahuoouooauuhheehee', random(105, width-1000), random(200, height-800))
        return 'wiifihi ahuoouooauuhheehee'
  
class Lion(Wild):
    def __init__(self, imie):
        self.imie = imie
    def definicja(self):
        text('awwwwww awwwwwww', random(100, width-1000), random(100, height-900))
        return 'awwwwww awwwwwww'
    def chcemmalpkie(self):
        image(loadImage("zwierzeta.jpg"), random(100, width-920), random(100, height-1200))
    def __add__(self, rozny):
        return self.imie[1]+ ' xd ' + rozny.imie[1]
class Malpka(Wild):
    pass
def setup():
    size(1200,1200)
    textSize(40)
    smieszek = Monkey('smieszek')
    grozny = Lion('grozny')
    global list_of_pets
    list_of_pets = [grozny, smieszek] 
    print(isinstance(smieszek, Wild))
    print(grozny+smieszek)
   
def draw(): 
    pass
    
def mouseClicked():
    for Wild in list_of_pets:
        Wild.definicja()
        if isinstance(Wild, Lion): 
            Wild.chcemmalpkie()
