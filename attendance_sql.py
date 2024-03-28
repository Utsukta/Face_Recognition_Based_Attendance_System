import csv
import tkinter as tk
from tkinter import END, Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, StringVar, Text, ttk,messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
from constants import Constants
import os


my_data=[]
class Attendancesql:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440, 900)
        self.root.maxsize(1440,900)

        #------------Varibales------------
        self.var_employee_id=StringVar()
        self.var_department=StringVar()
        self.var_name=StringVar()
        self.var_phone_number=StringVar()
        self.var_email=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attendance_status=StringVar()
 
        
        #Background Image
        img = Image.open("../Face_recogniton_system/Images/bg.png")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)

        #left Frame
        left_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Employee Details",relief=RIDGE, font=("times new roman", 18 ))
        left_frame.place(x=45, y=20, width=1227, height=300)

        # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)


        # Employee_id
        employee_id_label = Label(left_frame, text="Employee Id", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        employee_id_label.grid(row=0, column=0, padx=10, pady=15)

        education_entry = ttk.Entry(left_frame, textvariable=self.var_employee_id,font=(Constants.Add_Employee_font , 15 ), width=22)
        education_entry.grid(row=0, column=1, padx=10, pady=15, sticky=tk.W)

        # Full Name
        name_label = Label(left_frame,text="Full Name", font=(Constants.Add_Employee_font, 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        name_label.grid(row=0, column=2, padx=10, pady=15)

        name_entry = ttk.Entry(left_frame, textvariable=self.var_name,font=(Constants.Add_Employee_font , 15 ), width=22)
        name_entry.grid(row=0, column=3, padx=10, pady=15)

        # Department
        dep_label = Label(left_frame, text="Department", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        dep_label.grid(row=0, column=4, padx=2, pady=15)

        dep_entry = ttk.Entry(left_frame,textvariable=self.var_department, font=(Constants.Add_Employee_font , 15 ), width=22 )
        dep_entry.grid(row=0, column=5, padx=10, pady=15, sticky=tk.W)

        # Email Address
        email_label = Label(left_frame, text="Email Address", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        email_label.grid(row=1, column=0, padx=10, pady=15)

        email_entry = ttk.Entry(left_frame,textvariable=self.var_email, font=(Constants.Add_Employee_font , 15 ), width=22 )
        email_entry.grid(row=1, column=1, padx=10, pady=15, sticky=tk.W)

        # Department
        time_label = Label(left_frame, text="Time", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        time_label.grid(row=1, column=2, padx=2, pady=15)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time, font=(Constants.Add_Employee_font , 15 ), width=22 )
        time_entry.grid(row=1, column=3, padx=10, pady=15, sticky=tk.W)

        # Department
        date_label = Label(left_frame, text="Date", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        date_label.grid(row=1, column=4, padx=2, pady=15)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date, font=(Constants.Add_Employee_font , 15 ), width=22 )
        date_entry.grid(row=1, column=5, padx=10, pady=15, sticky=tk.W)

        # Attendance
        attendance_label = Label(left_frame, text="Attendance Status", font=(Constants.Add_Employee_font , 15, ),bg=Constants.content_background_color, fg=Constants.frame_content_text_color)
        attendance_label.grid(row=2, column=0, padx=10, pady=15)

        attendance_combo = ttk.Combobox(left_frame,textvariable=self.var_attendance_status, font=(Constants.Add_Employee_font , 12, "bold"), width=28, state="readonly")
        attendance_combo["values"] = ("Status" ,"Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=2, column=1, padx=2, pady=15, sticky=tk.W)

        #button_frame
        btn_frame = Frame(left_frame,bg=Constants.content_background_color)
        btn_frame.place(x=40, y=200, width=1100, height=50)

         #get_button
        get_btn=Button(btn_frame, text="Get Attendance",command=self.get_data,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        get_btn.grid(row=0,column=1)

         #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=2)

        #update_button
        update_btn=Button(btn_frame, text="Update",font=(Constants.Add_Employee_font ,15),command=self.update_data,highlightthickness=0)
        update_btn.grid(row=0,column=3)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=4)

        #reset_button
        reset_btn=Button(btn_frame, text="Reset",command=self.reset_data,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        reset_btn.grid(row=0,column=5)

        #WhiteSpace_between_buttons
        white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        white_space.grid(row=0,column=4)

        #reset_button
        delete_btn=Button(btn_frame, text="Delete",command=self.delete_data,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        delete_btn.grid(row=0,column=5)

        # #WhiteSpace_between_buttons
        # white_space=Label(btn_frame,bg=Constants.content_background_color, width=3)
        # white_space.grid(row=0,column=8)

        #Right Frame
        right_frame = LabelFrame(bg_img,bd=10,bg=Constants.content_background_color,fg=Constants.frame_content_text_color,text="Employee Details",relief=RIDGE, font=("times new roman", 18 ))
        right_frame.place(x=45, y=350, width=1227, height=600)
        
        #table frame
        table_frame = Frame(right_frame,bd=2, bg= "white" ,relief=RIDGE )
        table_frame.place(x=10, y=0, width=1200, height=500)
        
        scroll_x=ttk.Scrollbar(table_frame, orient="horizontal")
        scroll_y=ttk.Scrollbar(table_frame, orient="vertical")
        
        self.attendance_table=ttk.Treeview(table_frame, column=("employee_id","name","dep","email","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set,)
        
        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("employee_id", text="Employee Id")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("email", text="Email")
        self.attendance_table.heading("dep", text="Department")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("attendance", text="Attendance")
        self.attendance_table["show"] = "headings"
        
        self.attendance_table.column("employee_id",width=100)
        self.attendance_table.column("dep",width=200)
        self.attendance_table.column("name",width=200)
        self.attendance_table.column("email",width=200)
        self.attendance_table.column("time",width=150)
        self.attendance_table.column("date",width=150)
        self.attendance_table.column("attendance",width=150)
        self.attendance_table.pack(fill="both", expand=1)
        
        #Bind event with get_cursor method
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)

    # #================fetch data===============#
    # def fetch_data(self,rows):
    #      self.attendance_table.delete(*self.attendance_table.get_children())
    #      for i in rows:
    #          self.attendance_table.insert("",END, values=i)

    #--------reset function------------
    def reset_data(self):
        self.var_employee_id.set(""),
        self.var_department.set("Select Department"),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_time.set(""),
        self.var_date.set("")
        self.var_attendance_status.set("")

    def get_cursor(self , event=""):
        cursor_focus=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_focus)
        data=content["values"]
        if len(data)!=0:
        # print(data)
         self.var_employee_id.set(data[0]),
         self.var_name.set(data[1]),
         self.var_department.set(data[2]),
         self.var_email.set(data[3]),
         self.var_time.set(data[4]),
         self.var_date.set(data[5]),
         self.var_attendance_status.set(data[6]),
    
    def get_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from Attendance")
            data=my_cursor.fetchall()
            if(len(data))!=0:
                self.attendance_table.delete(*self.attendance_table.get_children())
                for i in data:
                    self.attendance_table.insert("",END, values=i)
         
            else:
                self.attendance_table.delete(*self.attendance_table.get_children())
            conn.close()
        except Exception as e:
            print(e)

    def delete_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
            my_curser=conn.cursor()
            check_sql="SELECT employee_id FROM Attendance WHERE employee_id=%s"
            check_val=(self.var_employee_id.get(),)
            my_curser.execute(check_sql,check_val)
            existing_is=my_curser.fetchall()
            print(existing_is)
            print(self.var_date.get())

            if existing_is:
               delete=messagebox.askyesno("Employee Delete Page","Do you want to delete the data?",parent=self.root)
               if delete>0:
                   delete_sql="DELETE FROM Attendance WHERE employee_id=%s AND date=%s AND time=%s"
                   delete_val=(self.var_employee_id.get(),self.var_date.get(),self.var_time.get())
                   print(delete_val)
                   my_curser.execute(delete_sql,delete_val)
                   conn.commit()
                   print("Rows Deleted:", my_curser.rowcount)
                   messagebox.showinfo("Success", "Data deleted successfully")
                   self.get_data()
                   self.reset_data()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

            
    def update_data(self):
            try:
                Update=messagebox.askyesno("Update","Do you want to update the Attendance status",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
                    my_curser=conn.cursor()
                    my_curser.execute("Update Attendance set Attendance_status=%s,date='10-8-2001'where employee_id=%s and date=%s",(
                        
                        self.var_attendance_status.get(),
                        self.var_employee_id.get(),
                        self.var_date.get()
                    ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Employee details successfully update completed",parent=self.root)
                conn.commit()
                self.get_data()
                
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

         
            
if __name__ == "__main__":
    root = tk.Tk()
    Attendance_obj = Attendancesql(root)
    root.mainloop()