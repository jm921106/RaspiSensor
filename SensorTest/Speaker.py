import pyaudio
import wave
import os

os.system('amixer cset numid=3 1')

Chunk = 1200

wf = wave.open("MicIn.wav", "rb")
p = pyaudio.PyAudio()

stream = p.open(
    format = p.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True)


data = wf.readframes(Chunk)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(Chunk)

stream.stop_stream()
stream.close()
p.terminate()