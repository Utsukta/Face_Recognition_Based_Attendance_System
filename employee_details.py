from calendar import Calendar
from tkinter import *
import tkinter as tk
import tkinter
from constants import Constants
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

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

        self.var_joined_date = tkinter.StringVar()

        # Left frame
        left_frame = ttk.Frame(root)
        left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        joined_entry = ttk.Entry(left_frame, textvariable=self.var_joined_date, font=(Constants.Add_Employee_font, 15), width=22)
        joined_entry.grid(row=1, column=5, padx=10, pady=15, sticky=tk.W)

        # Button to open calendar
        calendar_button = ttk.Button(left_frame, text="📅", command=self.open_calendar)
        calendar_button.grid(row=1, column=6, padx=5, pady=15, sticky=tk.W)

    def open_calendar(self):
        if not hasattr(self, "calendar_top") or not self.calendar_top.winfo_exists():
            self.calendar_top = tk.Toplevel(root)
            cal = Calendar(self.calendar_top, selectmode='day', locale='en_US', date_pattern='yyyy-mm-dd')
            cal.pack(pady=20, fill="both", expand=True)
            cal.bind("<<CalendarSelected>>", self.update_date)

    def update_date(self, event=None):
        selected_date = event.widget.get_date()
        self.var_joined_date.set(selected_date)

if __name__ == "__main__": 
    root = Tk()
    AddEmployee_obj = Employee_Details(root)
    root.mainloop()