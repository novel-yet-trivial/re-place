#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

HEIGHT, WIDTH = 1000, 1000
CHEATER = 10000 # update display every n changed pixels. The higher this number the faster the animation

colour_lookup = [
    (1.00, 1.00, 1.00), (0.89, 0.89, 0.89), (0.53, 0.53, 0.53), (0.13, 0.13, 0.13),
    (1.00, 0.65, 0.82), (0.90, 0.00, 0.00), (0.90, 0.58, 0.00), (0.63, 0.42, 0.26),
    (0.90, 0.85, 0.00), (0.58, 0.88, 0.27), (0.01, 0.75, 0.00), (0.00, 0.90, 0.94),
    (0.00, 0.51, 0.78), (0.00, 0.00, 0.92), (0.88, 0.29, 1.00), (0.51, 0.00, 0.50)]

print("Opening binary file")
fh = open('pixels.bin', 'rb')
print("Making a million pixels")
data = np.full((WIDTH, HEIGHT, 3), 1.0, dtype=np.float32)
print("Done, Drawing")

def from_bytes3(b):
    '''3 bytes => 24 bit integer => x, y, and color'''
    i = int.from_bytes(b, 'little')
    return i >> 14 & 1023, i >> 4 & 1023, i & 15

def clear():
    data.fill(1.0) # clear the image
    fh.seek(0) # restart the file

def load_data(num_pixels):
    for idx in range(num_pixels):
        pixel = fh.read(3)
        if not pixel: # file is exhausted. Restart.
            clear()
        else:
            x, y, c = from_bytes3(pixel)
            data[y][x] = colour_lookup[c]

fig = plt.figure()
plt.subplots_adjust(bottom=0.25)
im = plt.imshow(data, animated=True)

def draw(i):
    load_data(CHEATER)
    im.set_array(data)
    slide.set_val(fh.tell() / 3000000)
    return im,

def update(val):
    target_pixel = int(val * 1000000)
    current_pixel = int(fh.tell() / 3)
    delta = target_pixel - current_pixel
    if delta == 0:
        return # nothing to do

    if delta > 0:
        to_load = delta
    elif delta < 0:
        clear()
        to_load = target_pixel
    print('loading {:,} pixels, please wait ... '.format(to_load), end='', flush=True)
    load_data(to_load)
    im.set_array(data)
    print('done')

ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03]) # [left, bottom, width, height]
slide = Slider(ax_slider, 'Pixels', 0, 16.5, valinit=0)
slide.on_changed(update)

ani = animation.FuncAnimation(fig, draw, interval=50, blit=True)
plt.show()
