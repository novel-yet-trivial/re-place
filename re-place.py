from tkinter import *
import threading

"""
1001x1001 because if a pixel is placed at (1000, 1000), due to the create_rectangle
function, its bottom right corner would be located at (1001, 1001)

Data:
https://www.reddit.com/r/redditdata/comments/6640ru/place_datasets_april_fools_2017/
"""

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

h, w = 1001, 1001

root = Tk()
root.title("re-place")
root.geometry("{}x{}".format(w, h))
drawing_canvas = Canvas(root, width=w, height=h, highlightbackground="grey")
drawing_canvas.grid()

def draw():
    lis = [[25, 25, 9], [26, 26, 10], [27, 27, 5]]

    for entry in lis:
        x = entry[0]
        y = entry[1]
        c = entry[2]

        drawing_canvas.create_rectangle(x, y, x+1, y+1, fill=colour_lookup[c],  width=0)

t = threading.Thread(target=draw)
t.daemon = True
t.start()
root.mainloop()
