import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = 10

recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=1)

sd.wait()

#USING SCIPY
# write("recording0.wav", freq, recording)

#USING WAVIO
wv.write("recording0.wav", recording, freq, sampwidth=2)
