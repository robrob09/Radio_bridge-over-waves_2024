import speech_recognition as sr
from pydub import AudioSegment
import librosa
import noisereduce as nr
import soundfile as sf
import os
import warnings

warnings.filterwarnings('ignore')

# Using Google API (online) to recognize speech

audio_path = 'audio/'
filename = input('Please, print filename: ')
if filename == '':
    filename = "Arduino_Text[Me].wav"

filepath = audio_path + filename

# noise reducing
# commented, because it makes quality worse

# audio_data, sample_rate = librosa.load(filepath)
# reduced_noise_audio_data = nr.reduce_noise(y=audio_data, sr=sample_rate)
# audio_file = audio_path + 'reduced_noise_' + filename
# sf.write(audio_file, reduced_noise_audio_data, sample_rate)

# Comment this line, if using moise reducing
audio_file = filepath

audio = AudioSegment.from_wav(audio_file)

temp_file = audio_path + "temp.wav"
audio.export(temp_file, format="wav")

r = sr.Recognizer()

with sr.AudioFile(temp_file) as source:
    audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data, language="ru-RU")
        print(text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {str(e)}")

# os.remove(audio_file)
os.remove(temp_file)
