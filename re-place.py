from csv import DictReader
from tkinter import *
import threading

h, w = 1001, 1001

colour_lookup = ["#FFFFFF", "#E4E4E4", "#888888", "#222222", "#FFA7D1",
                 "#E50000", "#E59500", "#A06A42", "#E5D900", "#94E044",
                 "#02BE01", "#00E5F0", "#0083C7", "#0000EA", "#E04AFF",
                 "#820080"]

root = Tk()
root.title("re-place")
root.geometry("{}x{}".format(w, h))
place_canvas = Canvas(root, width=w, height=h, highlightbackground="white")
place_canvas.grid()

def draw():
    print("Opening csv")
    with open ("sorted_pixels.csv") as csvfile:
        print("Open, feeding to DictReader")
        reader = DictReader(csvfile)
        print("Done, Drawing")
        for row in reader:
            x = int(row["x_coordinate"])
            y = int(row["y_coordinate"])
            c = int(row["color"])
            place_canvas.create_rectangle(x, y, x+1, y+1, fill=colour_lookup[c],  width=0)

t = threading.Thread(target=draw)
t.daemon = True
t.start()
root.mainloop()
