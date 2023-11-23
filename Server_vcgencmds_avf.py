import socket
import os
import json
import time

s = socket.socket()
host = '10.102.13.65'
port = 5000
s.bind((host, port))
s.listen(5)

def get_pi_data():
    # gets the Core Temperature from Pi
    measure_temp = os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", "")
     # Returns a boolean value
    display_power = os.popen('vcgencmd display_power').readline().strip()
    # Measure ARM clock frequency
    measure_clock = os.popen('vcgencmd measure_clock arm').readline().strip()
    # Measure sdram voltage
    measure_volts = os.popen('vcgencmd measure_volts sdram_c').readline().strip()  

    return {
        "Temperature": measure_temp,
        "DisplayPower": display_power,
        "MeasureClock": measure_clock,
        "MeasureVolts": measure_volts
    }

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # continuously send updated information every 2 seconds
    while True:
        data_dict = get_pi_data()

        # Convert dictionary to JSON-formatted string
        json_string = json.dumps(data_dict, indent=2)

        # Send the JSON string as bytes
        c.send(json_string.encode('utf-8'))

        # Wait for a few seconds before sending updated information
        time.sleep(2)
