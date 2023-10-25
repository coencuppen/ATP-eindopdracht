import random

def checkByteStuffing(func):
    def inner(*args, **kwargs):
        if [item1 == item2 for item1 in args[0][1:-1] for item2 in [0x7E, 0x7D, 0x11, 0x13]].__contains__(True):
            raise ValueError("Frame contains bytes that must be stuffed!")
        return func(*args, **kwargs)
    return inner

def giveRandomReading():
    return random.random() * 1000

def commandListSum(list, sum=0):
    return commandListSum(list[1:], sum+list[0]) if list else sum

def checkInvertedByte(list):
    return commandListSum(list[1:-2]) == 255 -list[-2]

@checkByteStuffing
def sendCommand(list):
    return checkInvertedByte(list)

def startMeasurement():
    return [0x7E, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x7E] if sendCommand([0x7E, 0x00, 0x00, 0x02, 0x01, 0x03, 0xF9, 0x7E]) else False

def stopMeasurement():
    return [0x7E, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x7E] if sendCommand([0x7E, 0x00, 0x01, 0x00, 0xFE, 0x7E]) else False

def readMeasurement():
    return giveRandomReading() if sendCommand([0x7E, 0x00, 0x01, 0x00, 0xFE, 0x7E]) else False