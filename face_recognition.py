from datetime import datetime
import os
import tkinter as tk
from tkinter import END, Button, Label, LabelFrame, Frame, RIDGE, Radiobutton, StringVar, Text, ttk,messagebox
from PIL import Image, ImageTk
from constants import Constants
import mysql.connector
import cv2

class Facerecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.minsize(1440, 900)
        self.root.maxsize(1440,900)

        img = Image.open("../Face_recogniton_system/Images/splash-bg.png")
        img=img.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=150,y=0, width=1280,height=900)


        # instance of shared
        from shared import Shared
        self.shared = Shared(self.root)

        img1 = Image.open("../Face_recogniton_system/Images/ezgif.com-gif-maker-6.webp")
        img1=img1.resize((1280,900), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img1= Label(self.root, image=self.photoimg1)
        # bg_img1.place(x=500,y=50, width=600,height=600)
        bg_img1.place(x=190,y=0, width=1280,height=900)

        #button_frame
        btn_frame = Frame(root)
        btn_frame.place(x=810, y=580, width=175, height=30)

        #face_detector_button
        detector_btn=Button(btn_frame, text="Face Recognition",command=self.face_recognizer,font=(Constants.Add_Employee_font ,20),highlightthickness=0)
        detector_btn.grid(row=0,column=1)


#Marks attendance and saves it in the attendance.csv
    def mark_attendence(self,i,n,d,e):
        with open('attendance.csv',"r+") as f:
            myDataList=f.readlines()
            #Datalyst gives all data in the form of list
            # print(myDataList)

            name_list=[]
            for line in myDataList:
                # print("line is"+line)
                entry=line.split((","))
                print(len(entry))
                if len(entry) >= 6:
                   name_list.append(entry[0])
            # if all(field is not None for field in [i, n, d, e]) and set([i, n, d, e]).isdisjoint(name_list):
            if all(field is not None for field in [i, n, d, e]) and (i not in name_list):
                now=datetime.now()
                d1=now.strftime("%d-%m-%Y")
                dfstring=now.strftime("%H:%M:%S")
                f.writelines(f"{i},{n},{d},{e},{dfstring},{d1},Present\n")
                self.speech("Attendance marked Thank you")
            else: 
            #This gives individual character of data in line(eg: 2,,u,t,s,u..)
            #    for data in line:
            #       print(data)
               
                if len(entry)>=6 :
                    date_fromCsv = line.split(",")[5]
                    now=datetime.now()
                    d1=now.strftime("%d-%m-%Y")
                    dfstring=now.strftime("%H:%M:%S")
                    if(i in name_list and d1==date_fromCsv):
                      pass
                    elif (i in name_list and d1!=date_fromCsv):
                      f.writelines(f"{i},{n},{d},{e},{dfstring},{d1},Present\n")
                      self.speech("Attendance marked Thank you")   
                    else:
                      pass

                else:
                  pass
                # now=datetime.now()
                # d1=now.strftime("%d-%m-%Y")
                # dfstring=now.strftime("%H:%M:%S")
                # if(i in name_list and d1==date_fromCsv):
                #   pass
                # elif (i in name_list and d1!=date_fromCsv):
                #    f.writelines(f"{i},{n},{d},{e},{dfstring},{d1},Present\n")
                #    self.speech("Attendance marked Thank you")   
                # else:
                #   pass          
                    
    def speech(self,text):     
        import platform
    # Check the operating system
        if platform.system() == "Windows": 
        # Code for Windows using pyttsx3
           import pyttsx3
           engine = pyttsx3.init()
           engine.say(text)
           engine.runAndWait()
        elif platform.system() == "Darwin":  # macOS
            import subprocess
            subprocess.call(["say",text])


#Test for database storing attendance for database
    def attendance_mark(self, i, n, d, e):
     try:
        now = datetime.now()
        d1 = now.strftime("%d-%m-%Y")
        dfstring = now.strftime("%H:%M:%S")

        conn = mysql.connector.connect(host="localhost", username="root", password="Cre@ture12;", database="face_recognizer")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM Attendance WHERE employee_id = %s", (i,))
        result = my_cursor.fetchall()

        my_cursor.execute("SELECT date FROM Attendance WHERE employee_id = %s", (i,))
        old_dates = [date_tuple[0] for date_tuple in my_cursor.fetchall()]

        if not result:
            # If no result is found, insert the new record
            my_cursor.execute("INSERT INTO Attendance (employee_id, name, department, email, time, date, Attendance_status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                              (i, n, d, e, dfstring, d1, 'Present'))
            conn.commit()
            self.speech("Attendance Marked Thank you")
            
        else:
            # If result is found, check if any of the dates match d1
            date_match_found = False
            for old_date_str in old_dates:
                if old_date_str == d1:
                    date_match_found = True
                    break
            
            if not date_match_found:
                # If no matching date is found, insert the new record
                my_cursor.execute("INSERT INTO Attendance (employee_id, name, department, email, time, date, Attendance_status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                  (i, n, d, e, dfstring, d1, 'Present'))
                conn.commit()
                self.speech("Attendance Marked Thank you")
                
            else:
                # If a matching date is found, do nothing
                pass
        
        conn.close()
     except Exception as e:
        print(e)


    # def attendance_mark(self,i,n,d,e):
    #    try:
    #       now=datetime.now()
    #       d1=now.strftime("%d-%m-%Y")
    #       dfstring=now.strftime("%H:%M:%S") 

    #       conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
    #       my_cursor=conn.cursor()

    #       my_cursor.execute("SELECT * FROM Attendance WHERE employee_id = %s", (i,))
    #       result = my_cursor.fetchall()

    #       my_cursor.execute("SELECT date FROM Attendance WHERE employee_id=%s",(i,)) 
    #       old_date=my_cursor.fetchall()

    #       old_dates = [date_tuple[0] for date_tuple in old_date]
    #     #   print(old_dates)
    #       for old_date_str in old_dates:
    #          pass
    #         #  print(old_date_str)
    #       if not result:
    #             # now=datetime.now()
    #             # d1=now.strftime("%d-%m-%Y")
    #             # dfstring=now.strftime("%H:%M:%S")  
    #             my_cursor.execute("INSERT INTO Attendance (employee_id, name, department, email, time, date, Attendance_status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    #                           (i, n, d, e, dfstring, "10-02-2000", 'Present'))
    #             conn.commit()
    #             print("Attendance marked successfully")
    #             print("already exists")
    #       elif result and old_date_str!=d1:
    #          print(1)
    #         # my_cursor.execute("SELECT date FROM Attendance WHERE employee_id=%s",(i,)) 
    #         # old_date=my_cursor.fetchall()
    #         # print(old_date)
    #         # # Extract the date string from each tuple in old_date
    #         # old_dates = [date_tuple[0] for date_tuple in old_date]
    #         # print(old_dates)
    #         # for old_date_str in old_dates:
    #         #    print(old_date_str)
    #         # if result and old_date_str==d1:
    #         #    pass
    #         # elif result and old_date_str!=d1:
    #         #    print("hello")
        
    #         #       my_cursor.execute("INSERT INTO Attendance (employee_id, name, department, email, time, date, Attendance_status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    #         #                   (i, n, d, e, dfstring, d1, 'Present'))
    #         #       conn.commit()
    #         #   else:
    #         #       pass
    #       conn.close()
    #    except Exception as e:
    #       print(e)
    #    finally:
    #       conn.close()
          

    # def attendance_mark(self, i, n, d, e):
    #  try:
    #     conn = mysql.connector.connect(host="localhost", username="root", password="Cre@ture12;", database="face_recognizer")
    #     my_cursor = conn.cursor()
    #     # Check if the ID already exists in the Attendance table
    #     my_cursor.execute("SELECT * FROM Attendance WHERE employee_id = %s", (i,))
    #     result = my_cursor.fetchall()
    #     # If the ID does not exist, insert the new record
    #     if not result:
    #         now = datetime.now()
    #         d1 = now.strftime("%d-%m-%Y")
    #         dfstring = now.strftime("%H:%M:%S")
    #         my_cursor.execute("INSERT INTO Attendance (employee_id, name, department, email, time, date, Attendance_status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    #                           (i, n, d, e, dfstring, d1, 'Present'))
    #         conn.commit()
    #         print("Attendance marked successfully")
    #     else:
    #        pass
           
    #     # conn.commit()
    #     conn.close()
    #  except Exception as e:
    #     print(e)


    def face_recognizer(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            #Coordinates to draw the rectangle
            for  (x,y,w,h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

                id,predict=clf.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100*(1-predict/300)))
                # confidence=(float("%.2f" %(id)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Cre@ture12;",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("SELECT Name from employee WHERE employee_id="+str((id)))
                
                n=my_cursor.fetchone()
                if n is not None:
                 n="+".join(n)
                # n = "+".join([str(n)])
                # print(n)

                my_cursor.execute("SELECT employee_id from employee WHERE employee_id="+str((id)))
                i=my_cursor.fetchone()
                # i = "+".join([str(i)])
                if i is not None:
                 i="+".join(i)
                
                # i="+".join(i)
                my_cursor.execute("SELECT department from employee WHERE employee_id="+str((id)))
                d=my_cursor.fetchone()
                if d is not None:
                 d="+".join(d)
                # d = "+".join([str(d)])
                # d="+".join(d)

                my_cursor.execute("SELECT email from employee WHERE employee_id="+str((id)))
                e=my_cursor.fetchone()
                if e is not None:
                 e="+".join(e)
                # e = "+".join([str(e)])
                # e="+".join(e)
             

                if confidence>80:
                    # if i is not None and n is not None and d is not None and e is not None:  
                    cv2.putText(img,f"Employee ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Emaill Address:{e}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,n,d,e)
                    self.attendance_mark(i,n,d,e)
                elif confidence<80:
                   cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                   cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    # if i is not None and n is not None and d is not None and e is not None:

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture=cv2.VideoCapture(0)

        while True:
            ret,img=video_capture.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face Reconition",img)
            if cv2.waitKey(1)==13:
                break
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    facerecognition_obj = Facerecognition(root)
    root.mainloop()