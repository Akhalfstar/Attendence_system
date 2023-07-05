from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import Login_page as lg
import register as rg
import Student_d as sd
import forg as fg
import Teacher as Te
import page as pa
import math
import random
import smtplib


class Forget:
    def __init__(self,window):
        def btn_clicked():

            if entry0.get()=="" or entry1.get()=="" or entry2.get()=="":
                messagebox.showinfo("Invalid","Please enter all details")
            elif entry1.get() != entry2.get():
                messagebox.showwarning("Invalid","Password do not matchimg")
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aman",database="login_d")
                    my_c = conn.cursor()
                    my_c.execute("UPDATE login SET Password=%s where Username=%s",(entry1.get(),entry0.get()))
                    my_c.execute("select * from login where Username=%s and Password=%s",(entry0.get(),entry1.get()))
                    data = my_c.fetchone()
                    # print(f"{data}")
                    if data == None:
                        messagebox.showerror("Error","Username Not found",parent=window)
                        conn.commit()
                        conn.close()
                    else:
                        messagebox.showinfo("Log","Password changed Successefully")
                        conn.commit()
                        conn.close()
                        window.destroy()
                        # import Login_page
                        win=Tk()
                        lg.Login_page(win)

                except Exception as es:
                    messagebox.showerror("Error", f"Due to :{str(es)}", parent=window)

        def btn_clicked1():
            window.destroy()
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

        background_img = PhotoImage(file=f"pic\Fforget.png")
        background = canvas.create_image(
            614.5, 319.5,
            image=background_img)

        img0 = PhotoImage(file=f"pic\Ffimg0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        b0.place(
            x=697, y=449,
            width=416,
            height=35)

        entry0_img = PhotoImage(file=f"pic\Ffimg_textBox0.png")
        entry0_bg = canvas.create_image(
            881.5, 201.5,
            image=entry0_img)

        def on_enterU(e):
            entry0.delete(0,"end")

        def on_leaveU(e):
            name=entry0.get()
            if name=="":
                entry0.insert(0,"Username")

        img01 = PhotoImage(file=f"pic/Fimg0.png")
        b1 = Button(
            image=img01,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked1,
            relief="flat")

        b1.place(
            x=58, y=38,
            width=81,
            height=30)


        entry0 = Entry(
            bd=0,
            bg="#ffffff",
            font=("inter", 20),
            highlightthickness=0)
        entry0.insert(0,"Username")
        entry0.bind("<FocusIn>",on_enterU)
        entry0.bind("<FocusOut>",on_leaveU)

        entry0.place(
            x=708, y=179,
            width=337,
            height=43)

        entry1_img = PhotoImage(file=f"pic\Ffimg_textBox1.png")
        entry1_bg = canvas.create_image(
            876.5, 260.5,
            image=entry1_img)

        def on_enter1(e):
            entry1.delete(0,"end")

        def on_leave1(e):
            name=entry1.get()
            if name=="":
                entry0.insert(0,"Username")

        entry1 = Entry(
            bd=0,
            bg="#ffffff",
            font=("inter", 20),
            highlightthickness=0)
        entry1.insert(0, "Password")
        entry1.bind("<FocusIn>", on_enter1)
        entry1.bind("<FocusOut>", on_leave1)

        entry1.place(
            x=708, y=257,
            width=337,
            height=43)

        entry2_img = PhotoImage(file=f"pic\Ffimg_textBox2.png")
        entry2_bg = canvas.create_image(
            876.5, 349.5,
            image=entry2_img)


        def on_enter2(e):
            entry2.delete(0,"end")

        def on_leave2(e):
            name=entry2.get()
            if name=="":
                entry2.insert(0,"Conform pass")

        entry2 = Entry(
            bd=0,
            bg="#ffffff",
            font=("inter", 20),
            highlightthickness=0)
        entry2.insert(0, "Conform Pass")
        entry2.bind("<FocusIn>", on_enter2)
        entry2.bind("<FocusOut>", on_leave2)

        entry2.place(
            x=708, y=327,
            width=337,
            height=43)

# ============================OTP system===================


        # def btn_clicked3():
        #     digits = "0123456789"
        #     OTP = ""
        #     for i in range(6):
        #         OTP += digits[math.floor(random.random() * 10)]
        #     otp = OTP + " is your OTP"
        #     msg = otp
        #     s = smtplib.SMTP('smtp.gmail.com', 587)
        #     s.starttls()
        #     s.login("exposmarty@gmail.com", "sbwspqydixwzjozm")
        #     emailid = entry0.get()
        #     s.sendmail("exposmarty@gmail.com", emailid, msg)
        #     a = input("Enter Your OTP >>: ")
        #     if a == OTP:
        #         print("Verified")
        #     else:
        #         print("Please Check your OTP again")
        #
        # img0a = PhotoImage(file=f"pic/F1img0.png")
        # b3 = Button(
        #     image=img0a,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=btn_clicked3,
        #     relief="flat")
        #
        # b3.place(
        #     x=1014, y=196,
        #     width=111,
        #     height=27)

 # ============================OTP system===================

        window.resizable(False, False)
        window.mainloop()

# forget=Tk()
# obj=Forget(forget)
# forget.mainloop()

if __name__ == '__main__':
    window = Tk()
    obj = Forget(window)
    window.mainloop()