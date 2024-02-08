import wave
import numpy as np
import matplotlib.pyplot as plt
import librosa
import soundfile as sf
from scipy.signal import find_peaks
import sys

if len(sys.argv) != 2:
    sys.exit(0)

x,_ = librosa.load("./"+sys.argv[1], sr=16000)
sf.write("./"+sys.argv[1], x, 16000)
wav_obj = wave.open("./"+sys.argv[1], 'rb')


sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
t_audio = n_samples/sample_freq
n_channels = wav_obj.getnchannels()
signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]
times = np.linspace(0, n_samples/sample_freq, num=n_samples)
peaks2, _ = find_peaks(l_channel, distance=3000)
plt.plot(peaks2,l_channel[peaks2],'ob')
plt.plot(l_channel)
plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()