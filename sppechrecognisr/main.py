import pyaudio
import wave
import speech_recognition as sr
from comments import Command
import subprocess
import pyttsx3
running = True
engine = pyttsx3.init()




def say(text):
    engine.say(text)
    engine.runAndWait()

def play_audio(filename):
    
    chunk =1024
    wf = wave.open(filename,'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels  =wf.getnchannels(),
        rate = wf.getframerate(),
        output =True

    )
    data_stream = wf.readframes(chunk)
    while data_stream:

        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    stream.close()
    pa.terminate()

r = sr.Recognizer()
cmd = Command()
def initSpeech():
    print("Listening")
    play_audio("./audio/a.wav")
     
    with sr.Microphone() as source:
         print("Say something")
         audio = r.listen(source)
         
    play_audio("./audio/b.wav")
    
    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print("sorry couldnt understand")
    print("your command")
    print(command)
    if command in ["quit","exit","bye","goodbye"]:
        global running
        running = False
    cmd.discover(command)
    #say('you said' + command)
    
while running ==True:
    initSpeech()