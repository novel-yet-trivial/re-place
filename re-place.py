#!/usr/bin/env python3

from csv import DictReader
import tkinter as tk
import threading
import lzma
from PIL import Image, ImageTk

HEIGHT, WIDTH = 1001, 1001
CHEATER = 10000 # update display every n changed pixels. The higher this number the faster the animation

root = tk.Tk()
root.title("re-place")
root.geometry("{}x{}".format(WIDTH, HEIGHT))

img = Image.new(mode="P", size=(WIDTH, HEIGHT))
img.putpalette([255, 255, 255, 228, 228, 228, 136, 136, 136, 34, 34, 34, 255, 167, 209, 229, 0, 0, 229, 149, 0, 160, 106, 66, 229, 217, 0, 148, 224, 68, 2, 190, 1, 0, 229, 240, 0, 131, 199, 0, 0, 234, 224, 74, 255, 130, 0, 128])
place_label = tk.Label(root)
place_label.pimg = ImageTk.PhotoImage(img)
place_label.config(image=place_label.pimg)
place_label.pack()

def draw():
    print("Opening csv")
    with lzma.open('sorted_pixels.csv.xz', 'rt') as csvfile:
        print("Open, feeding to DictReader")
        reader = DictReader(csvfile)
        print("Done, Drawing")
        for idx, row in enumerate(reader):
            x = int(row["x_coordinate"])
            y = int(row["y_coordinate"])
            c = int(row["color"])
            img.putpixel((x,y), c)
            if idx % CHEATER == 0:
                place_label.pimg = ImageTk.PhotoImage(img)
                place_label.config(image=place_label.pimg) #update GUI

t = threading.Thread(target=draw)
t.daemon = True
t.start()
root.mainloop()
