def giveRandomReading():
    return 0

def commandListSum(list, sum=0):
    return commandListSum(list[1:], sum+list[0]) if list else sum

def checkInvertedByte(list):
    return commandListSum(list[1:-2]) == 255 -list[-2]

def sendCommand(list):
    return 0


print(checkInvertedByte([0x7E, 0x00, 0x00, 0x02, 0x01, 0x03, 0xF9, 0x7E]))