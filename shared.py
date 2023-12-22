from tkinter import *
from PIL import Image, ImageTk
from constants import Constants
from add_employee import AddEmployee 
from employee_details import Employee_Details

# from employee_details import Employee_Details

class Shared:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.title("Face Recognition system")
        self.content_frame = Frame(root, bg=Constants.shared_background_color)
        self.content_frame.place(x=0, y=0, width=160, height=900)
        #logo
        logo_img = Image.open("/Users/utsuktakhatri/Desktop/Face_recogniton_system/Images/rps_logo-preview.png")
        logo_img=logo_img.resize((100,45))
        self.logo_img = ImageTk.PhotoImage(logo_img)

        #logo label
        logo_label = Label(self.root, image=self.logo_img, bg=Constants.shared_background_color)
        logo_label.place(x=5, y=20)

        #Home label
        home_label= Label(text="Home",bg="lightgrey",foreground="black", )
        home_label.bind("<Button>",self.on_home_label_clicked)
        home_label.place(x=35, y=150)

        #Add Employee Label
        Add_Employee_label= Label( text="Add Employee",bg="lightgrey",foreground="black" )
        Add_Employee_label.bind("<Button>",self.on_add_employee_label_clicked)
        Add_Employee_label.place(x=35, y=190)

        #Employee Details Label
        Add_Employee_details_label= Label( text="Employee Details",bg="lightgrey",foreground="black" )
        Add_Employee_details_label.bind("<Button>",self.on_employee_details_label_clicked)
        Add_Employee_details_label.place(x=35, y=230)

        #Photos Label
        Photos_label= Label( text="Photos",bg="lightgrey",foreground="black" )
        Photos_label.bind("<Button>",self.on_photos_label_clicked)
        Photos_label.place(x=35, y=270)

        #Train Data Label
        Train_Data_label= Label( text="Train Data",bg="lightgrey",foreground="black" )
        Train_Data_label.bind("<Button>",self.on_train_data_label_clicked)
        Train_Data_label.place(x=35, y=310)

        #Face Recognition Label
        Face_Recognition_label= Label( text="Face Recognition",bg="lightgrey",foreground="black" )
        Face_Recognition_label.bind("<Button>",self.on_face_recognition_label_clicked)
        Face_Recognition_label.place(x=35, y=350)

        #Attendance Label
        Attendance_label= Label( text="Attendance",bg="lightgrey",foreground="black" )
        Attendance_label.bind("<Button>",self.on_attendance_label_clicked)
        Attendance_label.place(x=35, y=390)

        #Exit Label
        Exit_label= Label( text="Exit",bg="lightgrey",foreground="black" )
        # Add_Employee_label.bind("<Button>",self.on_attendance_label_clicked)
        Exit_label.place(x=35, y=750)

    def on_home_label_clicked(self,event):
            print("clicked home")
    def on_add_employee_label_clicked(self,event):
            
            # self.root.withdraw()
            self.new_window=Toplevel(self.root)
            self.app=AddEmployee(self.new_window)
            # self.root.iconify()
          
    
            
            print("clicked emploee")
    def on_employee_details_label_clicked(self,event):
            self.new_window=Toplevel(self.root)
            self.app=Employee_Details(self.new_window)
         
            # self.root.withdraw()
            print("clicked details")
    def on_photos_label_clicked(self,event):
            print("clicked photos")
    def on_train_data_label_clicked(self,event):
            print("clicked train data")
    def on_face_recognition_label_clicked(self,event):
            print("clicked face recognition")
    def on_attendance_label_clicked(self,event):
            print("clicked attendance")   
    # def on_home_label_clicked(event):
    #         print("clicked")
    # def on_home_label_clicked(event):
    #         print("clicked")




