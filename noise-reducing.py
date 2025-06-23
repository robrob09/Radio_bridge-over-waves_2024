import noisereduce as nr
import soundfile as sf
import librosa
import speech_recognition as sr
# do not forget to install "pip install pocketsphinx"

# Attempt to reduce noise


audio_path = 'audio/'

# filename = 'Arduino_counting[Me].wav'
filename = input('Please, print filename: ')

if filename == '':
    filename = 'Apricot stone.wav'

filepath = audio_path + filename

# noise-reducing
audio_data, sample_rate = librosa.load(filepath)
reduced_noise_audio_data = nr.reduce_noise(y=audio_data, sr=sample_rate)
reduced_noise_filepath = audio_path + 'reduced_noise_' + filename
sf.write(reduced_noise_filepath, reduced_noise_audio_data, sample_rate)
