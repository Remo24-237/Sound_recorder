
# library neccessary
# wavio
# scipy
# sounddevice

# importing related libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

def voice_rec():
    # sampling frequency
    freq = 44100

    # recording duration
    duration = 5

    # start recorder with the given values of duration and sample frequency
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

    # record audio for the given number of seconds
    sd.wait()

    # converting the numpy array into an audio file with the given sampling frequency
    write("recording.wav", freq, recording)

    # convert the numpy array to audio file
    wv.write("recording1.wav", recording, freq, sampwidth=2)

if __name__ == '__main__':
    voice_rec()


