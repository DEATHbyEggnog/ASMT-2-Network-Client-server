
#Runs on PC
#The Client

import socket
import json
import time

s = socket.socket()
host = '10.102.13.65'
port = 5000
s.connect((host, port))

while True:
    data = s.recv(1024).decode()
    if not data:
        s.close()
        break
    
    data_dict = json.loads(data)
    #print data collected
    print("Core Temperature: {} C".format(data_dict["Temperature"]))
    print("Display Power: {} ".format(data_dict["DisplayPower"]))
    print("Clock Frequency: {} Hz" .format(data_dict["MeasureClock"]))
    print("DRAM Voltage: {} V" .format(data_dict["MeasureVolts"]))

s.close()

time.sleep(5)
