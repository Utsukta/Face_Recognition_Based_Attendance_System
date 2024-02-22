import os
import tkinter as tk
from tkinter import END, Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, StringVar, Text, ttk,messagebox
from tkinter import Entry
import webbrowser
from PIL import Image, ImageTk
from constants import Constants
import mysql.connector
import cv2

class Photos:
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
        save_btn=Button(btn_frame, text="Open the photo folder",command=self.open_img,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        save_btn.grid(row=0,column=1)


    def open_img(self):
        folder_path = os.path.join(os.getcwd(), "data") # Assuming "data" folder is in the same directory as the script
        if os.path.exists(folder_path):
            os.system(f'open "{folder_path}"') 
        else:
            print("Error: Folder not found.")
      


if __name__ == "__main__":
    root = tk.Tk()
    Photos_obj = Photos(root)
    root.mainloop()