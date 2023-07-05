from tkinter import *
from tkinter import *
import cv2,os
import pandas as pd
import time
import datetime
import csv
import collections
import page2 as pa2
from tkinter import ttk
from PIL import Image
from tkinter import messagebox
import mysql.connector
import time
import os
import pandas as pd
import datetime
import Login_page as lg
import register as rg
import Student_d as sd
import forg as fg
import Teacher as Te
import page as pa
import cv2
import cv2,os
import numpy as np
from PIL import Image
import pandas as pd
import time
import datetime

class Teacher:
    def __init__(self,window):
        def btn_clicked4():
            print("Start Addendance")

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

            periods = 1
            n = 1

            check_haarcascadefile()
            assure_path_exists("Attendance/")
            assure_path_exists("StudentDetails/")

            recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
            exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
            if exists3:
                recognizer.read("TrainingImageLabel\Trainner.yml")
            else:
                print('Please click on Save Profile to reset data!!')
            harcascadePath = "haar_face.xml"
            faceCascade = cv2.CascadeClassifier(harcascadePath);

            for i in range(periods):
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
                exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
                if exists1:
                    df = pd.read_csv("StudentDetails\StudentDetails.csv")
                else:
                    print('Students details are missing, please check!')
                    cam.release()
                    cv2.destroyAllWindows()
                alias = []

                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                        serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if (conf < 50):
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%B-%Y')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

                            aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                            ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                            ID = str(ID)
                            ID = ID[1:-1]
                            temp = ID
                            bb = str(aa)
                            bb = bb[2:-2]
                            attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%B-%Y')
                            exists = os.path.isfile("Attendance\Attendance_" + date + f" Period {i + 1}" + ".csv")
                            if ID not in alias:
                                if exists:
                                    with open("Attendance\Attendance_" + date + f" Period {i + 1}" + ".csv",
                                              'a+') as csvFile1:
                                        writer = csv.writer(csvFile1)
                                        writer.writerow(attendance)
                                    csvFile1.close()
                                else:
                                    with open("Attendance\Attendance_" + date + f" Period {i + 1}" + ".csv",
                                              'a+') as csvFile1:
                                        writer = csv.writer(csvFile1)
                                        writer.writerow(col_names)
                                        writer.writerow(attendance)
                                    csvFile1.close()

                                alias.append(ID)


                        else:
                            Id = 'Unknown'
                            bb = str(Id)
                        cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
                    cv2.imshow('Taking Attendance', im)
                    if (cv2.waitKey(1) == ord('q')):
                        break

            l1 = os.listdir("Attendance")
            roll_no_list = []
            name_list = []
            name_present = []
            roll_present = []

            for l2 in l1:
                df = pd.read_csv("Attendance/" + l2)
                for id in df["Id"].unique():
                    roll_no_list.append(id)

                for name in df["Name"].unique():
                    name_list.append(name)

            name_freq = collections.Counter(name_list)
            roll_no_freq = collections.Counter(roll_no_list)

            for name in name_freq:
                if name_freq[name] >= n:
                    name_present.append(name)

            for roll in roll_no_freq:
                if roll_no_freq[roll] >= n:
                    roll_present.append(roll)

            l = len(name_present)
            tb = time.ctime(time.time())
            a, b, c, d, e = tb.split()
            ls = [a, b, c, d, e]
            f = b + e
            f = f.lower()
            var = "Day" + c
            roll=""
            name=""
            for i in range(0, l):
                Name = name_present[i]
                roll = roll_present[i]
                roll = roll[1:-1]
                print(roll)
                print(Name)
                try:
                    con = mysql.connector.connect(host="localhost", username="root", password="Aman",database="login_d")
                    my_c = con.cursor()
                    my_c.execute(f"update {f} set {var} =%s where Username=%s and Name=%s", ("P", roll, Name))
                    con.commit()
                    con.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)}", parent=window)

            print(name_present)
            print(roll_present)


        def btn_clicked():
            print("Button Clicked")

        def btn_clicked1():
            print("Button Clicked1")
            print("Show Attendence data")
            window.destroy()
            win = Tk()
            pa2.page(win)


        def btn_clicked2():
            print("Button Clicked2")
            print("Show Attendence data")
            window.destroy()
            win = Tk()
            pa.page(win)

            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Aman", database="login_d")
                my = conn.cursor()
                tb = time.ctime(time.time())
                a, b, c, d, e = tb.split()
                ls = [a, b, c, d, e]
                f = b + e
                f = f.lower()

                my.execute(f"select * from {f}")
                da = my.fetchall()
                print(da)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=window)

        def btn_clicked3():
            print("Button Clicked3")
            print("Start Addendance")

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

            periods = 1
            n = 1

            check_haarcascadefile()
            assure_path_exists("Attendance/")
            assure_path_exists("StudentDetails/")

            recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
            exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
            if exists3:
                recognizer.read("TrainingImageLabel\Trainner.yml")
            else:
                print('Please click on Save Profile to reset data!!')
            harcascadePath = "haar_face.xml"
            faceCascade = cv2.CascadeClassifier(harcascadePath);

            for i in range(periods):
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
                exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
                if exists1:
                    df = pd.read_csv("StudentDetails\StudentDetails.csv")
                else:
                    print('Students details are missing, please check!')
                    cam.release()
                    cv2.destroyAllWindows()
                alias = []

                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                        serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if (conf < 50):
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%B-%Y')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

                            aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                            ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                            ID = str(ID)
                            ID = ID[1:-1]
                            temp = ID
                            bb = str(aa)
                            bb = bb[2:-2]
                            attendance = [str(ID), '', bb, '', str(date), '', str(timeStamp)]
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%B-%Y')
                            exists = os.path.isfile("Attendance\Attendance_" + date + f" Period {i + 1}" + ".csv")
                            if ID not in alias:
                                if exists:
                                    with open("Attendance\Attendance_" + date + f" Period {i + 1}" + ".csv",
                                              'a+') as csvFile1:
                                        writer = csv.writer(csvFile1)
                                        writer.writerow(attendance)
                                    csvFile1.close()
                                else:
                                    with open("Attendance\Attendance_" + date + f" Period {i + 1}" + ".csv",
                                              'a+') as csvFile1:
                                        writer = csv.writer(csvFile1)
                                        writer.writerow(col_names)
                                        writer.writerow(attendance)
                                    csvFile1.close()

                                alias.append(ID)


                        else:
                            Id = 'Unknown'
                            bb = str(Id)
                        cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
                    cv2.imshow('Taking Attendance', im)
                    if (cv2.waitKey(1) == ord('q')):
                        break

            l1 = os.listdir("Attendance")
            roll_no_list = []
            name_list = []
            name_present = []
            roll_present = []

            for l2 in l1:
                df = pd.read_csv("Attendance/" + l2)
                for id in df["Id"].unique():
                    roll_no_list.append(id)

                for name in df["Name"].unique():
                    name_list.append(name)

            name_freq = collections.Counter(name_list)
            roll_no_freq = collections.Counter(roll_no_list)

            for name in name_freq:
                if name_freq[name] >= n:
                    name_present.append(name)

            for roll in roll_no_freq:
                if roll_no_freq[roll] >= n:
                    roll = roll[1:-1]
                    roll_present.append(roll)


            l=len(name_present)
            tb = time.ctime(time.time())
            a, b, c, d, e = tb.split()
            ls = [a, b, c, d, e]
            f = b + e
            f = f.lower()
            var="Days"+c
            for i in range(0,l):
                Name=name_present[i]
                roll=roll_present[i]
                try:
                    con= mysql.connector.connect(host="localhost",username="root",password="Aman",database="login_d")
                    my_c=con.cursor()
                    # my_c.execute(f"select * from {f} where Username=%s and Name=%s",(roll,Name))
                    # data = my_c.fetchone()
                    # if data != n:
                    ft = open("ttd.txt", "r")
                    da = ft.read()
                    ft.close()
                    if da != "meal":
                        my_c.execute(
                            f"create table if not exists meal(Username VARCHAR(100) PRIMARY KEY, Name VARCHAR(100),Rollno VARCHAR(45),Type VARCHAR(45))")
                        for i in range(1, 32):
                            j = str(i)
                            j = "Days" + j
                            ls = ("H")
                            my_c.execute(f"ALTER TABLE meal ADD {j} VARCHAR(45)")
                        ft = open("ttd.txt", "w")
                        ft.write(f"meal")
                        ft.close()
                    else:
                        pass
                    con.commit()
                    con.close()
                    con = mysql.connector.connect(host="localhost", username="root", password="Aman",database="login_d")
                    my_c = con.cursor()
                    my_c.execute(f"update meal set {var} =%s where Username=%s and Name=%s",("P",roll,Name))
                    con.commit()
                    con.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=window)



            print(name_present)
            print(roll_present)

        # def btn_clicked4():
        #     print("Button Clicked4")

        def btn_clicked5():
            print("Button Clicked5")
            window.destroy()
            win = Tk()
            lg.Login_page(win)


        window.geometry("1240x640")
        window.configure(bg = "#ffffff")
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 640,
            width = 1240,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"pic\Tbackground.png")
        background = canvas.create_image(
            635.5, 202.5,
            image=background_img)


        btn = Button(window, text = 'Show Applications',command = btn_clicked)
        btn.place( x = 220, y = 535,
            width = 200,
            height = 44)

        btn1 = Button(window, text = 'Start Distribution',command = btn_clicked)
        btn1.place( x = 720, y = 535,
            width = 200,
            height = 44)

        img1 = PhotoImage(file = f"pic\Timg1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked1,
            relief = "flat")

        b1.place(
            x = 1020, y = 336,
            width = 166,
            height = 46)

        img2 = PhotoImage(file = f"pic\Timg2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked2,
            relief = "flat")

        b2.place(
            x = 707, y = 337,
            width = 171,
            height = 45)

        img3 = PhotoImage(file = f"pic\Timg3.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked3,
            relief = "flat")

        b3.place(
            x = 390, y = 335,
            width = 159,
            height = 44)

        img4 = PhotoImage(file = f"pic\Timg4.png")
        b4 = Button(
            image = img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked4,
            relief = "flat")

        b4.place(
            x = 99, y = 336,
            width = 146,
            height = 42)

        img5 = PhotoImage(file = f"pic\Timg5.png")
        b5 = Button(
            image = img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked5,
            relief = "flat")

        b5.place(
            x = 1067, y = 22,
            width = 116,
            height = 39)

        window.resizable(False, False)
        window.mainloop()

if __name__ == '__main__':
    window = Tk()
    obj = Teacher(window)
    window.mainloop()
