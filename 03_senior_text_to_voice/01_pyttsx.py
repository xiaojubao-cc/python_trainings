#文本转语音
import pyttsx3


class TextToSpeech(object):
    engine: pyttsx3.engine
    def __init__(self,voice,rate:int,volume:float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_all_voices(self):
        voices:list = [self.engine.getProperty('voices')]
        for i, voice in enumerate(voices[0]):
            print(f"{i}: {voice.name},[{voice.id}]")


if __name__ == '__main__':
    tts = TextToSpeech(voice=None,rate=200,volume=1)
    tts.list_all_voices()
