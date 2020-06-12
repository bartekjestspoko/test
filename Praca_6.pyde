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
         Kw.sketch(self, a, b)
         fill(random(220), 44, 12)
         rect(self.a, self.b, self.krawedz, self.krawedz)
    
def setup():
    size(800, 800)
    smalKolorowyKw = KolorowyKw(30.64) 
    smalKolorowyKw.sketchKolorowy(random(123), 12, 51) 
    smalKolorowyKw.sketchKolorowy(random(13),26, 75) 
    bigKolorowyKw = KolorowyKw(140.54)
    bigKolorowyKw.sketchKolorowy(random(245), 46, 109)
    bigKolorowyKw.sketch(random(50), 40) 
