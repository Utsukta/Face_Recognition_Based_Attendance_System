import tkinter as tk
from tkinter import Label, LabelFrame, Frame, RIDGE, ttk
from tkinter import Entry
from PIL import Image, ImageTk
from constants import Constants

class AddEmployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")

        #Background Image
        img = Image.open("../Face_recogniton_system/Images/white_background.jpg")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)

        #Main Frame
        add_employee_frame = Frame(bg_img,bd=4,bg=Constants.content_background_color)
        add_employee_frame.place(x=50, y=0, width=1000, height=900)

        #left Frame
        left_frame = LabelFrame(add_employee_frame,bd=10, bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Add Employee",relief=RIDGE, font=("times new roman", 18 ))
        left_frame.place(x=50, y=50, width=500, height=800)

        # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

        # Full Name
        name_label = Label(left_frame, text="Full Name", font=("georgia", 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        name_label.grid(row=0, column=0, padx=10, pady=15)

        name_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        name_entry.grid(row=0, column=1, padx=10, pady=15, sticky=tk.W)

        # Address
        address_label = Label(left_frame, text="Address", font=("times new roman", 12, "bold"))
        address_label.grid(row=1, column=0, padx=10, pady=15)

        address_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        address_entry.grid(row=1, column=1, padx=10, pady=15, sticky=tk.W)

        # Phone Number
        phone_label = Label(left_frame, text="Phone Number", font=("times new roman", 12, "bold"))
        phone_label.grid(row=2, column=0, padx=10, pady=15)

        phone_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        phone_entry.grid(row=2, column=1, padx=10, pady=15, sticky=tk.W)

        # Email Address
        email_label = Label(left_frame, text="Email Address", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=15)

        email_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        email_entry.grid(row=3, column=1, padx=10, pady=15, sticky=tk.W)

        # Gender
        gender_label = Label(left_frame, text="Gender", font=("times new roman", 12, "bold"))
        gender_label.grid(row=4, column=0, padx=10, pady=15)

        gender_combo = ttk.Combobox(left_frame, font=("times new roman", 12, "bold"), width=17)
        gender_combo["values"] = ("select Gender", "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=4, column=1, padx=2, pady=15, sticky=tk.W)

        # Joined Date
        joined_label = Label(left_frame, text="Joined Date", font=("times new roman", 12, "bold"))
        joined_label.grid(row=5, column=0, padx=10, pady=15)

        joined_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        joined_entry.grid(row=5, column=1, padx=10, pady=15, sticky=tk.W)

        # Department
        dep_label = Label(left_frame, text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=6, column=0, padx=2, pady=15)

        dep_combo = ttk.Combobox(left_frame, font=("times new roman", 12, "bold"), width=17)
        dep_combo["values"] = ("select Department", "HR", "IT", "Finance", "Marketing", "Operations")
        dep_combo.current(0)
        dep_combo.grid(row=6, column=1, padx=2, pady=15, sticky=tk.W)

        # Salary
        salary_label = Label(left_frame, text="Salary", font=("times new roman", 12, "bold"))
        salary_label.grid(row=7, column=0, padx=10, pady=15)

        salary_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        salary_entry.grid(row=7, column=1, padx=10, pady=15, sticky=tk.W)

        # Emergency Contacts
        emergency_label = Label(left_frame, text="Emergency Contacts", font=("times new roman", 12, "bold"))
        emergency_label.grid(row=8, column=0, padx=10, pady=15)

        emergency_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        emergency_entry.grid(row=8, column=1, padx=10, pady=15, sticky=tk.W)

        # Educational Background
        education_label = Label(left_frame, text="Educational Background", font=("times new roman", 12, "bold"))
        education_label.grid(row=9, column=0, padx=10, pady=15)

        education_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        education_entry.grid(row=9, column=1, padx=10, pady=15, sticky=tk.W)

        # Work History
        work_history_label = Label(left_frame, text="Work History", font=("times new roman", 12, "bold"))
        work_history_label.grid(row=10, column=0, padx=10, pady=15)

        work_history_entry = Entry(left_frame, font=("times New roman", 12, "bold"), width=17)
        work_history_entry.grid(row=10, column=1, padx=10, pady=15, sticky=tk.W)


if __name__ == "__main__":
    root = tk.Tk()
    AddEmployee_obj = AddEmployee(root)
    root.mainloop()