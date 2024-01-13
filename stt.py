import gtts
import speech_recognition as sr
from pydub import AudioSegment


def speak(msg):
    tts = gtts.gTTS(msg, lang="ru")
    tts.save("hello.mp3")  