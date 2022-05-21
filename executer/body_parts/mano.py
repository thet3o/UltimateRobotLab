import dito

class Mano(dito.Dito):
    def __init__(self, pin, position, dita: []):
        self._pin = pin
        self._position = position
        self._dita = dita

    def move_finger(self, index, angle):
        self._dita[index-1].move(angle)




