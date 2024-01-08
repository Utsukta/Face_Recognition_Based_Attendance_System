import tkinter as tk
from tkinter import Label, LabelFrame, Frame, RIDGE, Text, ttk
from tkinter import Entry
from PIL import Image, ImageTk
from constants import Constants

class AddEmployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        # self.root.configure(bg="white")

        #Background Image
        img = Image.open("../Face_recogniton_system/Images/splash-bg.png")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)

        #left Frame
        left_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Add Employee",relief=RIDGE, font=("times new roman", 18 ))
        left_frame.place(x=45, y=0, width=1230, height=350)

        # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

        # Full Name
        name_label = Label(left_frame, text="Full Name", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        name_label.grid(row=0, column=0, padx=10, pady=15)

        name_entry = Text(left_frame, font=("times New roman", 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        name_entry.grid(row=0, column=1, padx=10, pady=15)

        # Address
        address_label = Label(left_frame, text="Address", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        address_label.grid(row=0, column=2, padx=10, pady=15)

        address_entry = Text(left_frame, font=("times New roman", 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        address_entry.grid(row=0, column=3, padx=10, pady=15, sticky=tk.W)

        # Phone Number
        phone_label = Label(left_frame, text="Phone Number", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        phone_label.grid(row=0, column=4, padx=10, pady=15)

        phone_entry = Text(left_frame, font=("times New roman", 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        phone_entry.grid(row=0, column=5, padx=10, pady=15, sticky=tk.W)

        # Email Address
        email_label = Label(left_frame, text="Email Address", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        email_label.grid(row=1, column=0, padx=10, pady=15)

        email_entry = Text(left_frame, font=("times New roman", 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        email_entry.grid(row=1, column=1, padx=10, pady=15, sticky=tk.W)

        # Gender
        gender_label = Label(left_frame, text="Gender", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        gender_label.grid(row=1, column=2, padx=10, pady=15)
        gender_combo = ttk.Combobox(left_frame, font=("times new roman", 12, "bold"), width=28, state="readonly")
        gender_combo["values"] = ( "Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=15, sticky=tk.W)
        

        # Joined Date
        joined_label = Label(left_frame, text="Joined Date", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        joined_label.grid(row=1, column=4, padx=10, pady=15)

        joined_entry = Text(left_frame, font=("times New roman", 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        joined_entry.grid(row=1, column=5, padx=10, pady=15, sticky=tk.W)

        # Department
        dep_label = Label(left_frame, text="Department", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        dep_label.grid(row=2, column=0, padx=2, pady=15)

        dep_combo = ttk.Combobox(left_frame, font=("times new roman", 12, "bold"), width=28, state="readonly")
        dep_combo["values"] = ("select Department", "HR", "IT", "Finance", "Marketing", "Operations")
        dep_combo.current(0)
        dep_combo.grid(row=2, column=1, padx=2, pady=15, sticky=tk.W)

        # Salary
        salary_label = Label(left_frame, text="Salary", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        salary_label.grid(row=2, column=2, padx=10, pady=15)

        salary_entry = Text(left_frame, font=("times New roman", 15 ), width=22,height=1,insertbackground="black",bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        salary_entry.grid(row=2, column=3, padx=10, pady=15, sticky=tk.W)

        # Emergency Contacts
        emergency_label = Label(left_frame, text="Emergency Contacts", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        emergency_label.grid(row=2, column=4, padx=10, pady=15)

        emergency_entry = Text(left_frame, font=("times New roman", 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        emergency_entry.grid(row=2, column=5, padx=10, pady=15, sticky=tk.W)

        # Educational Background
        education_label = Label(left_frame, text="Educational Background", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        education_label.grid(row=9, column=0, padx=10, pady=15)

        education_entry = Text(left_frame, font=("times New roman", 15 ), width=22,height=1,insertbackground="black" ,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,borderwidth=0,highlightbackground="grey",highlightthickness=2 )
        education_entry.grid(row=9, column=1, padx=10, pady=15, sticky=tk.W)

      


if __name__ == "__main__":
    root = tk.Tk()
    AddEmployee_obj = AddEmployee(root)
    root.mainloop()