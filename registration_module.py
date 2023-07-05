import cv2,os
import csv
import mysql.connector
from tkinter import *
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import mysql.connector
import os
import time

import Teacher
import register as rg
import Student_d as sd
import forg as fg
import Teacher as Te
import page as pa

class registration:
    def __init__(self):
        
            
        self.harcascadePath = "haar_face.xml"
        
            
    def assure_path_exists(self, path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)
            
    def add_student_details(self, serial, columns):
        exists = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists:
            with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)
            csvFile1.close()
        else:
            with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
            
        self.detector = cv2.CascadeClassifier(self.harcascadePath)
        ft = open("ld.txt", "r")
        a,b=ft.read().split(",")
        ft.close()
        nam=""
        self.Id =a
        try:
            con = mysql.connector.connect(host="localhost", username="root", password="Aman", database="login_d")
            my_c = con.cursor()
            my_c.execute("select * from login where Username=%s Type=%s",(a,b))
            data = my_c.fetchone()
            fn=data[3]
            ln=data[4]
            nam=fn+" "+ln

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.window)


        self.name =nam
        
        return serial, self.detector, self.Id, self.name
    
    def edit_image(self, sampleNum, img, serial):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # incrementing sample number
            sampleNum = sampleNum + 1
            # saving the captured face in the dataset folder TrainingImage
            cv2.imwrite("TrainingImage\ " + self.name + "." + str(serial) + "." + self.Id + '.' + str(sampleNum) + ".jpg",
                        gray[y:y + h, x:x + w])
            # display the frame
            cv2.imshow('Taking Images', img)
                           
        return gray, faces, sampleNum
    
    def append_data(self, serial):
        res = "Images Taken for ID : " + self.Id
        row = [serial, '', self.Id, '', self.name]
        with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        print(res)
            
            
        
def main():
    reg = registration()
    columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
    reg.assure_path_exists("StudentDetails/")
    reg.assure_path_exists("TrainingImage/")
    serial = 0
    
    serial, detector, Id, name = reg.add_student_details(serial, columns)
    
    if ((name.isalpha()) or (' ' in name)):
        cam = cv2.VideoCapture(0)
        
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray, faces, sampleNum = reg.edit_image(sampleNum, img, serial)
            
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 100:
                break
            
        cam.release()
        cv2.destroyAllWindows()
        reg.append_data(serial)
        
    else:
        if (name.isalpha() == False):
            res = "Enter Correct name"
            print(res)
            
if __name__=="__main__":
    main()
            
