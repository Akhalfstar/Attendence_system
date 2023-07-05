from tkinter import *
import cv2,os
import pandas as pd
import time
import datetime
import csv
import collections

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import time
import Login_page as lg
from tkcalendar import *
import register as rg
import Student_d as sd
import forg as fg
import Teacher as Te
import page as pa
import T_reg as tr

class s_reg:
    def __init__(self,window):
        self.window = window
        self.window.title("Team EXPO Teacher Registration")
        def Gologin():
            print("Go login")
            self.window.destroy()
            # import Login_page
            win=Tk()
            lg.Login_page(win)

        # ============variables====================




        # ============variables====================

        def Reg():
            print(perADD.get())
            print(fname.get())
            print(S_id.get())
            print(pin.get())
            print(pro.get())
            print(RN.get())
            print(phone.get())
            print(Email.get())
            print(Pword.get())
            print(School.get())
            print(Gaurdian.get())
            print(Lname.get())
            print(DOB.get())
            print(Gender.get())
            if fname.get() == "" or pro.get() == "" or S_id.get()=="" or Lname.get() ==""  or  phone.get()=="" or RN.get()=="" or perADD.get()=="" or Email.get()=="" or Pword.get()=="" or School.get()=="" or Gaurdian.get()=="" or pin.get()=="" or DOB.get()=="" or Gender.get()=="":
                messagebox.showerror("Error","All feilds are must",parent=self.window)
            #elif cb.get()=="Select Role":
            #    messagebox.showinfo("Select Role", "Please select valid Role")
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Aman",database="login_d")
                    my_c = conn.cursor()
                    fullN=fname.get()+" "+Lname.get()
                    tb = time.ctime(time.time())
                    a, b, c, d, e = tb.split()
                    ls = [a, b, c, d, e]
                    print(ls)
                    f = b + e
                    f = f.lower()
                    my_c.execute(f"insert into {f} (Username,Name,Rollno,Type) values(%s,%s,%s,%s)",( Email.get(),fullN,RN.get(),"Student"))
                    my_c.execute("insert into login values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            Email.get(),
                            Pword.get(),
                            "Student",
                            fname.get(),
                            Lname.get(),
                            School.get(),
                            RN.get(),
                            DOB.get(),
                            Gaurdian.get(),
                            phone.get(),
                            Gender.get(),
                            S_id.get(),
                            pro.get(),
                            perADD.get(),
                            pin.get()
                            
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","You have been Registered Successfully",parent=self.window)
                    self.window.destroy()
                    win=Tk()
                    # import Login_page
                    lg.Login_page(win)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.window)



        def btn_clicked():
            print("Button Clicked")
            self.window.destroy()
            # import Login_page
            win = Tk()
            tr.Treg(win)

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

        background_img = PhotoImage(file = f"pic\SRbackground.png")
        background = canvas.create_image(
            625.0, 310.0,
            image=background_img)
        
        entry1_img = PhotoImage(file = f"pic\SRimg_textBox1.png")
        entry1_bg = canvas.create_image(
            359.0, 163.5,
            image = entry1_img)

        fname = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        fname.place(
            x = 297.0, y = 151,
            width = 124.0,
            height = 23)
        
        entry11_img = PhotoImage(file = f"pic\SRimg_textBox11.png")
        entry11_bg = canvas.create_image(
            503.0, 163.5,
            image = entry11_img)

        Lname = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        Lname.place(
            x = 441.0, y = 151,
            width = 124.0,
            height = 23)

        entry0_img = PhotoImage(file = f"pic\SRimg_textBox0.png")
        entry0_bg = canvas.create_image(
            789.0, 337.0,
            image = entry0_img)
        
        entry7_img = PhotoImage(file = f"pic\SRimg_textBox7.png")
        entry7_bg = canvas.create_image(
            431.0, 223.0,
            image = entry7_img)

        Email = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        Email.place(
            x = 297.0, y = 208,
            width = 268.0,
            height = 28)
        
        entry8_img = PhotoImage(file = f"pic\SRimg_textBox8.png")
        entry8_bg = canvas.create_image(
            431.0, 277.5,
            image = entry8_img)

        Pword = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        Pword.place(
            x = 297.0, y = 265,
            width = 268.0,
            height = 23)
        
        School = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        School.place(
            x = 297.0, y = 323,
            width = 268.0,
            height = 23)
        
        RN = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        RN.place(
            x = 297.0, y = 380,
            width = 124.0,
            height = 23)
        
        DOB = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        DOB.place(
            x = 441.0, y = 380,
            width = 124.0,
            height = 23)
        
        Gaurdian = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        Gaurdian.place(
            x = 655.0, y = 151,
            width = 268.0,
            height = 23)
        
        phone = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        phone.place(
            x = 655.0, y = 209,
            width = 124.0,
            height = 23)
        
        Gender = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        Gender.place(
            x = 801.0, y = 209,
            width = 124.0,
            height = 23)
        
        S_id = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        S_id.place(
            x = 655.0, y = 265,
            width = 124.0,
            height = 23)
        
        pro = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        pro.place(
            x = 799.0, y = 265,
            width = 124.0,
            height = 23)

        perADD = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        perADD.place(
            x = 655.0, y = 322,
            width = 268.0,
            height = 28)

        

        entry2_img = PhotoImage(file = f"pic\SRimg_textBox2.png")
        entry2_bg = canvas.create_image(
            717.0, 277.5,
            image = entry2_img)


        entry3_img = PhotoImage(file = f"pic\SRimg_textBox3.png")
        entry3_bg = canvas.create_image(
            717.0, 391.5,
            image = entry3_img)

        pin = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        pin.place(
            x = 655.0, y = 379,
            width = 124.0,
            height = 23)

        entry4_img = PhotoImage(file = f"pic\SRimg_textBox4.png")
        entry4_bg = canvas.create_image(
            861.0, 277.5,
            image = entry4_img)

        entry5_img = PhotoImage(file = f"pic\SRimg_textBox5.png")
        entry5_bg = canvas.create_image(
            359.0, 392.5,
            image = entry5_img)

        entry6_img = PhotoImage(file = f"pic\SRimg_textBox6.png")
        entry6_bg = canvas.create_image(
            717.0, 221.5,
            image = entry6_img)

        entry9_img = PhotoImage(file = f"pic\SRimg_textBox9.png")
        entry9_bg = canvas.create_image(
            431.0, 335.5,
            image = entry9_img)


        entry10_img = PhotoImage(file = f"pic\SRimg_textBox10.png")
        entry10_bg = canvas.create_image(
            789.0, 163.5,
            image = entry10_img)

        entry12_img = PhotoImage(file = f"pic\SRimg_textBox12.png")
        entry12_bg = canvas.create_image(
            503.0, 392.5,
            image = entry12_img)

        entry13_img = PhotoImage(file = f"pic\SRimg_textBox13.png")
        entry13_bg = canvas.create_image(
            863.0, 221.5,
            image = entry13_img)

        img0 = PhotoImage(file = f"pic\SRimg0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Gologin,
            relief = "flat")

        b0.place(
            x = 1018, y = 600,
            width = 155,
            height = 23)

        img1 = PhotoImage(file = f"pic\SRimg1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b1.place(
            x = 57, y = 600,
            width = 210,
            height = 26)

        img2 = PhotoImage(file = f"pic\SRimg2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = Reg,
            relief = "flat")

        b2.place(
            x = 563, y = 445,
            width = 163,
            height = 31)

        window.resizable(False, False)
        window.mainloop()

if __name__ == '__main__':
    window = Tk()
    obj = s_reg(window)
    window.mainloop()
