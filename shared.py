from tkinter import *
from PIL import Image, ImageTk
from constants import Constants
from add_employee import AddEmployee 
from employee_details import Employee_Details
from main import Face_Recognition_Attendance_System
from photos import Photos
from train import Train

# from employee_details import Employee_Details

class Shared:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.title("Face Recognition system")
        self.shared_frame = Frame(root, bg=Constants.shared_background_color)
        self.shared_frame.place(x=0, y=0, width=190, height=900)
        #logo
        logo_img = Image.open("../Face_recogniton_system/Images/rps_logo-preview.png")
        logo_img=logo_img.resize((100,45))
        self.logo_img = ImageTk.PhotoImage(logo_img)

        #logo label
        logo_label = Label(self.root, image=self.logo_img, bg=Constants.shared_background_color)
        logo_label.place(x=5, y=20)

        #Home label
        home_label= Label(text="Home",bg=Constants.shared_background_color,foreground=Constants.shared_text_color, )
        home_label.bind("<Button>",self.on_home_label_clicked)
        home_label.place(x=35, y=150)

        #Add Employee Label
        Add_Employee_label= Label( text="Add Employee",bg=Constants.shared_background_color,foreground=Constants.shared_text_color )
        Add_Employee_label.bind("<Button>",self.on_add_employee_label_clicked)
        Add_Employee_label.place(x=35, y=190)

        #Employee Details Label
        Add_Employee_details_label= Label( text="Employee Details",bg=Constants.shared_background_color,foreground=Constants.shared_text_color )
        Add_Employee_details_label.bind("<Button>",self.on_employee_details_label_clicked)
        Add_Employee_details_label.place(x=35, y=230)

        #Photos Label
        Photos_label= Label( text="Photos",bg=Constants.shared_background_color,foreground=Constants.shared_text_color )
        Photos_label.bind("<Button>",self.on_photos_label_clicked)
        Photos_label.place(x=35, y=270)

        #Train Data Label
        Train_Data_label= Label( text="Train Data",bg=Constants.shared_background_color,foreground=Constants.shared_text_color )
        Train_Data_label.bind("<Button>",self.on_train_data_label_clicked)
        Train_Data_label.place(x=35, y=310)

        #Face Recognition Label
        Face_Recognition_label= Label( text="Face Recognition",bg=Constants.shared_background_color,foreground=Constants.shared_text_color )
        Face_Recognition_label.bind("<Button>",self.on_face_recognition_label_clicked)
        Face_Recognition_label.place(x=35, y=350)

        #Attendance Label
        Attendance_label= Label( text="Attendance",bg=Constants.shared_background_color,foreground=Constants.shared_text_color )
        Attendance_label.bind("<Button>",self.on_attendance_label_clicked)
        Attendance_label.place(x=35, y=390)

        #Exit Label
        Exit_label= Label( text="Exit",bg=Constants.shared_background_color,foreground=Constants.shared_text_color )
        Exit_label.bind("<Button>",self.on_attendance_label_clicked)
        Exit_label.place(x=35, y=750)

    def on_home_label_clicked(self,event):
            self.instancee= Face_Recognition_Attendance_System(self.root)
            print("clicked home")
    def on_add_employee_label_clicked(self,event):
            # self.root.withdraw()
        #     self.new_window=Toplevel(self.root)
            self.app=AddEmployee(self.root)
            # self.root.iconify()
            print("clicked emploee")
    def on_employee_details_label_clicked(self,event):
        #     self.new_window=Toplevel(self.root)
            self.app=Employee_Details(self.root)
            # self.root.withdraw()
            print("clicked details") 
    def on_photos_label_clicked(self,event):
            self.app=Photos(self.root)
            
            print("clicked photos")
    def on_train_data_label_clicked(self,event):
            self.app=Train(self.root)
            print("clicked train data")
    def on_face_recognition_label_clicked(self,event):
            print("clicked face recognition")
    def on_attendance_label_clicked(self,event):
            print("clicked attendance")   
    def on_Exit_label_clicked(event):
            print("clicked exit")
   
print("done")
if __name__ == "__main__":
        root = Tk()
        shared_obj= Shared(root)
        root.mainloop()


