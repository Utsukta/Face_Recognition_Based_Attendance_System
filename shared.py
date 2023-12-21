from tkinter import *
from PIL import Image, ImageTk
from constants import Constants

class Shared:
    def __init__(self, root):
        self.root = root
        self.content_frame = Frame(root, bg=Constants.shared_background_color)
        self.content_frame.place(x=0, y=0, width=140, height=900)
        #logo
        logo_img = Image.open("/Users/utsuktakhatri/Desktop/Face_recogniton_system/Images/rps_logo-preview.png")
        logo_img=logo_img.resize((100,45))
        self.logo_img = ImageTk.PhotoImage(logo_img)
        #background Image

        # background_img=Image.open("/Users/utsuktakhatri/Desktop/Face_recogniton_system/Images/splash-bg.png")
        # self.background_img = ImageTk.PhotoImage(background_img)
       
        # background_label = Label(self.content_frame, image=self.background_img)
        # background_label.place(x=0,y=0)
        # img = Image.open("/Users/utsuktakhatri/Desktop/Face_recogniton_system/Images/rps_logo-preview.png")
        # img=img.resize((100,50))
        # self.photoimg = ImageTk.PhotoImage(img)


        #logo label
        logo_label = Label(self.root, image=self.logo_img, bg=Constants.shared_background_color)
        logo_label.place(x=5, y=20)

        #Home label
        home_label= Label(text="Home",bg="lightgrey",foreground="black", )
        home_label.bind("<Button-1>",self.on_home_label_clicked)
        home_label.place(x=35, y=150)

        
        home_label= Label( text="Home",bg="lightgrey",foreground="black" )
        home_label.place(x=35, y=190)

    def on_home_label_clicked(self,event):
            print("clicked")
    

    
        