import time
import body_controller as bc
import basicActions as ba

def read(actionFile):
    actions = []
    with open(actionFile, 'r') as f:
        for line in f:
            actions.append(line.strip())
    return actions

def executer(actions = []):
    for action in actions:
        finger = action.split(' ')[1]
        degrees = action.split(' ')[2]
        if 'moveLeftHand' in action:
            ba.moveHand('left', degrees)
        elif 'moveLeftFinger' in action:
            ba.moveFinger('left', finger, degrees)
        elif 'moveRightHand' in action:
            ba.moveHand('right', degrees)
        elif 'moveRightFinger' in action:
            ba.moveFinger('right', finger, degrees)
        elif 'speck' in action:
            pass