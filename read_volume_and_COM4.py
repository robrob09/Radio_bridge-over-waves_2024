import serial.tools.list_ports
from matplotlib import pyplot as plt
import pandas as pd
import time
import pyaudio
import wave

# read_volume.py & Arduino_read_com4_V1.py
# A file to read values from COM4 and write 
# them to a .wav audio file.

port = 'COM4'
time_rec = 20
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
df.to_csv('data/arduino_com4.csv')

df_bin = pd.DataFrame(D_bin)
# df_bin.to_csv('data/arduino_com4_bin.csv', mode='wb')

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
time_rec = 20

audio_path = 'audio/'
filename = "arduino_audio_com4.wav"

filepath = audio_path + filename

wf = wave.open(filepath, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
wf.setframerate(RATE)

frames = []
df = pd.read_csv('data/arduino_com4_bin.csv')
for i in range(len(df)):
    frames.append(str(df.iloc[i]['Volume']).encode('utf-8'))
    N = int(44100 * time_rec / len(df))
    if i + 1 == len(df):
        d = df.iloc[i]['Volume'] - df.iloc[i - 1]['Volume']
    else:
        d = df.iloc[i + 1]['Volume'] - df.iloc[i]['Volume']
    for j in range(N):
        frames.append(str(df.iloc[i]['Volume']).encode('utf-16'))
        # frames.append(str(df.iloc[i]['Volume'] + d * j / N).encode('utf-8'))

wf.writeframes(b'\n'.join(frames))
wf.close()
