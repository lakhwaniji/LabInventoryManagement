import serial


def scanning_card():
    arduino = serial.Serial(port='/dev/cu.usbmodem11101', baudrate=9600)
    try:
        data = arduino.readline()
        data = str(data)
        data = data[3:-5]
        return data
    except:
        return "Failure"
