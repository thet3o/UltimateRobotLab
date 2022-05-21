from telemetrix import telemetrix
import time
import body_parts.dito as dito
import body_parts.mano as mano


board2 = telemetrix.Telemetrix(arduino_instance_id=2, arduino_wait=1)
board1 = telemetrix.Telemetrix(arduino_instance_id=1, arduino_wait=1)

def checkArduinos():
    '''board1.digital_write(13, 1)
    time.sleep(1)
    board1.digital_write(13, 0)'''
    time.sleep(2)
    board2.digital_write(13, 1)
    time.sleep(1)
    board2.digital_write(13, 0)

#Limbs Setup (first character is the side, second character MAIUSC is the type, third character is the number of the limb)
lD1 = dito.Dito(2, 0, board2)
lD2 = dito.Dito(3, 0, board2)
lD3 = dito.Dito(4, 0, board2)
lD4 = dito.Dito(5, 0, board2)
lD5 = dito.Dito(6, 0, board2)

lM = mano.Mano(8, 0, [lD1, lD2, lD3, lD4, lD5])

rD1 = dito.Dito(2, 1, board1)
rD2 = dito.Dito(3, 1, board1)
rD3 = dito.Dito(4, 1, board1)
rD4 = dito.Dito(5, 1, board1)
rD5 = dito.Dito(6, 1, board1)

rM = mano.Mano(8, 0, [rD1, rD2, rD3, rD4, rD5])