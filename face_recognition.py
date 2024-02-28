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

         #button_frame
        btn_frame = Frame(root)
        btn_frame.place(x=700, y=270, width=150, height=25)

        #save_button
        save_btn=Button(btn_frame, text="Face Detector",command=self.face_recognizer,font=(Constants.Add_Employee_font ,15),highlightthickness=0)
        save_btn.grid(row=0,column=1)


#Marks attendance and saves it in the attendance.csv
    def mark_attendence(self,i,n,d,e):
        with open('attendance.csv',"r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (n not in name_list) and (d not in name_list) and (e not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d\%m\%Y")
                dfstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{e},{dfstring},{d1},Present")
        

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
                n="+".join(n)
                # n = "+".join([str(n)])
                print(n)


                my_cursor.execute("SELECT employee_id from employee WHERE employee_id="+str((id)))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("SELECT department from employee WHERE employee_id="+str((id)))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("SELECT email from employee WHERE employee_id="+str((id)))
                e=my_cursor.fetchone()
                e="+".join(e)
             

                if confidence>77:
                    cv2.putText(img,f"Employee ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Emaill Address:{e}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,n,d,e)

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