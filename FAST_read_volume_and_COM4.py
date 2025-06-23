import serial
import wave
import time
import datetime as dt

# Reading the signal from Serial (fast reading from Arduino)

audio_path = 'audio/'
filename = 'output.wav'

port = 'COM4'
filepath = audio_path + filename
baudrate = 115200
try:
    time_rec = int(input('Print time of recording [seconds]: '))
except ValueError:
    time_rec = 60
inc_factor = 50
# inc_factor = 5

sample_rate = 10000
num_channels = 1
sampwidth = 2

# Read timeout
ser = serial.Serial(port, baudrate, timeout=1)

# To count the number of processed frames
frame_count = 0

with wave.open(filepath, 'w') as wf:
    wf.setnchannels(num_channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(sample_rate)
    
    a = []

    try:
        print('Reading data from the microphone', flush=True)
        time_sec = time_rec
        end_time = time.time() + time_rec
        while time.time() < end_time:
            if abs(time_sec + time.time() - end_time) < 0.1:
                print(dt.timedelta(seconds=time_sec), flush=True)
                time_sec -= 1
            if ser.in_waiting > 0:
                data = ser.readline().strip()
                try:
                    value = int(data) * inc_factor
                    # wf.writeframes(value.to_bytes(2, byteorder='little', signed=True))
                    a.append(value.to_bytes(2, byteorder='little', signed=True))
                    frame_count += 1
                except ValueError:
                    continue
    except KeyboardInterrupt:
        print("Interrupted by the user", flush=True)
    finally:
        print('The end of reading data from the microphone', flush=True)
        ser.close()
    
    # The number of additional recordings to bring the length of the audio 
    # file to the required length time_rec
    # num = 1
    num = int(time_rec * sample_rate / frame_count)
    print(f'Start writing to a file {filepath}', flush=True)
    for i in range(frame_count):
        for j in range(num):
            wf.writeframes(a[i])

print("Recording completed", flush=True)
print(f"Number of processed frames: {frame_count}", flush=True)
# print(f"Expected recording time: {frame_count / sample_rate} секунд", flush=True)
