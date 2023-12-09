import tkinter;
from tkinter import ttk
from PIL import Image

class Face_Recogniton_Attendance_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1440x900+0+0")
        self.root.title("Face Recognition system")
        self.root.configure(bg="white")



if __name__== "__main__":
    root=tkinter.Tk()
    obj=Face_Recogniton_Attendance_System(root)
    root.mainloop()


