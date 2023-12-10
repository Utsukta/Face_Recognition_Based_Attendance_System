from tkinter import *
from PIL import Image, ImageTk

class Shared:
    def __init__(self, root):
        self.root = root
        self.content_frame = Frame(root, bg="pink")
        self.content_frame.place(x=0, y=0, width=120, height=900)
        img = Image.open("/Users/utsuktakhatri/Desktop/Face_recogniton_system/Images/rps_logo-preview.png")
        img=img.resize((100,50))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg,bg='pink')
        f_lbl.place(x=5, y=20)
    

    
