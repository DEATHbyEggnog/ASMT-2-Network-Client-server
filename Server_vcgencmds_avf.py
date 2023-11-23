import socket
import os
import json

s = socket.socket()
host = '10.102.13.65'
port = 5000
s.bind((host, port))
s.listen(5)

# gets the Core Temperature from Pi
measure_temp = os.popen('vcgencmd measure_temp').readline().replace("temp=", "").replace("'C\n", "")
# Display boolean power
display_power = os.popen('vcgencmd display_power').readline().strip()
# Display clock frequency 
measure_clock = os.popen('vcgencmd measure_clock arm').readline().strip()
#SDRAM Voltage
measure_volts = os.popen('vcgencmd measure_volts sdram_c').readline().strip()


# Dictionary with the data
data_dict = {
    "Temperature": measure_temp,
    "DisplayPower": display_power,
    "MeasureClock": measure_clock,
    "MeasureVolts": measure_volts
}

# Convert dictionary to JSON-formatted string
json_string = json.dumps(data_dict, indent=2)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    # Print the JSON string
    print(json_string)

    # Send the JSON string as bytes
    c.send(json_string.encode('utf-8'))

    # Close the connection after sending data
    c.close()
