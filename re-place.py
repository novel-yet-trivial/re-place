from tkinter import *
import threading

"""
1001x1001 because if a pixel is placed at (1000, 1000), due to the create_rectangle
function, its bottom right corner would be located at (1001, 1001)

http://wiki.tcl.tk/37701
"""

h, w = 1001, 1001

root = Tk()
root.title("re-place")
root.geometry("{}x{}".format(w, h))
drawing_canvas = Canvas(root, width=w, height=h, highlightbackground="grey")
drawing_canvas.grid()

def draw():
    lis = [[25, 25, "blue"], [26, 26, "red"], [27, 27, "green"]]

    for entry in lis:
        x = entry[0]
        y = entry[1]
        colour = entry[2]

        drawing_canvas.create_rectangle(x, y, x+1, y+1, fill=colour,  width=0)

t = threading.Thread(target=draw)
t.daemon = True
t.start()
root.mainloop()
