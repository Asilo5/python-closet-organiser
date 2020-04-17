import os

import tkinter as tk 
from PIL import Image, ImageTk 
from playsound import playsound

WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500

# store all the Tops into a filename can access & skip hidden files
ALL_TOPS = [str('tops/')+ imagefile for imagefile in os.listdir('tops/') if not imagefile.startswith('.')]

class WardrobeApp:
    def __init__(self, root):
       self.root = root

       # create background
       self.create_background()

    def create_background(self):
        # add title to window and change size
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))


root = tk.Tk()
app = WardrobeApp(root)
print(ALL_TOPS)
root.mainloop()