from pathlib import Path
import speech_recognition as sr
from pydub import AudioSegment

def audio2text(filepath: str) -> str:
    file = Path(filepath)
    if not file.exists():
        raise FileNotFoundError('Audio File not found')
    if file.suffix == '.mp3':
        sound = AudioSegment.from_mp3(file)
        filename = str(file.absolute()).replace('.mp3', '.wav')
        sound.export(filename, format="wav")
        file = Path(filename)

    r = sr.Recognizer()

    with sr.AudioFile(str(file.absolute())) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = r.recognize_google_cloud(audio_data)
    return text

if __name__ == '__main__':
    print(audio2text('audio.mp3'))
