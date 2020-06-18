class Kw():
    def __init__(self, krawedz):
        self.krawedz = krawedz
    def sketch(self, a, b):
        self.a = a
        self.b = b
        rect(self.a, self.b, self.krawedz, self.krawedz)
        
class KolorowyKw(Kw):
    def sketchKolorowy(self):
        Kw.sketch(self, a, b)
    def sketchKolorowy(self, a, b, kolory):
         fill(random(220), 44, 12) # wypadałoby później przywróćić kolor pierwotny, bo wszystkie rysujące się figury będą od teraz w tym kolorze
         Kw.sketch(self, a, b) # to już rysuje kwadrat, nie ma potrzeby ponownego używania rect
    
def setup():
    size(800, 800)
    smalKolorowyKw = KolorowyKw(30.64) 
    smalKolorowyKw.sketchKolorowy(random(123), 12, 51) 
    smalKolorowyKw.sketchKolorowy(random(13),26, 75) 
    bigKolorowyKw = KolorowyKw(140.54)
    bigKolorowyKw.sketchKolorowy(random(245), 46, 109)
    bigKolorowyKw.sketch(random(50), 40)
    
# 1,5pkt 
