import tkinter as tk
from tkinter import Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, StringVar, Text, ttk
from tkinter import Entry
from PIL import Image, ImageTk
from constants import Constants

class AddEmployee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440, 900)
        self.root.maxsize(1440,900)

        #------------Varibales------------
        self.var_department=StringVar()
        self.var_name=StringVar()
        self.var_phone_number=StringVar()
        self.var_address=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_joined_date=StringVar()
        self.var_salary=StringVar()
        self.var_Emergency_contact=StringVar()
        self.var_education=StringVar()
        
        #Background Image
        img = Image.open("../Face_recogniton_system/Images/splash-bg.png")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)

        #left Frame
        left_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Add Employee",relief=RIDGE, font=("times new roman", 18 ))
        left_frame.place(x=45, y=20, width=1227, height=400)

        # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

        # Full Name
        name_label = Label(left_frame,text="Full Name", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        name_label.grid(row=0, column=0, padx=10, pady=15)

        name_entry = ttk.Entry(left_frame, textvariable=self.var_name,font=(Constants.Add_Employee_font , 15 ), width=22)
        name_entry.grid(row=0, column=1, padx=10, pady=15)

        # Address
        address_label = Label(left_frame, text="Address", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        address_label.grid(row=0, column=2, padx=10, pady=15)

        address_entry = ttk.Entry(left_frame, textvariable=self.var_address,font=(Constants.Add_Employee_font , 15 ), width=22 )
        address_entry.grid(row=0, column=3, padx=10, pady=15, sticky=tk.W)

        # Phone Number
        phone_label = Label(left_frame, text="Phone Number", font=(Constants.Add_Employee_font ,15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        phone_label.grid(row=0, column=4, padx=10, pady=15)

        phone_entry = ttk.Entry(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22 )
        phone_entry.grid(row=0, column=5, padx=10, pady=15, sticky=tk.W)

        # Email Address
        email_label = Label(left_frame, text="Email Address", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        email_label.grid(row=1, column=0, padx=10, pady=15)

        email_entry = ttk.Entry(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22 )
        email_entry.grid(row=1, column=1, padx=10, pady=15, sticky=tk.W)

        # Gender
        gender_label = Label(left_frame, text="Gender", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        gender_label.grid(row=1, column=2, padx=10, pady=15)
        gender_combo = ttk.Combobox(left_frame, font=(Constants.Add_Employee_font , 12, "bold"), width=28, state="readonly")
        gender_combo["values"] = ( "Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=15, sticky=tk.W)

        # Joined Date
        joined_label = Label(left_frame, text="Joined Date", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        joined_label.grid(row=1, column=4, padx=10, pady=15)

        joined_entry = ttk.Entry(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22)
        joined_entry.grid(row=1, column=5, padx=10, pady=15, sticky=tk.W)

        # Department
        dep_label = Label(left_frame, text="Department", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        dep_label.grid(row=2, column=0, padx=2, pady=15)

        dep_combo = ttk.Combobox(left_frame, font=(Constants.Add_Employee_font ,12, "bold"), width=28, state="readonly")
        dep_combo["values"] = ("select Department", "HR", "IT", "Finance", "Marketing", "Operations")
        dep_combo.current(0)
        dep_combo.grid(row=2, column=1, padx=2, pady=15, sticky=tk.W)

        # Salary
        salary_label = Label(left_frame, text="Salary", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        salary_label.grid(row=2, column=2, padx=10, pady=15)

        salary_entry = ttk.Entry(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22 )
        salary_entry.grid(row=2, column=3, padx=10, pady=15, sticky=tk.W)

        # Emergency Contacts
        emergency_label = Label(left_frame, text="Emergency Contacts", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        emergency_label.grid(row=2, column=4, padx=10, pady=15)

        emergency_entry = ttk.Entry(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22 )
        emergency_entry.grid(row=2, column=5, padx=10, pady=15, sticky=tk.W)

        # Educational Background
        education_label = Label(left_frame, text="Educational Background", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        education_label.grid(row=9, column=0, padx=10, pady=15)

        education_entry = ttk.Entry(left_frame, font=(Constants.Add_Employee_font , 15 ), width=22)
        education_entry.grid(row=9, column=1, padx=10, pady=15, sticky=tk.W)

        #radio_buttons1
        radiobtn1=Radiobutton(left_frame,text="Take Photos", font=(Constants.Add_Employee_font ,15),value="yes",bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        radiobtn1.grid(row=10,column=0)

        #radio_buttons1
        radiobtn2=Radiobutton(left_frame,text="No Photos",font=(Constants.Add_Employee_font ,15), value="yes",bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        radiobtn2.grid(row=10,column=1)

        #button_frame
        btn_frame = Frame(left_frame,bg=Constants.content_background_color)
        btn_frame.place(x=40, y=270, width=1100, height=50)

        #save_button
        save_btn=Button(btn_frame, text="Save",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        save_btn.grid(row=0,column=1)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=2)

        #update_button
        update_btn=Button(btn_frame, text="Update",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        update_btn.grid(row=0,column=3)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=4)

        #delete_btn
        delete_btn=Button(btn_frame, text="Delete",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        delete_btn.grid(row=0,column=5)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=6)

        #update_button
        reset_btn=Button(btn_frame, text="Reset",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        reset_btn.grid(row=0,column=7)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=8)

         #delete_btn
        delete_btn=Button(btn_frame, text="Take Photo Samples",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        delete_btn.grid(row=0,column=9)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=10)

        #update_button
        reset_btn=Button(btn_frame, text="Update Photo Samples",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        reset_btn.grid(row=0,column=11)

        #Right Frame
        right_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Employee Details",relief=RIDGE, font=("times new roman", 18 ))
        right_frame.place(x=45, y=440, width=1227, height=400)

        #search system  
        search_frame = LabelFrame(right_frame,bd=2,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Search by system",relief=RIDGE, font=("times new roman", 15 ))
        search_frame.place(x=10, y=10, width=1190, height=80)
        
        search_label = Label(search_frame, text="Search By:", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        search_label.grid(row=0, column=0, padx=10, pady=15)
        
        search_combo = ttk.Combobox(search_frame, font=(Constants.Add_Employee_font , 15, "bold"), width=28, state="readonly")
        search_combo["values"] = ( "select", "Name","Mobile number","Department")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=15, sticky=tk.W)
       
        search_entry = ttk.Entry(search_frame, font=(Constants.Add_Employee_font , 15 ), width=22)
        search_entry.grid(row=0, column=2, padx=10, pady=15, sticky=tk.W)

        search_btn=Button(search_frame, text="Search",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        search_btn.grid(row=0,column=3)
        
        white_space=Label(search_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=4)
        
        showAll_btn=Button(search_frame, text="Show All",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        showAll_btn.grid(row=0,column=5)

        #table frame
        table_frame = Frame(right_frame,bd=2, bg= "white" ,relief=RIDGE )
        table_frame.place(x=10, y=100, width=1200, height=250)
        
        scroll_x=ttk.Scrollbar(table_frame, orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame, orient="vertical")
        
        self.employee_table=ttk.Treeview(table_frame, column=("dep","name","phone","address","email","gender","joined","salary","emergency","education"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,)
        
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading("dep", text="Department ")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("phone", text="Phone number")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("joined", text="Joined")
        self.employee_table.heading("salary", text="Salary")
        self.employee_table.heading("emergency", text="Emergency Contacts")
        self.employee_table.heading("education", text="Education")
        self.employee_table["show"] = "headings"
        

        self.employee_table.column("dep",width=200)
        self.employee_table.column("name",width=200)
        self.employee_table.column("phone",width=200)
        self.employee_table.column("address",width=200)
        self.employee_table.column("email",width=200)
        self.employee_table.column("gender",width=200)
        self.employee_table.column("joined",width=200)
        self.employee_table.column("salary",width=200)
        self.employee_table.column("emergency",width=150)
        self.employee_table.column("education",width=100)
        self.employee_table.pack(fill="both", expand=1)


        #------------function declaration-----------------
        # def add_data(self):


      
if __name__ == "__main__":
    root = tk.Tk()
    AddEmployee_obj = AddEmployee(root)
    root.mainloop()