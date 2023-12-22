from tkinter import *
from PIL import Image, ImageTk
from shared import Shared

class Face_Recognition_Attendance_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440,900)
        
        
        self.root.title("Face Recognition system")
        self.root.configure(bg="white")

        # Create an instance of the Shared class
        self.shared_instance_main = Shared(self.root)
        
        

if __name__ == "__main__":
    root = Tk()
    main_obj = Face_Recognition_Attendance_System(root)
    root.mainloop()
