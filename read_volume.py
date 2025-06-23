import pyaudio
import wave
import pandas as pd

# Process csv file (that COM4 data was converted to)
# to get binary file

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
time_rec = 480

audio_path = 'audio/'
filename = "arduino_audio_COM4.wav"

filepath = audio_path + filename

wf = wave.open(filepath, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
wf.setframerate(RATE)

frames = []
df = pd.read_csv('data/arduino_COM4_bin.csv')
for i in range(len(df)):
    frames.append(str(df.iloc[i]['Volume']).encode('utf-8'))
    N = int(RATE * time_rec / len(df))
    if i + 1 == len(df):
        d = df.iloc[i]['Volume'] - df.iloc[i - 1]['Volume']
    else:
        d = df.iloc[i + 1]['Volume'] - df.iloc[i]['Volume']
    for j in range(N):
        frames.append('0.0'.encode('utf-8'))
        # frames.append(str(df.iloc[i]['Volume']).encode('utf-8'))
        # frames.append(str(df.iloc[i]['Volume'] + d * j / N).encode('utf-8'))

wf.writeframes(b'\n'.join(frames))
wf.close()
