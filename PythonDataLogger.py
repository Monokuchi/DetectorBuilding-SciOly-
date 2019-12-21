import serial
import sys
from serial.tools.list_ports import comports
import time

import logging
logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s \t %(message)s', "%Y-%m-%d %H:%M:%S")
# create file handler which logs even debug messages
fh = logging.FileHandler('C:\\temp\\arduino_adc.csv')
fh.setLevel(logging.INFO)
# create console handle
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)

class Communications:
    def __init__(self):
        self.SerialPort = serial.Serial()
        self.SerialPort.baudrate = 9600
        self.SerialPort.write_timeout = 0.1
        self.getListofPorts()
        self.openPort()

    def __del__(self):
        if self.SerialPort.is_open:
            self.SerialPort.close()

    def getListofPorts(self):
        ports = comports()
        for port in ports:
            print(port)
        return ports

    def openPort(self, port_name="COM3"):
        self.SerialPort.port = port_name
        self.SerialPort.open()

    def sendData(self, vals: bytearray):
        self.SerialPort.write(vals)

    def getBytesAvailableToRead(self):
        data = list()
        while self.SerialPort.in_waiting:
            data.append(float(self.SerialPort.readline()))
        return data

if __name__ == "__main__":
    comm = Communications()
    while True:
        data = comm.getBytesAvailableToRead()
        for d in data:
            logger.info(d)
        time.sleep(0.1)
