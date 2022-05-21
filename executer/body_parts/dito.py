class Dito:
    def __init__(self, pin, position, board):
        self._pin = pin
        self._position = position
        self._board = board
        self._board.set_pin_mode_servo(pin_number=pin)
    def getPin(self):
        return self._pin
    
    def move(self, angle):
        self._board.servo_write(self._pin, angle)






