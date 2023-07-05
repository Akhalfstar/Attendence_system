from tkinter import *
from tkinter import ttk
from PIL import Image
import csv
from tkinter import messagebox
import mysql.connector
import time
import os
import cv2 as cv2
import Login_page as lg
import os
import numpy as np
import register as rg
import Student_d as sd
import forg as fg
import Teacher as Te
from registration_module import registration
import page as pa




class Students:
    def __init__(self,window):
        self.window=window
        self.window.title("Team EXPO Student")
        def btn_clicked0():
            print("Resistration is running")

            def assure_path_exists(path):
                dir = os.path.dirname(path)
                if not os.path.exists(dir):
                    os.makedirs(dir)

            def check_haarcascadefile():
                exists = os.path.isfile("haar_face.xml")
                if exists:
                    pass
                else:
                    print("haar_cascade file missing")

            check_haarcascadefile()
            columns = ['SERIAL NO.', '', 'ID', '', 'NAME']
            assure_path_exists("StudentDetails/")
            assure_path_exists("TrainingImage/")
            serial = 0
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
            self.detector = cv2.CascadeClassifier("haar_face.xml")
            # name=""
            # Id=""
            # ft = open("ld.txt", "r")
            # a, b = ft.read().split(",")
            # ft.close()
            # nam = ""
            # self.Id = a
            # try:
            #     con = mysql.connector.connect(host="localhost", username="root", password="Aman", database="login_d")
            #     my_c = con.cursor()
            #     my_c.execute("select * from login where Username=%s Type=%s",())
            #     data = my_c.fetchone()
            #     fn = data[3]
            #     ln = data[4]
            #     nam = fn + " " + ln
            #
            # except Exception as es:
            #     messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.window)
            # con.commit()
            # con.close()
            #
            # self.name = nam
            Id = ""
            name = ""
            ft = open("ld.txt", "r")
            a, b = ft.read().split(",")
            ft.close()
            nam = ""
            Id = a
            # print(a)
            print(Id)
            try:
                con = mysql.connector.connect(host="localhost", username="root", password="Aman", database="login_d")
                my_c = con.cursor()
                my_c.execute("select * from login where Username=%s and Type=%s", (a, b))
                data = my_c.fetchone()
                fn = data[3]
                ln = data[4]
                nam = fn + " " + ln

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.window)

            name = nam
            if ((name.isalpha()) or (' ' in name)):

                # cam modl

                cam = cv2.VideoCapture(0)
                harcascadePath = "haar_face.xml"
                detector = cv2.CascadeClassifier(harcascadePath)
                sampleNum = 0
                while (True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        # incrementing sample number
                        sampleNum = sampleNum + 1
                        # saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite(
                            "TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                            gray[y:y + h, x:x + w])
                        # display the frame
                        cv2.imshow('Taking Images', img)
                    # wait for 100 miliseconds
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    # break if the sample number is morethan 100
                    elif sampleNum > 100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                res = "Images Taken for ID : " + Id
                row = [serial, '', Id, '', name]
                with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                print(res)
            else:
                if (name.isalpha() == False):
                    res = "Enter Correct name"
                    print(res)

            print("module new starting.......")

            def check_haarcascadefile():
                exists = os.path.isfile("haar_face.xml")
                if exists:
                    pass
                else:
                    print("haar_cascade file missing")

            def assure_path_exists(path):
                dir = os.path.dirname(path)
                if not os.path.exists(dir):
                    os.makedirs(dir)

            def getImagesAndLabels(path):
                # get the path of all the files in the folder
                imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
                # create empth face list
                faces = []
                # create empty ID list
                Ids = []
                # now looping through all the image paths and loading the Ids and the images
                for imagePath in imagePaths:
                    # loading the image and converting it to gray scale
                    pilImage = Image.open(imagePath).convert('L')
                    # Now we are converting the PIL image into numpy array
                    imageNp = np.array(pilImage, 'uint8')
                    # getting the Id from the image
                    ID = int(os.path.split(imagePath)[-1].split(".")[1])
                    # extract the face from the training image sample
                    faces.append(imageNp)
                    Ids.append(ID)
                return faces, Ids

            def TrainImages():
                check_haarcascadefile()
                assure_path_exists("TrainingImageLabel/")
                recognizer = cv2.face_LBPHFaceRecognizer.create()
                harcascadePath = "haar_face.xml"
                detector = cv2.CascadeClassifier(harcascadePath)
                faces, ID = getImagesAndLabels("TrainingImage")
                try:
                    recognizer.train(faces, np.array(ID))
                except:
                    print("Please Register first........")
                    return
                recognizer.save("TrainingImageLabel\Trainner.yml")
                res = "Profile Saved Successfully"
                print(res)
                print('Total Registrations till now  : ' + str(ID[0]))

            check_haarcascadefile()
            assure_path_exists("TrainingImageLabel/")
            recognizer = cv2.face_LBPHFaceRecognizer.create()
            harcascadePath = "haar_face.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            faces, ID = getImagesAndLabels("TrainingImage")
            try:
                recognizer.train(faces, np.array(ID))
            except:
                print("Please Register first........")
            recognizer.save("TrainingImageLabel\Trainner.yml")
            res = "Profile Saved Successfully"
            print(res)
            print('Total Registrations till now  : ' + str(ID[0]))


        def btn_clicked1():
            print("Attendence Data")
            window.destroy()
            win = Tk()
            pa.page(win)

            # f = open("ld.txt","r")
            # dta,roll = f.read().split(",")
            # f.close()
            # try:
            #     conn = mysql.connector.connect(host="localhost", username="root", password="Aman", database="login_d")
            #     my_c = conn.cursor()
            #     my_c.execute("select * from stu_data where Username=%s and Type=%s",(dta,roll))
            #     data=my_c.fetchall()
            #     print(data)

            # except Exception as es:
            #     messagebox.showerror("Error", f"Due to :{str(es)}",parent=window)

        def btn_clicked2():
            print("Logout")
            window.destroy()
            # import Login_page
            win=Tk()
            lg.Login_page(win)


        window.geometry("1240x640")
        window.configure(bg="#ffffff")
        canvas = Canvas(
            window,
            bg="#ffffff",
            height=640,
            width=1240,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"pic\SDbackground.png")
        background = canvas.create_image(
            595.0, 229.5,
            image=background_img)

        img0 = PhotoImage(file=f"pic\SDimg0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked0,
            relief="flat")

        b0.place(
            x=150, y=435,
            width=370,
            height=44)

        img1 = PhotoImage(file=f"pic\SDimg1.png")
        b1 = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked1,
            relief="flat")

        b1.place(
            x=677, y=435,
            width=370,
            height=44)

        img2 = PhotoImage(file=f"pic\SDimg2.png")
        b2 = Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked2,
            relief="flat")

        b2.place(
            x=1100, y=22,
            width=121,
            height=38)

        window.resizable(False, False)
        window.mainloop()



#         =================== genrate photo st============================

        # f_c=cv.CascadeClassifier("haarcascade_frontalface_default")
        # def ima():


# Stud=Tk()
# obj=Students(Stud)
# Stud.mainloop()

if __name__ == '__main__':
    window = Tk()
    obj = Students(window)
    window.mainloop()

