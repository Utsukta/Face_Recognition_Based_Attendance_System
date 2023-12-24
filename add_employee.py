from tkinter import *
from constants import Constants


class AddEmployee:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1440x900+0+0")
        # self.root.minsize(1440,900)
        self.root.configure(bg="white")

        #instance of shared
        from shared import Shared
        self.shared=Shared(self.root)

        self.add_employee_frame = Frame(root, bg=Constants.content_background_color)
        self.add_employee_frame .place(x=160, y=0, width=1280, height=900)
        Addemployee_label= Label(text="Add Employee", bg=Constants.content_background_color, fg=Constants.frame_content_text_color, font=("Times New Roman",23))
        Addemployee_label.place(x=680, y=50)

    



if __name__ == "__main__": 
    root = Tk()
    AddEmployee_obj = AddEmployee(root)
    root.mainloop()