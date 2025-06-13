import serial
import time

# Reading COM4
# Version 2

port = 'COM4'
baudrate = 9600
time_rec = 20

ser = serial.Serial(port, baudrate)

start = time.time()
cur_time = start

while cur_time - start < time_rec:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8', errors='replace').strip()
        print(line)
    cur_time = time.time()

ser.close()
