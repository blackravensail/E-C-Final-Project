"""
Draws a set of points on a scope.

"""
from audiocore import RawSample
from audioio import AudioOut
import board

from array import array
from time import sleep, monotonic

from frames import *
from utils import *


stereo_dac = AudioOut(board.A0, right_channel = board.A1, quiescent_value = 0)

frames = [locals()[f"frame_{i}"] for i in range(18)]
buffers = []
for c, points in enumerate(frames):
    print(f"Building frame {c}")
    print(f"Number of array cells {((len(points) - 1) * samples) * 2}")
    print(f"Num lines {len(points) - 1}")

    line_array = array("H", [0] * ((len(points) - 1) * samples * 2))


    i = 0
    for pt1, pt2 in pairwise(points):
        pt1 = int(pt1[0] * 65535/400), int(pt1[1] * 65535/400)
        pt2 = int(pt2[0] * 65535/400), int(pt2[1] * 65535/400)
        temp = sum(gen_line(pt1, pt2), ())

        for val in temp:
            line_array[i] = val
            i += 1
    buffers.append(RawSample(line_array, channel_count = 2, sample_rate = 1_000_000))

i = 0
while True:
    stereo_dac.play(buffers[i], loop = True)
    sleep(0.08)
    stereo_dac.stop()
    i= (i+1)%len(buffers)