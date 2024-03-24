import os
import subprocess
import sys
import tkinter as tk
from tkinter import END, Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, StringVar, Text, ttk,messagebox
from PIL import Image, ImageTk
from constants import Constants


class Photos:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440, 900)
        self.root.maxsize(1440,900)

        #Background Image
        img = Image.open("/Users/utsuktakhatri/Desktop/Face_recogniton_system/Images/photo_bg.png")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)

        # img1 = Image.open("../Face_recogniton_system/Images/facial-recognition-attendance-system.png")
        # img1=img1.resize((500,400), Image.Resampling.LANCZOS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)
        # bg_img1= Label(self.root, image=self.photoimg1)
        # bg_img1.place(x=500,y=0,width=370,height=400)

         # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

         #button_frame
        btn_frame = Frame(root)
        btn_frame.place(x=700, y=300, width=200, height=30)

        #save_button
        save_btn=Button(btn_frame, text="Open the photo folder",command=self.open_img,font=(Constants.Add_Employee_font ,20),highlightthickness=0)
        save_btn.grid(row=0,column=1)


    # def open_img(self):
    #     folder_path = os.path.join(os.getcwd(), "data") # Assuming "data" folder is in the same directory as the script
    #     if os.path.exists(folder_path):
    #         os.system(f'open "{folder_path}"') 
    #     else:
    #         print("Error: Folder not found.")
    def open_img(self):
        folder_path = os.path.join(os.getcwd(), "data")  # Assuming "data" folder is in the same directory as the script
        try:
            if os.path.exists(folder_path):
                if os.name == 'nt':  # For Windows
                    os.startfile(folder_path)
                elif os.name == 'posix':  # For Linux and macOS
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    subprocess.call([opener, folder_path])
            else:
                raise FileNotFoundError("Folder not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
      


if __name__ == "__main__":
    root = tk.Tk()
    Photos_obj = Photos(root)
    root.mainloop()