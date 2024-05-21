from PIL import Image, ImageSequence, ImageTk
import tkinter as tk
import random
from tkinter import ttk
from itertools import cycle


root = tk.Tk()
root.lift()
root.attributes("-topmost", True)
root.withdraw()
list_of_windows = []

def close_window(i, list_var):
    list_var[i][0].destroy()
    del list_var[i][0]

def close_windows(list_var):
    for window in list_var:
        window[0].destroy()

def play_gif(imagelist, label):
    img = next(imagelist)
    label.img = ImageTk.PhotoImage(img)
    label.config(image=label.img)
    label.after(100, play_gif, imagelist, label) 

with Image.open(f".\\img\\youareanidiot.gif") as im:
        imagelist = cycle(ImageSequence.all_frames(im))
    
for _ in range(0, (20)):
        x = tk.Toplevel(root) 
        x.title("You are an idiot!")
        x_pos = random.randint(0,x.winfo_screenwidth())
        y_pos = random.randint(0,x.winfo_screenheight())
        x.geometry(f"160x117+{x_pos}+{y_pos}")
        x.resizable(False, False)
        yaai = tk.PhotoImage(file=f".\\img\\youareanidiot.gif", format="gif -index 2")
        y = ttk.Label(x, image=yaai)
        y.pack()
        x.lift()
        x.attributes("-topmost", True)
        x.after(10, play_gif, imagelist, y)
        list_of_windows.append([x,x_pos, y_pos, 4, 4])
    

while True:
        for x in list_of_windows:
            print(x)
            x[0].geometry(F"+{x[1]}+{x[2]}")
            x[0].update()
            if x[1]<0 or x[1]>2000: 
                x[3] *= -random.randint(1, 15)/5
            if x[2]<0 or x[2]>1000:
                x[4] *= -random.randint(1, 15)/5
            x[3] = round(x[3])
            x[4] = round(x[4])
            if abs(x[3])>20: x[3] = 3
            if abs(x[4])>20: x[4] = 3
            x[1] += x[3]
            x[2] += x[4]
