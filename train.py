import os
import tkinter as tk
from tkinter import END, Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, StringVar, Text, ttk,messagebox
from tkinter import Entry
import webbrowser
from PIL import Image, ImageTk
from constants import Constants
import mysql.connector
import cv2

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440, 900)
        self.root.maxsize(1440,900)

        img = Image.open("../Face_recogniton_system/Images/splash-bg.png")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)

         # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

         #button_frame
        btn_frame = Frame(root)
        btn_frame.place(x=700, y=270, width=150, height=25)

        #save_button
        save_btn=Button(btn_frame, text="Train Data",command=self.train_classifier,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        save_btn.grid(row=0,column=1)

    def train_classifier(self):
        data_dir=("data")
        #list comprehension
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            #Converts in grey scale image
            img=Image.open(image).convert("L")


if __name__ == "__main__":
    root = tk.Tk()
    Train_obj = Train(root)
    root.mainloop()