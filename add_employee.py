import datetime
import os
import re
import tkinter as tk
from tkinter import END, Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, StringVar,ttk,messagebox
from tkinter import Entry
from PIL import Image, ImageTk
from constants import Constants
import mysql.connector
import cv2

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

        #For searching
        self.var_search_combo=StringVar()
        self.var_search_entry=StringVar()
 
        
        #Background Image
        img = Image.open("../Face_recogniton_system/Images/splash-bg.png")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)

        #top Frame
        top_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Add Employee",relief=RIDGE, font=("times new roman", 18 ))
        top_frame.place(x=45, y=20, width=1227, height=400)

        # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

        # Full Name
        name_label = Label(top_frame,text="Full Name", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        name_label.grid(row=0, column=0, padx=10, pady=15)

        name_entry = ttk.Entry(top_frame, textvariable=self.var_name,font=(Constants.Add_Employee_font , 15 ), width=22)
        name_entry.grid(row=0, column=1, padx=10, pady=15)

        # Address
        address_label = Label(top_frame, text="Address", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        address_label.grid(row=0, column=2, padx=10, pady=15)

        address_entry = ttk.Entry(top_frame, textvariable=self.var_address,font=(Constants.Add_Employee_font , 15 ), width=22 )
        address_entry.grid(row=0, column=3, padx=10, pady=15, sticky=tk.W)

        # Phone Number
        phone_label = Label(top_frame, text="Phone Number", font=(Constants.Add_Employee_font ,15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        phone_label.grid(row=0, column=4, padx=10, pady=15)

        phone_entry = ttk.Entry(top_frame, textvariable=self.var_phone_number,font=(Constants.Add_Employee_font , 15 ), width=22 )
        phone_entry.grid(row=0, column=5, padx=10, pady=15, sticky=tk.W)

        # Email Address
        email_label = Label(top_frame, text="Email Address", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        email_label.grid(row=1, column=0, padx=10, pady=15)

        email_entry = ttk.Entry(top_frame,textvariable=self.var_email,font=(Constants.Add_Employee_font , 15 ), width=22 )
        email_entry.grid(row=1, column=1, padx=10, pady=15, sticky=tk.W)


        # Gender
        gender_label = Label(top_frame, text="Gender", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        gender_label.grid(row=1, column=2, padx=10, pady=15)

        gender_combo = ttk.Combobox(top_frame,textvariable=self.var_gender, font=(Constants.Add_Employee_font , 12, "bold"), width=28, state="readonly")
        gender_combo["values"] = ("Select Gender" ,"Male", "Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=2, pady=15, sticky=tk.W)

        # Joined Date
        joined_label = Label(top_frame, text="Joined Date", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        joined_label.grid(row=1, column=4, padx=10, pady=15)


        # joined_entry = DateEntry(top_frame, textvariable=self.var_joined_date, date_pattern='yyyy-mm-dd', background='darkblue', foreground='white', selectbackground='lightgray', selectforeground='black', bordercolor='white', othermonthforeground='gray50', othermonthbackground='gray10', arrowscolor='white')
        # joined_entry.grid(row=1, column=5, padx=10, pady=15)


        joined_entry = ttk.Entry(top_frame, textvariable=self.var_joined_date,font=(Constants.Add_Employee_font , 15 ), width=22)
        joined_entry.grid(row=1, column=5, padx=10, pady=15, sticky=tk.W)

        # Department
        dep_label = Label(top_frame, text="Department", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        dep_label.grid(row=2, column=0, padx=2, pady=15)

        dep_combo = ttk.Combobox(top_frame, textvariable=self.var_department,font=(Constants.Add_Employee_font ,12, "bold"), width=28, state="readonly")
        dep_combo["values"] = ("Select Department", "HR", "IT", "Finance", "Marketing", "Operations")
        dep_combo.current(0)
        dep_combo.grid(row=2, column=1, padx=2, pady=15, sticky=tk.W)

        # Salary
        salary_label = Label(top_frame, text="Salary", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        salary_label.grid(row=2, column=2, padx=10, pady=15)

        salary_entry = ttk.Entry(top_frame, textvariable=self.var_salary,font=(Constants.Add_Employee_font , 15 ), width=22 )
        salary_entry.grid(row=2, column=3, padx=10, pady=15, sticky=tk.W)

        # Emergency Contacts
        emergency_label = Label(top_frame, text="Emergency Contacts", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        emergency_label.grid(row=2, column=4, padx=10, pady=15)

        emergency_entry = ttk.Entry(top_frame, textvariable=self.var_Emergency_contact,font=(Constants.Add_Employee_font , 15 ), width=22 )
        emergency_entry.grid(row=2, column=5, padx=10, pady=15, sticky=tk.W)

        # Employee_id
        employee_id_label = Label(top_frame, text="Employee Id", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        employee_id_label.grid(row=9, column=0, padx=10, pady=15)

        education_entry = ttk.Entry(top_frame, textvariable=self.var_employee_id,font=(Constants.Add_Employee_font , 15 ), width=22)
        education_entry.grid(row=9, column=1, padx=10, pady=15, sticky=tk.W)

        #radio_buttons1
        radiobtn1=Radiobutton(top_frame,variable=self.var_radio1,text="Take Photos",font=(Constants.Add_Employee_font ,15),value="yes",bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        radiobtn1.grid(row=10,column=0)

        #radio_buttons2
        radiobtn2=Radiobutton(top_frame,variable=self.var_radio1,text="No Photos",font=(Constants.Add_Employee_font ,15), value="no",bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        radiobtn2.grid(row=10,column=1)

        #button_frame
        btn_frame = Frame(top_frame,bg=Constants.content_background_color)
        btn_frame.place(x=40, y=270, width=1100, height=50)

        #save_button
        save_btn=Button(btn_frame, text="Save",command=self.add_data,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        save_btn.grid(row=0,column=1)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=2)

        #update_button
        update_btn=Button(btn_frame, text="Update",command=self.update_data,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        update_btn.grid(row=0,column=3)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=4)

        #delete_btn
        delete_btn=Button(btn_frame, text="Delete",command=self.delete_data,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        delete_btn.grid(row=0,column=5)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=6)

        #reset_button
        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        reset_btn.grid(row=0,column=7)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=8)

        #Take_Photo_btn
        add_photo_btn=Button(btn_frame, text="Add Photo Samples",command=self.generate_dataset,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        add_photo_btn.grid(row=0,column=9)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=10)

        #update_button
        # update_photo_btn=Button(btn_frame, text="Update Photo Samples",font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        # update_photo_btn.grid(row=0,column=11)


        #bottom Frame
        bottom_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Employee Details",relief=RIDGE, font=("times new roman", 18 ))
        bottom_frame.place(x=45, y=440, width=1227, height=400)

        #search system  
        search_frame = LabelFrame(bottom_frame,bd=2,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Search by system",relief=RIDGE, font=("times new roman", 15 ))
        search_frame.place(x=10, y=10, width=1190, height=80)
        
        search_label = Label(search_frame, text="Search By:", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        search_label.grid(row=0, column=0, padx=10, pady=15)
        
        search_combo = ttk.Combobox(search_frame, font=(Constants.Add_Employee_font , 15, "bold"),textvariable=self.var_search_combo, width=28, state="readonly")
        search_combo["values"] = ( "Select", "Department","Name","Phone number","Email")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=15, sticky=tk.W)
       
        search_entry = ttk.Entry(search_frame, font=(Constants.Add_Employee_font , 15 ),textvariable=self.var_search_entry, width=22)
        search_entry.grid(row=0, column=2, padx=10, pady=15, sticky=tk.W)

        search_btn=Button(search_frame, text="Search",font=(Constants.Add_Employee_font ,15),command=self.search,highlightthickness=0)
        search_btn.grid(row=0,column=3)
        
        white_space=Label(search_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=4)
        
        clear_btn=Button(search_frame, text="Clear",font=(Constants.Add_Employee_font ,15),command=self.clear,highlightthickness=0)
        clear_btn.grid(row=0,column=5)

        #table frame
        table_frame = Frame(bottom_frame,bd=2, bg= "white" ,relief=RIDGE )
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
        
        #Bind event with get_cursor method
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #------------function declaration-----------------
    def add_data(self):
        if self.var_department.get()=="Select Department" or self.var_address.get()=="" or self.var_email.get()=="" or self.var_employee_id.get()=="" or self.var_gender.get()=="Select Gender" or self.var_joined_date.get()=="" or self.var_phone_number.get()==""or self.var_Emergency_contact.get()=="" or self.var_salary.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        elif not self.validate_form():
            pass
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
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
                self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All details added",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",str(e), parent=self.root)

    #================fetch data===============#
    def fetch_data(self):
     conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
     my_cursor=conn.cursor()
     my_cursor.execute("select * from employee")
     data=my_cursor.fetchall()
     
     #if the data contains rows in it
     if len(data)!=0:
         self.employee_table.delete(*self.employee_table.get_children())
         for i in data:
             self.employee_table.insert("",END, values=i)
         
     else:
          self.employee_table.delete(*self.employee_table.get_children())
     conn.close()

         
            
     #============get cursor===========#    
    def get_cursor(self , event=""):
        cursor_focus=self.employee_table.focus()
        content=self.employee_table.item(cursor_focus)
        data=content["values"]
        print(data)
        if len(data) >= 11:

         self.var_employee_id.set(data[0]),
         self.var_department.set(data[1]),
         self.var_name.set(data[2]),
         self.var_phone_number.set(data[3]),
         self.var_address.set(data[4]),
         self.var_email.set(data[5]),
         self.var_gender.set(data[6]),
         self.var_joined_date.set(data[7]), 
         self.var_salary.set(data[8]),
         self.var_Emergency_contact.set(data[9]),
         self.var_radio1.set(data[10])


        # self.var_employee_id.set(data[0]),
        # self.var_department.set(data[1]),
        # self.var_name.set(data[2]),
        # self.var_phone_number.set(data[3]),
        # self.var_address.set(data[4]),
        # self.var_email.set(data[5]),
        # self.var_gender.set(data[6]),
        # self.var_joined_date.set(data[7]), 
        # self.var_salary.set(data[8]),
        # self.var_Emergency_contact.set(data[9]),
        # self.var_radio1.set(data[10])

    #--------update function--------------
    def update_data(self):
        if self.var_department.get()=="Select Department" or self.var_address.get()=="" or self.var_email.get()=="" or self.var_employee_id.get()=="" or self.var_gender.get()=="Select Gender" or self.var_joined_date.get()=="" or self.var_phone_number.get()==""or self.var_Emergency_contact.get()=="" or self.var_salary.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        elif not self.validate_form():
            pass
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
                    my_curser=conn.cursor()
                    my_curser.execute("Update employee set department=%s,Name=%s,Phone=%s,address=%s,email=%s,gender=%s,joined=%s,salary=%s,emergency_contact=%s,Photo_sample=%s where employee_id=%s",(
                        
                        self.var_department.get(),
                        self.var_name.get(),
                        self.var_phone_number.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_joined_date.get(),
                        self.var_salary.get(),
                        self.var_Emergency_contact.get(),
                        self.var_radio1.get(),
                        self.var_employee_id.get(),

                    ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Employee details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)


    #--------delete function--------------
    def delete_data(self):
        if self.var_employee_id.get()=="":
            messagebox.showerror("Error","Employee Id is required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
            my_curser=conn.cursor()
            check_sql="SELECT employee_id FROM employee WHERE employee_id=%s"
            check_val=(self.var_employee_id.get(),)
            my_curser.execute(check_sql,check_val)
            existing_is=my_curser.fetchone()
            # print("is exising is "+str(existing_is))

            if existing_is:
               delete=messagebox.askyesno("Employee Delete Page","Do you want to delete the data?",parent=self.root)
               if delete>0:
                 #delete the images from data folder
                if not os.listdir("data"):
                  pass
                else:
                 id=self.var_employee_id.get()
                 #Since 100 samples are taken
                 for i in range(1,101): 
                    # print(i)
                    # print("exising is "+'data/user.'+id+'.'+str(i)+'.jpg')
                    os.remove('data/user.'+id+'.'+str(i)+'.jpg')
              
                delete_sql="DELETE FROM employee WHERE employee_id=%s"
                delete_val=(self.var_employee_id.get(),)
                my_curser.execute(delete_sql,delete_val)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                messagebox.showinfo("Delete","Employee Details Succesfully Deleted")
                
                conn.close()
                           
                
               else:
                if not delete:
                    return
            else:
                messagebox.showerror("ID not found","Employee Id is not available")
           

    #--------reset function------------
    def reset_data(self):
        self.var_employee_id.set(""),
        self.var_department.set("Select Department"),
        self.var_name.set(""),
        self.var_phone_number.set(""),
        self.var_address.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select Gender"),
        self.var_joined_date.set(""), 
        self.var_salary.set(""),
        self.var_Emergency_contact.set(""),
        self.var_radio1.set("")
        

    #-----------generate data or take photo sample------------
    #Capturing images and updating database
    def generate_dataset(self):
        if self.var_department.get()=="Select Department" or self.var_address.get()=="" or self.var_email.get()=="" or self.var_employee_id.get()=="" or self.var_gender.get()=="Select Gender" or self.var_joined_date.get()=="" or self.var_phone_number.get()==""or self.var_Emergency_contact.get()=="" or self.var_salary.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
                my_curser=conn.cursor()
                my_curser.execute("SELECT * FROM employee")
                my_result=my_curser.fetchall()
                id=self.var_employee_id.get()
                # id=0
                # for x in my_result:
                #      id+=1
                my_curser.execute("Update employee set department=%s,Name=%s,Phone=%s,address=%s,email=%s,gender=%s,joined=%s,salary=%s,emergency_contact=%s,Photo_sample=%s where employee_id=%s",(
                        
                        self.var_department.get(),
                        self.var_name.get(),
                        self.var_phone_number.get(),
                        self.var_address.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_joined_date.get(),
                        self.var_salary.get(),
                        self.var_Emergency_contact.get(),
                        self.var_radio1.get(),
                        self.var_employee_id.get(),

                    ))
                conn.commit()
                conn.close()


                    #----------load predefined data on face frontals from opencv---------
                face_classifer=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_classifer.detectMultiScale(gray,1.3,5)
                         #scaling_factor=1.3
                         #minimum neighbour=5

                         for(x,y,w,h) in faces:
                             face_cropped=img[y:y+h,x:x+w]
                             return face_cropped
                         
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                            cv2.imshow("Cropped face",face)


                        #Enter gare paxi close garni
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating datasets Completed")
                
                # self.add_data()
                self.fetch_data()
                # self.reset_data()

                              
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

    def validate_form(self):
        email = self.var_email.get()
        phone = self.var_phone_number.get()
        emergency_contact=self.var_Emergency_contact.get()
        salary= self.var_salary.get()
        joined_date=self.var_joined_date.get()

        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid Email Address")
            return False
        elif not self.validate_phone(phone):
            messagebox.showerror("Error", "Invalid Phone Number")
        elif not self.validate_phone(emergency_contact):
            messagebox.showerror("Error", "Invalid Emergency Contact")
        elif not self.validate_salary(salary):
            messagebox.showerror("Error", "Salary contains only numerical number")
        elif not self.validate_joined_date(joined_date):
            messagebox.showerror("Error", "Correct format for date is DD-MM-YYYY")
        elif not self.compare_dates(joined_date):
            messagebox.showerror("Error", "Future joined date is not valid")
        else:
            return True
            

    def validate_email(self, email):
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(regex, email)

    def validate_phone(self, phone):
        # Simple phone number validation: 10 digits, no characters
        regex = r"^\d{10}$"
        return re.match(regex, phone)
    
    def validate_salary(self,salary):
        regex=r"[0-9]"
        return re.match(regex,salary)
    
    def validate_joined_date(self,date):
        regex=r"^(3[01]|[12][0-9]|0?[1-9])(\-)(1[0-2]|0?[1-9])\2([0-9]{2})?[0-9]{2}$"
        return re.match(regex,date)
     
    def compare_dates(self,date):
        print(date)
        given_date=datetime.datetime.strptime(date,"%d-%m-%Y").date()
        print(given_date)
        current_date=datetime.date.today()
        print(current_date)
        if(given_date>current_date):
            return False
        else:
            return True
    
    def search(self):
        search_combo_value=self.var_search_combo.get()
        search_entry_value=self.var_search_entry.get()
        # print(search_combo_value +"and"+ search_entry_value)
        conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
        my_cursor=conn.cursor()
        sql_query="SELECT * FROM employee WHERE 1=1"
        if search_combo_value != "Select" and search_entry_value:
            if search_combo_value == "Name":
               sql_query += f" AND Name='{search_entry_value}'"
            elif search_combo_value == "Department":
               sql_query += f" AND department='{search_entry_value}'"
            elif search_combo_value == "Phone number":
               sql_query += f" AND Phone='{search_entry_value}'"
            elif search_combo_value == "Email":
               sql_query += f" AND email='{search_entry_value}'"
        # if(search_combo_value=="Select" and search_entry_value==""):
        #     sql_query="SELECT * FROM employee"
        # elif(search_combo_value=="Name"):
        #     sql_query="SELECT * FROM employee WHERE Name='%s'" %search_entry_value
        # elif(search_combo_value=="Department"):
        #     sql_query="SELECT * FROM employee WHERE department='%s'" %search_entry_value
        # elif(search_combo_value=="Phone number"):
        #     sql_query="SELECT * FROM employee WHERE Phone='%s'" %search_entry_value
        # elif(search_combo_value=="Email"):
        #     sql_query="SELECT * FROM employee WHERE email='%s'" %search_entry_value
        my_cursor.execute(sql_query)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in rows:
                print(i)
                self.employee_table.insert("",END, values=i)
            #linear searching algorithm
            # data = self.employee_table.get_children()
            # arrays=[]
            # for item in data:
            #      values = self.employee_table.item(item, 'values')
            #      arrays.append((values))
            # for row in arrays:
            #     if search_entry_value in row:
            #         print(row)
            #         self.employee_table.delete(*self.employee_table.get_children())
            #         self.employee_table.insert("",END, values=row)
                     
    def clear(self):
        self.var_search_combo.set("Select")
        self.var_search_entry.set("")
        conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM employee")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in rows:
                self.employee_table.insert("",END, values=i)

            
if __name__ == "__main__":
    root = tk.Tk()
    AddEmployee_obj = AddEmployee(root)
    root.mainloop()