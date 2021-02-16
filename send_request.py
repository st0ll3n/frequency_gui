import time
import struct
import serial
import csv
from datetime import datetime
from time import sleep
import variable_to_csv
variable_to_csv
from radio_variables_1 import hihihi
radio_send_set = 0
ser = serial.Serial('COM4', 19200, timeout=.1)
ser.setDTR(False)  # must have one or both of these to prevent random transmit
ser.setRTS(False)
while radio_send_set < len(hihihi):
    send_data = int(bytes(hihihi[radio_send_set], 'UTF-8'), 0)
    send_byte = struct.pack('>B', send_data)
    ser.write(send_byte)
    radio_send_set += 1
sleep(.1)
ser_bytes = ser.read(100)
serial_string = ""
for x in ser_bytes:
    serial_string = serial_string + "/ " + (hex(x))
with open("frequency_save.csv", "a") as frequency_save:
    write = csv.writer(frequency_save)
    timestamp = (time.time())
    date_time = datetime.fromtimestamp(timestamp)
    write.writerow([date_time, serial_string])
    #  print(ser_bytes) Just for testing
    #  todo: fix the removal of 0 at the end of what is printed or saved to file
ser.close()
