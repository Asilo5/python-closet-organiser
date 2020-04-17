import os

import tkinter as tk 
from PIL import Image, ImageTk 
from playsound import playsound

WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500
IMAGE_WIDTH = 250
IMAGE_HEIGHT = 250

# store all the Tops into a filename can access & skip hidden files
ALL_TOPS = [str('tops/')+ imagefile for imagefile in os.listdir('tops/') if not imagefile.startswith('.')]

class WardrobeApp:
    def __init__(self, root):
       self.root = root

       # create background
       self.create_background()

       # show top image in the window
       self.top_images = ALL_TOPS

       # save single top
       self.top_image_path = self.top_images[0]

       # create and add top image into frame
       self.tops_frame = tk.Frame(self.root)
       self.top_image_label = self.create_photo( self.top_image_path, self.tops_frame)

       # add it to pack
       self.top_image_label.pack(side=tk.TOP)

       self.tops_frame.pack(fill=tk.BOTH, expand=tk.YES)


       # create background
       self.create_background()

    def create_background(self):
        # add title to window and change size
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

    
    def create_photo(self, image_path, frame):
        image_file = Image.open(image_path)
        image_resized = image_file.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)
        image_label = tk.Label(frame, image=tk_photo, anchor=tk.CENTER)
        image_label.image = tk.photo 

        return image_label



root = tk.Tk()
app = WardrobeApp(root)
print(ALL_TOPS)
root.mainloop()