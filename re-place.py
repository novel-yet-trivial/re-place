#!/usr/bin/env python3

print("Loading...")
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from csv import DictReader
import numpy as np
import lzma

HEIGHT, WIDTH = 1001, 1001
STEP = 10000 # update display every n changed pixels

colour_lookup = [
    (1.00, 1.00, 1.00), (0.89, 0.89, 0.89), (0.53, 0.53, 0.53), (0.13, 0.13, 0.13),
    (1.00, 0.65, 0.82), (0.90, 0.00, 0.00), (0.90, 0.58, 0.00), (0.63, 0.42, 0.26),
    (0.90, 0.85, 0.00), (0.58, 0.88, 0.27), (0.01, 0.75, 0.00), (0.00, 0.90, 0.94),
    (0.00, 0.51, 0.78), (0.00, 0.00, 0.92), (0.88, 0.29, 1.00), (0.51, 0.00, 0.50)
]

print("Opening csv")
csvfile = lzma.open('sorted_pixels.csv.xz', 'rt')
print("Open, feeding to DictReader")
reader = DictReader(csvfile)
print("Making a million pixels")
data = np.full((WIDTH, HEIGHT, 3), 1.0, dtype=np.float32)
print("Done, Drawing")

def draw(i):
    for idx in range(STEP):
        try:
            row = next(reader)
        except StopIteration:
            print("Finished")
            break
        x = int(row["x_coordinate"])
        y = int(row["y_coordinate"])
        c = int(row["color"])
        data[y][x] = colour_lookup[c]
    im.set_array(data)
    return im,

fig = plt.figure()
im = plt.imshow(data, animated=True)
ani = animation.FuncAnimation(fig, draw, interval=50, blit=True)
plt.show()
