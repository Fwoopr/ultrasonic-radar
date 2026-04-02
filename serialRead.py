from serial.tools import list_ports
import serial
import time


# List available serial ports
ports = list_ports.comports()

for port in ports:
    print(port)

def init_serial():
    SerialCom = serial.Serial('/dev/cu.usbserial-A50285BI', 115200, timeout=0.1)
    SerialCom.setDTR(False)
    time.sleep(1)
    SerialCom.flushInput()
    SerialCom.setDTR(True)
    return SerialCom


def read_serial(SerialCom):
    try:
        s_bytes = SerialCom.readline() # Read a line of data from the serial port
        s = s_bytes.decode('utf-8').rstrip('\r\n') # Decode the bytes to a string and remove the newline character

        angle, distance = map(float, s.split(',')) # Split the string by comma and convert to float
        return angle, distance

    except:
        return None

if __name__ == "__main__":
    SerialCom = init_serial()
    while True:
        read_serial(SerialCom)