from tkinter import *
from constants import Constants

class Employee_Details:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1440x900+0+0")
        # self.root.minsize(1440,900)
        self.root.configure(bg="white")


        #instance of shared
        # from shared import Shared
        # self.shared=Shared(self.root)
        # self.shared_frame = Frame(root, bg="white")
        # self.shared_frame.place(x=160, y=0, width=1000, height=900)
        Employee_details_label= Label(text="Employee Details", bg=Constants.content_background_color, fg=Constants.shared_text_color)
        Employee_details_label.place(x=500, y=100)
        label1= Label(text="text")
        label1.place(x=900, y=100)
    

if __name__ == "__main__": 
    root = Tk()
    AddEmployee_obj = Employee_Details(root)
    root.mainloop()