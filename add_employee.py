import tkinter as tk
from tkinter import Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, StringVar, Text, ttk,messagebox
from tkinter import Entry
from PIL import Image, ImageTk
from constants import Constants
import mysql.connector

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
        self.var_employee_id=StringVar()
        self.var_radio1=StringVar()
 
        
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

        phone_entry = ttk.Entry(left_frame, textvariable=self.var_phone_number,font=(Constants.Add_Employee_font , 15 ), width=22 )
        phone_entry.grid(row=0, column=5, padx=10, pady=15, sticky=tk.W)

        # Email Address
        email_label = Label(left_frame, text="Email Address", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        email_label.grid(row=1, column=0, padx=10, pady=15)

        email_entry = ttk.Entry(left_frame,textvariable=self.var_email, font=(Constants.Add_Employee_font , 15 ), width=22 )
        email_entry.grid(row=1, column=1, padx=10, pady=15, sticky=tk.W)

        # Gender
        gender_label = Label(left_frame, text="Gender", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        gender_label.grid(row=1, column=2, padx=10, pady=15)
        gender_combo = ttk.Combobox(left_frame,textvariable=self.var_gender, font=(Constants.Add_Employee_font , 12, "bold"), width=28, state="readonly")
        gender_combo["values"] = ("Select Gender" ,"Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=15, sticky=tk.W)

        # Joined Date
        joined_label = Label(left_frame, text="Joined Date", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        joined_label.grid(row=1, column=4, padx=10, pady=15)

        joined_entry = ttk.Entry(left_frame, textvariable=self.var_joined_date,font=(Constants.Add_Employee_font , 15 ), width=22)
        joined_entry.grid(row=1, column=5, padx=10, pady=15, sticky=tk.W)

        # Department
        dep_label = Label(left_frame, text="Department", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        dep_label.grid(row=2, column=0, padx=2, pady=15)

        dep_combo = ttk.Combobox(left_frame, textvariable=self.var_department,font=(Constants.Add_Employee_font ,12, "bold"), width=28, state="readonly")
        dep_combo["values"] = ("select Department", "HR", "IT", "Finance", "Marketing", "Operations")
        dep_combo.current(0)
        dep_combo.grid(row=2, column=1, padx=2, pady=15, sticky=tk.W)

        # Salary
        salary_label = Label(left_frame, text="Salary", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        salary_label.grid(row=2, column=2, padx=10, pady=15)

        salary_entry = ttk.Entry(left_frame, textvariable=self.var_salary,font=(Constants.Add_Employee_font , 15 ), width=22 )
        salary_entry.grid(row=2, column=3, padx=10, pady=15, sticky=tk.W)

        # Emergency Contacts
        emergency_label = Label(left_frame, text="Emergency Contacts", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        emergency_label.grid(row=2, column=4, padx=10, pady=15)

        emergency_entry = ttk.Entry(left_frame, textvariable=self.var_Emergency_contact,font=(Constants.Add_Employee_font , 15 ), width=22 )
        emergency_entry.grid(row=2, column=5, padx=10, pady=15, sticky=tk.W)

        # Employee_id
        employee_id_label = Label(left_frame, text="Employee Id", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        employee_id_label.grid(row=9, column=0, padx=10, pady=15)

        education_entry = ttk.Entry(left_frame, textvariable=self.var_employee_id,font=(Constants.Add_Employee_font , 15 ), width=22)
        education_entry.grid(row=9, column=1, padx=10, pady=15, sticky=tk.W)

        #radio_buttons1
        radiobtn1=Radiobutton(left_frame,variable=self.var_radio1,text="Take Photos", font=(Constants.Add_Employee_font ,15),value="yes",bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        radiobtn1.grid(row=10,column=0)

        #radio_buttons2
        radiobtn2=Radiobutton(left_frame,variable=self.var_radio1,text="No Photos",font=(Constants.Add_Employee_font ,15), value="no",bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        radiobtn2.grid(row=10,column=1)

        #button_frame
        btn_frame = Frame(left_frame,bg=Constants.content_background_color)
        btn_frame.place(x=40, y=270, width=1100, height=50)

        #save_button
        save_btn=Button(btn_frame, text="Save",command=self.add_data,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
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
        
        self.employee_table=ttk.Treeview(table_frame, column=("employee_id","dep","name","phone","address","email","gender","joined","salary","emergency","photo_sample"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,)
        
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading("employee_id", text="Employee Id")
        self.employee_table.heading("dep", text="Department ")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading("phone", text="Phone number")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("email", text="Email")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("joined", text="Joined")
        self.employee_table.heading("salary", text="Salary")
        self.employee_table.heading("emergency", text="Emergency Contacts")
        self.employee_table.heading("photo_sample", text="Photo Sample")
        self.employee_table["show"] = "headings"
        
        self.employee_table.column("employee_id",width=100)
        self.employee_table.column("dep",width=200)
        self.employee_table.column("name",width=200)
        self.employee_table.column("phone",width=200)
        self.employee_table.column("address",width=200)
        self.employee_table.column("email",width=200)
        self.employee_table.column("gender",width=200)
        self.employee_table.column("joined",width=200)
        self.employee_table.column("salary",width=200)
        self.employee_table.column("emergency",width=150)
        self.employee_table.column("photo_sample",width=150)
        
        self.employee_table.pack(fill="both", expand=1)


    #------------function declaration-----------------
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_address.get()=="" or self.var_email.get()=="" or self.var_employee_id.get()=="" or self.var_gender.get()=="Select Gender" or self.var_joined_date.get()=="" or self.var_phone_number.get()==""or self.var_Emergency_contact.get()=="" or self.var_salary.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_employee_id.get(),
                self.var_department.get(),
                self.var_name.get(),
                self.var_phone_number.get(),
                self.var_address.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_joined_date.get(),
                self.var_salary.get(),
                self.var_Emergency_contact.get(),
                self.var_radio1.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","All details added",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",str(e), parent=self.root)

            
if __name__ == "__main__":
    root = tk.Tk()
    AddEmployee_obj = AddEmployee(root)
    root.mainloop()