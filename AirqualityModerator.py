import FanControl
import SPS30Control
import PS4VOC100MODControl
import AirFilteringSystemControl

def sumReadings(func, numberOfReadings, list = []):
    list.append(func())
    return list if numberOfReadings == 1 else sumReadings(func, numberOfReadings-1, list)
    
def averageList(list):
    return sum(list) / len(list)

def controlFilter(bool):
    AirFilteringSystemControl.write(bool)

def activateFan(speed):
    FanControl.write(speed)

def moderate():
    readingsSPS30 = averageList(sumReadings(SPS30Control.readMeasurement, 10))
    readingsPS4 = averageList(sumReadings(PS4VOC100MODControl.read, 10))
    if readingsSPS30 > 500 or readingsPS4 > 50:
        controlFilter(True)
        activateFan((readingsSPS30 + readingsPS4) - 550)
    if readingsSPS30 < 300 and readingsPS4 < 30:
        controlFilter(False)
        activateFan(0)

    return 0

def main():
    while 1:
        moderate()
    return 0

if __name__ == '__main__':
    main()