class Moteur:
    def __init__(self,pinVcc,pinGnd,pinVccEnc,pinGndEnc,pinAnalog) :
        self.pinVcc=pinVcc
        self.pinGnd=pinGnd
        self.pinVccEnc=pinVccEnc
        self.pinGndEnc=pinGndEnc
        self.pinAnalog=pinAnalog
        self.pos = None

    def pos(self):
        print(f"La position encoyé par {self.pinAnalog} est : {self.pos}")

    def turnR(self):
        print(f"Je tourne vers la droite avec la valeur de {self.pinVcc} ")

    def turnL(self):
        print(f"Je tourne vers la gauche avec la valeur de {self.pinVcc} ")
