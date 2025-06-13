import serial.tools.list_ports
from matplotlib import pyplot as plt
import pandas as pd
import time

# Reading COM4
# Version 1

port = 'COM4'
time_rec = 480
baudrate = 9600
ser = serial.Serial(port, baudrate=baudrate)
start = time.time()

D = {'Time': [], 'Volume': []}
D_bin = {'Time': [], 'Volume': []}
cur_time = start

while cur_time - start < time_rec:
    data = ser.readline()
    try:
        num = float(data.decode('utf-8').strip())
    except BaseException:
        num = 0
    D['Time'].append(cur_time - start)
    D['Volume'].append(num)
    D_bin['Time'].append(cur_time - start)
    D_bin['Volume'].append(data)
    cur_time = time.time()
        
ser.close()

plt.title('Arduino Microphone')
plt.xlabel('Time')
plt.ylabel('Volume')

plt.plot(D['Time'], D['Volume'])
plt.show()

df = pd.DataFrame(D)
df.to_csv('data/arduino_COM4.csv')


df_bin = pd.DataFrame(D_bin)
# df_bin.to_csv('data/arduino_COM4_bin.csv', mode='wb')
