import os
import speech_recognition as sr
# do not forget to install "pip install pocketsphinx"

# Using pocketsphinx (offline) to recognize speech

# Initialize the recognizer
r = sr.Recognizer()

audio_path = 'audio/'
filename = input('Please, print filename: ')
if filename == '':
    filename = "Arduino_Counting[Me].wav"

filepath = audio_path + filename

# Folder, that contains:
# ru-RU/
#  └ acoustic-model/
#     └ (...)
#    └ pronunciation-dictionary.dict
#    └ language-model.lm.bin
model_path = 'ru-RU/'

with sr.AudioFile(filepath) as source:
    audio = r.record(source)

try:
    # Perform speech recognition using the CMUSphinx engine
    text = r.recognize_sphinx(audio, language="ru-RU")
    print("Recognized text: " + text)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    e = str(e)
    print(f"Sphinx error\n{e}.\nPlease copy folder '{os.path.abspath(model_path)}' to directory {e[e.find('"'): e.rfind('\\')]}.\"")
