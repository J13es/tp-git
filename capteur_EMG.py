class EMG:
    def __init__(self, Vcc, Vgnd):
        self.Vcc = Vcc
        self.Vgnd = Vgnd

class EMGT(EMG):
    def __init__(self, Vcc, Vgnd, pinT):
        super().__init__(Vcc, Vgnd)
        self.pinT = pinT

    def read_signal(self): 
        print(f"Je lis la valeur {self.pinT}")

class EMGB(EMG):
    def __init__(self, Vcc, Vgnd, pinB):
        super().__init__(Vcc, Vgnd)
        self.pinB = pinB

    def read_signal(self):
        print(f"Je lis la valeur {self.pinB}")
