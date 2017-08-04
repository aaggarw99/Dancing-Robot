import serial
import time
# import pyaudio
import subprocess

audioFile = "/Users/dwheadon/Desktop/unforgettable.wav"
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
[Fs, x] = audioBasicIO.readAudioFile(audioFile);
print(Fs);
print(x.shape);
x = x[:,0];
F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);

return_code = subprocess.Popen(["afplay", audioFile])

print(F.shape);
print("Max is ", F[1].max());
mean = F[1].mean();
print("Mean is ", mean);
for i in range(0, len(F[1])):
    print(F[1][i]);
    if F[1][i] > 0.1:
        ser.write(b'b')
    time.sleep(0.022)
ser.close()
