import socket
from threading import Thread
import time

TRIM_MAX = 1000
TRIM_MIN = -1000
MSP_STATUS = 101

TCP_IP = '192.168.4.1'
TCP_PORT = 23

MSP_HEADER_IN = "244d3c"

MSP_FC_VERSION = 3
MSP_RAW_IMU = 102
MSP_RC = 105
MSP_ATTITUDE = 108
MSP_ALTITUDE = 109
MSP_ANALOG = 110
MSP_SET_RAW_RC = 200
MSP_ACC_CALIBRATION = 205
MSP_MAG_CALIBRATION = 206
MSP_SET_MOTOR = 214
MSP_SET_ACC_TRIM = 239
MSP_ACC_TRIM = 240
MSP_EEPROM_WRITE = 250
MSP_SET_POS = 216
MSP_SET_COMMAND = 217
MSP_SET_1WIRE = 243

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((TCP_IP, TCP_PORT))

def sendRequestMSP(data):
    client.send(bytes.fromhex(data))

def createPacketMSP(msp, payload):
    bf = ""
    bf += MSP_HEADER_IN

    checksum = 0
    if (msp == MSP_SET_COMMAND):
        pl_size = 1
    else:
        pl_size = len(payload) * 2

    bf += '{:02x}'.format(pl_size & 0xFF)
    checksum ^= pl_size

    bf += '{:02x}'.format(msp & 0xFF)
    checksum ^= msp

    for k in payload:
        if (msp == MSP_SET_COMMAND):
            bf += '{:02x}'.format(k & 0xFF)
            checksum ^= k & 0xFF
        else:
            bf += '{:02x}'.format(k & 0xFF)
            checksum ^= k & 0xFF
            bf += '{:02x}'.format((k >> 8) & 0xFF)
            checksum ^= (k >> 8) & 0xFF

    bf += '{:02x}'.format(checksum)

    return bf

def sendRequestMSP_SET_RAW_RC(channels):
    sendRequestMSP(createPacketMSP(MSP_SET_RAW_RC, channels))

def sendRequestMSP_SET_COMMAND(commandType):
    sendRequestMSP(createPacketMSP(MSP_SET_COMMAND, [commandType]))

def sendRequestMSP_GET_DEBUG(requests):
    for i in range(len(requests)):
        sendRequestMSP(createPacketMSP(requests[i], []))

def sendRequestMSP_SET_ACC_TRIM(trim_roll, trim_pitch):
    sendRequestMSP(createPacketMSP(MSP_ACC_TRIM, [trim_roll, trim_pitch]))

def sendRequestMSP_ACC_TRIM():
    sendRequestMSP(createPacketMSP(MSP_ACC_TRIM, []))

def sendRequestMSP_EEPROM_WRITE():
    sendRequestMSP(createPacketMSP(MSP_EEPROM_WRITE, []))

class pluto():
    def __init__(self):
        self.rcRoll = 1500
        self.rcPitch = 1500
        self.rcThrottle = 1500
        self.rcYaw = 1500
        self.rcAUX1 = 1500
        self.rcAUX2 = 1000
        self.rcAUX3 = 1500
        self.rcAUX4 = 1000
        self.commandType = 0
        self.droneRC = [1500,1500,1500,1500,1500,1000,1500,1000]
        self.NONE_COMMAND = 0
        self.TAKE_OFF = 1
        self.LAND = 2
        self.thread = Thread(target=self.writeFunction)
        self.thread.start()

    def arm(self):
        print("Arming")
        self.rcRoll = 1500
        self.rcYaw = 1500
        self.rcPitch = 1500
        self.rcThrottle = 1000
        self.rcAUX4 = 1500

    def box_arm(self):
        print("boxarm")
        self.rcRoll=1500
        self.rcYaw=1500
        self.rcPitch =1500
        self.rcThrottle = 1800
        self.rcAUX4 =1500

    def disarm(self):
        print("Disarm")
        self.rcThrottle = 1300
        self.rcAUX4 = 1200

    def forward(self):
        print("Forward")
        self.rcPitch = 1600

    def backward(self):
        print("Backward")
        self.rcPitch =1300

    def left(self):
        print("Left Roll")
        self.rcRoll =1200

    def right(self):
        print("Right Roll")
        self.rcRoll =1600

    def left_yaw(self):
        print("Left Yaw")
        self.rcYaw = 1300

    def right_yaw(self):
        print("Right Yaw")
        self.rcYaw = 1600

    def reset(self):
        self.rcRoll =1500
        self.rcThrottle =1500
        self.rcPitch =1500
        self.rcYaw = 1500
        self.commandType = 0

    def increase_height(self):
        print("Increasing height")
        self.rcThrottle = 1800

    def decrease_height(self):
        print("Decreasing height")
        self.rcThrottle = 1300

    def take_off(self):
        self.disarm()
        self.box_arm()
        print("take off")
        self.commandType = 1

    def land(self):
        self.commandType = 2

    def rcValues(self):
        return [self.rcRoll, self.rcPitch, self.rcThrottle, self.rcYaw,
                self.rcAUX1, self.rcAUX2, self.rcAUX3, self.rcAUX4]

    def trim_left_roll(self):
        print("Trimming Left Roll")
        self.rcRoll = max(TRIM_MIN, self.rcRoll + 100)

    def flip(self):
        print("Get Ready for the FLIP !!")
        sendRequestMSP_SET_COMMAND(3)
        sendRequestMSP_SET_RAW_RC([0, 0, 0, 0, 0, 0, 0, 0])

    def writeFunction(self):
        requests = [MSP_RC, MSP_ATTITUDE, MSP_RAW_IMU, MSP_ALTITUDE, MSP_ANALOG]
        sendRequestMSP_ACC_TRIM()

        while True:
            self.droneRC[:] = self.rcValues()

            sendRequestMSP_SET_RAW_RC(self.droneRC)
            sendRequestMSP_GET_DEBUG(requests)

            if (self.commandType != self.NONE_COMMAND):
                sendRequestMSP_SET_COMMAND(self.commandType)
                self.commandType = self.NONE_COMMAND

            time.sleep(0.022)
