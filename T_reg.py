from tkinter import *
from tkinter import ttk
from PIL import Image
import csv
from tkinter import messagebox
import mysql.connector
import time
import Login_page as lg
import Teacher
import register as rg
import Student_d as sd
import forg as fg
import Teacher as Te
import page as pa


# login

class Treg:
    def __init__(self,window):
        self.window = window
        self.window.title("Team EXPO Teacher Registration")

        def btn_clicked():
            self.window.destroy()
            # import Login_page
            win = Tk()
            lg.Login_page(win)



        # student

        def btn_clicked1():
            print("Button Clicked1")
            self.window.destroy()
            # import Login_page
            win = Tk()
            rg.s_reg(win)

        # register
        def btn_3():
            print(entry0.get())
            print(entry1.get())
            print(entry2.get())
            print(entry3.get())
            print(entry4.get())
            print(entry5.get())
            print(entry6.get())
            print(entry7.get())
            print(entry8.get())
            print(entry9.get())
        def btn_clicked2():
            print("Button Clicked2")
            if entry0.get() == "" or entry1.get()=="" or entry2.get() ==""  or  entry3.get()=="" or entry4.get()=="" or entry5.get()=="" or entry6.get()=="" or entry7.get()=="" or entry8.get()=="" or entry9.get()=="" or entry10.get()=="" :
                messagebox.showerror("Error","All feilds are must",parent=window)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Aman",database="login_d")
                    my_c = conn.cursor()
                    fullN=entry1.get()+" "+entry8.get()
                    tb = time.ctime(time.time())
                    a, b, c, d, e = tb.split()
                    ls = [a, b, c, d, e]
                    print(ls)
                    f = b + e
                    f = f.lower()
                    my_c.execute(f"insert into {f} (Username,Name,Rollno,Type) values(%s,%s,%s,%s)",( entry5.get(),fullN,"","Administrator"))
                    my_c.execute("insert into login values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            entry5.get(),
                            entry6.get(),
                            "Administrator",
                            entry1.get(),
                            entry8.get(),
                            "",
                            # roll.get(),
                            entry4.get(),
                            entry7.get(),
                            entry10.get(),
                            "",
                            # Gaurdian.get(),
                            entry9.get(),
                            entry0.get(),
                            entry3.get(),
                            entry2.get(),
                            ""
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



        def correct(inp):
            if inp.isdigit():
                return True
            elif inp == "":
                return True
            else:
                return False
        re=window.register(correct)


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

        background_img = PhotoImage(file = f"TRbackground.png")
        background = canvas.create_image(
            630.0, 309.0,
            image=background_img)

        entry0_img = PhotoImage(file = f"TRimg_textBox0.png")
        entry0_bg = canvas.create_image(
            781.0, 226.0,
            image = entry0_img)

        # permanenrt adress
        entry0 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry0.place(
            x = 647.0, y = 211,
            width = 268.0,
            height = 28)

        # first namwe

        entry1_img = PhotoImage(file = f"TRimg_textBox1.png")
        entry1_bg = canvas.create_image(
            364.0, 162.5,
            image = entry1_img)

        entry1 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry1.place(
            x = 302.0, y = 150,
            width = 124.0,
            height = 23)

        # teacher

        entry2_img = PhotoImage(file = f"TRimg_textBox2.png")
        entry2_bg = canvas.create_image(
            364.0, 391.5,
            image = entry2_img)

        entry2 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry2.place(
            x = 302.0, y = 379,
            width = 124.0,
            height = 23)

        # pin

        entry3_img = PhotoImage(file = f"TRimg_textBox3.png")
        entry3_bg = canvas.create_image(
            709.0, 280.5,
            image = entry3_img)

        entry3 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry3.place(
            x = 647.0, y = 268,
            width = 124.0,
            height = 23)
        entry3.config(validate="key", validatecommand=(re, "%P"))

        # phone number

        entry4_img = PhotoImage(file = f"TRimg_textBox4.png")
        entry4_bg = canvas.create_image(
            709.0, 163.5,
            image = entry4_img)

        entry4 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry4.place(
            x = 647.0, y = 151,
            width = 124.0,
            height = 23)
        entry4.config(validate="key", validatecommand=(re, "%P"))

        # email

        entry5_img = PhotoImage(file = f"TRimg_textBox5.png")
        entry5_bg = canvas.create_image(
            436.0, 222.0,
            image = entry5_img)

        entry5 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry5.place(
            x = 302.0, y = 207,
            width = 268.0,
            height = 28)

        # pass

        entry6_img = PhotoImage(file = f"TRimg_textBox6.png")
        entry6_bg = canvas.create_image(
            436.0, 276.5,
            image = entry6_img)

        entry6 = Entry(
            bd = 0,
            bg = "#ffffff",
            show='*',
            highlightthickness = 0)

        entry6.place(
            x = 302.0, y = 264,
            width = 268.0,
            height = 23)

        # school

        entry7_img = PhotoImage(file = f"TRimg_textBox7.png")
        entry7_bg = canvas.create_image(
            436.0, 334.5,
            image = entry7_img)

        entry7 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry7.place(
            x = 302.0, y = 322,
            width = 268.0,
            height = 23)


        # last name

        entry8_img = PhotoImage(file = f"TRimg_textBox8.png")
        entry8_bg = canvas.create_image(
            508.0, 162.5,
            image = entry8_img)

        entry8 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry8.place(
            x = 446.0, y = 150,
            width = 124.0,
            height = 23)

        # dob

        entry9_img = PhotoImage(file = f"TRimg_textBox9.png")
        entry9_bg = canvas.create_image(
            508.0, 391.5,
            image = entry9_img)

        entry9 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry9.place(
            x = 446.0, y = 379,
            width = 124.0,
            height = 23)

        # Gender

        entry10_img = PhotoImage(file = f"TRimg_textBox10.png")
        entry10_bg = canvas.create_image(
            855.0, 163.5,
            image = entry10_img)

        entry10 = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        entry10.place(
            x = 793.0, y = 151,
            width = 124.0,
            height = 23)

        img0 = PhotoImage(file = f"TRimg0.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b0.place(
            x = 1023, y = 599,
            width = 155,
            height = 23)

        img1 = PhotoImage(file = f"TRimg1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked1,
            relief = "flat")

        b1.place(
            x = 73, y = 599,
            width = 199,
            height = 23)

        img2 = PhotoImage(file = f"TRimg2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked2,
            relief = "flat")

        b2.place(
            x = 545, y = 468,
            width = 262,
            height = 50)

        window.resizable(False, False)
        window.mainloop()

if __name__ == '__main__':
    window = Tk()
    obj = Treg(window)
    window.mainloop()