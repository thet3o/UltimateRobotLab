import body_controller as bc
import time

#Finger Movement
def moveFinger(handPosition, finger, degrees):
    _finger = int(finger)
    _degrees = int(degrees)
    if handPosition == 'left':
        bc.lM.move_finger(_finger, _degrees)
    elif handPosition == 'right':
        bc.rM.move_finger(_finger, _degrees)
    time.sleep(0.5)
    
#Hand Movement
def moveHand(handPosition, degrees):
    _degrees = int(degrees)
    if handPosition == 'left':
        bc.lM.move(_degrees)
    elif handPosition == 'right':
        bc.rM.move(_degrees)
    time.sleep(0.5)