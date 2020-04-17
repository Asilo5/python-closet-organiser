import tkinter as tk 
from PIL import Image, ImageTk 
from playsound import playsound

WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500

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
root.mainloop()