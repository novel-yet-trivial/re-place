from tkinter import *
import threading

h, w = 1001, 1001

colour_lookup = {
    0:"#FFFFFF",
    1:"#E4E4E4",
    2:"#888888",
    3:"#222222",
    4:"#FFA7D1",
    5:"#E50000",
    6:"#E59500",
    7:"#A06A42",
    8:"#E5D900",
    9:"#94E044",
    10:"#02BE01",
    11:"#00E5F0",
    12:"#0083C7",
    13:"#0000EA",
    14:"#E04AFF",
    15:"#820080"
}

root = Tk()
root.title("re-place")
root.geometry("{}x{}".format(w, h))
place_canvas = Canvas(root, width=w, height=h, highlightbackground="white")
place_canvas.grid()

def draw():
    # Temp demo list, I can't experiment with the actualy data just yet, as my
    # internet is too bad to download it :(
    lis = [[25, 25, 9], [26, 26, 10], [27, 27, 5]]
    for entry in lis:
        x, y, c = entry[0]. entry[1], entry[2]
        place_canvas.create_rectangle(x, y, x+1, y+1, fill=colour_lookup[c],  width=0)

t = threading.Thread(target=draw)
t.daemon = True
t.start()
root.mainloop()
