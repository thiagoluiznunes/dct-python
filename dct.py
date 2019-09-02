import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos, radians
from scipy.io import wavfile
from scipy.fftpack import dct
from scipy.fftpack import idct
from PIL import Image
import array as arr
import math
import wave
import struct
# DCT Audio


def openAudio():
    waveFile = wave.open('audio.wav', 'r')
    # rate = waveFile.getframerate()
    length = waveFile.getnframes()
    arrayAudioFrames = arr.array('i')

    for i in range(0, length):
        waveData = waveFile.readframes(1)
        data = struct.unpack('<h', waveData)
        arrayAudioFrames.append(int(data[0]))
    return arrayAudioFrames


# def getImportantCosines(array_frames, cosine_rate):
#     rate = cosine_rate
#     importantCosines = arr.array('i')

#     for i in range(0, length):
#         waveData = waveFile.readframes(i)
#         data = struct.unpack('<h', waveData)
#         if abs(int(data[0])) > rate:
#             importantCosines.append(int(data[0]))


def showDCTGraph(dcts):
    arr = np.arange(len(dcts))
    plt.plot(arr, dcts)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('DCT graph')
    plt.show()


def applayDCTinAudio(frames):
    # N = len(frames)
    N = 8

    for k in range(0, N):
        ck = math.sqrt(0.5) if k == 0 else 1
        Ak = math.sqrt(2.0/N)
        Xk = frames[k]
        samples = np.zeros(N)
        # print('Frame value: ', frames[k])
        # print('ck value: ', ck)
        # print('Ak value: ', Ak)
        # print('Xk value: ', Xk)

        for n in range(0, N):
          samples[n] = Ak * ck * Xk * cos(radians(((2 * pi * k * n)/2*N) + ((k * pi)/2*N)))

        if k == 3:
          arr = np.arange(N)
          plt.plot(arr, samples)
          plt.xlabel('x - axis')
          plt.ylabel('y - axis')
          plt.title('DC')
          plt.show()
    # dct_frames = arr.array('f')
    # N = len(array_frames)
    # for n in range(0, N):
    #   print('Amostra', n)
    #   aux = arr.array('f')
    #   Xk = array_frames[n]
    #   for k in range(0, N):
    #     ck = math.sqrt(1/2) if k == 0 else 1
    #     aux.append((2/N) * ck * Xk * math.cos((2*math.pi*k*n/2*N) + (k*math.pi/2*N)))
    #   if n == 0:
    #     dct_frames = aux
    #   else:
    #     for i in range(0, N):
    #       dct_frames[i] += aux[i]


if __name__ == '__main__':
    frames = openAudio()
    applayDCTinAudio(frames)
    # showDCTGraph(frames)
    # applayDCTinAudio(frames)
    # newArrayDCT = dct(arrayAudioFrames, norm = 'ortho')

    # newArrayIDCT = idct(newArrayDCT, norm = 'ortho')
    # newArrayIDCT = newArrayIDCT.astype('int16')

    # wavfile.write('audio-idct.wav', rate , newArrayIDCT)
    # wavfile.write('audio-idct-chunked.wav', rate , newArrayIDCTChunked)
    # wavfile.write('audio-idct-robot.wav', rate , newArrayIDCTRobot)

    # DCT Image
    # img = Image.open('lena.bmp')
    # arrayImg = np.asarray(img)

    # newImgDCT = dct(dct(arrayImg.T, norm = 'ortho').T, norm = 'ortho')
    # maxCosValueImg = 5
    # countCosImg = 0

    # for i in range(0, len(newImgDCT)):
    #   for j in range(0, len(newImgDCT[i])):
    #     if newImgDCT[i][j] < maxCosValueImg:
    #       newImgDCT[i][j] = 0
    #       countCosImg += 1

    # print('Total cosine deleted: ', countCosImg)
    # newImgIDCT = idct(idct(newImgDCT.T, norm = 'ortho').T, norm = 'ortho')
    # im = Image.fromarray(newImgIDCT)
    # im.show()
