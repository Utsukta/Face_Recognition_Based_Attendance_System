from tkinter import *

class Employee_Details:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440,900)
        self.root.configure(bg="white")
    


if __name__ == "__main__": 
    root = Tk()
    AddEmployee_obj = Employee_Details(root)
    root.mainloop()