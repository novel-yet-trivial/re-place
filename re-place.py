#!/usr/bin/env python3

from csv import DictReader
import tkinter as tk
import threading
import lzma

HEIGHT, WIDTH = 1001, 1001

colour_lookup = ["#FFFFFF", "#E4E4E4", "#888888", "#222222", "#FFA7D1",
                 "#E50000", "#E59500", "#A06A42", "#E5D900", "#94E044",
                 "#02BE01", "#00E5F0", "#0083C7", "#0000EA", "#E04AFF",
                 "#820080"]

root = tk.Tk()
root.title("re-place")
root.geometry("{}x{}".format(WIDTH, HEIGHT))
place_canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightbackground="white")
place_canvas.grid()

print('please wait ... making 1 million pixels')
pixels = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        pixels[(x, y)] = place_canvas.create_rectangle(x, y, x+1, y+1, fill=colour_lookup[0],  width=0)

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
            place_canvas.itemconfig(pixels[(x,y)], fill=colour_lookup[c])
            if idx % 1000:
                root.update()

t = threading.Thread(target=draw)
t.daemon = True
t.start()
root.mainloop()
