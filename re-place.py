#!/usr/bin/env python3

from csv import DictReader
import lzma
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

HEIGHT, WIDTH = 1001, 1001
CHEATER = 1000 # update display every n changed pixels. The higher this number the faster the animation

colour_lookup = [(1.0, 1.0, 1.0), (0.8941176470588236, 0.8941176470588236, 0.8941176470588236), (0.5333333333333333, 0.5333333333333333, 0.5333333333333333), (0.13333333333333333, 0.13333333333333333, 0.13333333333333333), (1.0, 0.6549019607843137, 0.8196078431372549), (0.8980392156862745, 0.0, 0.0), (0.8980392156862745, 0.5843137254901961, 0.0), (0.6274509803921569, 0.41568627450980394, 0.25882352941176473), (0.8980392156862745, 0.8509803921568627, 0.0), (0.5803921568627451, 0.8784313725490196, 0.26666666666666666), (0.00784313725490196, 0.7450980392156863, 0.00392156862745098), (0.0, 0.8980392156862745, 0.9411764705882353), (0.0, 0.5137254901960784, 0.7803921568627451), (0.0, 0.0, 0.9176470588235294), (0.8784313725490196, 0.2901960784313726, 1.0), (0.5098039215686274, 0.0, 0.5019607843137255)]

print("Opening csv")
csvfile = lzma.open('sorted_pixels.csv.xz', 'rt')
print("Open, feeding to DictReader")
reader = DictReader(csvfile)
print("Making a million pixels")
data = np.full((WIDTH, HEIGHT, 3), 1.0, dtype=np.float32)
print("Done, Drawing")

def draw(i):
    for idx in range(CHEATER):
        row = next(reader)
        x = int(row["x_coordinate"])
        y = int(row["y_coordinate"])
        c = int(row["color"])
        #~ data[x][y] = colour_lookup[c]
        data[y][x] = colour_lookup[c]
    im.set_array(data)
    return im,

fig = plt.figure()

im = plt.imshow(data, animated=True)

ani = animation.FuncAnimation(fig, draw, interval=50, blit=True)
plt.show()
