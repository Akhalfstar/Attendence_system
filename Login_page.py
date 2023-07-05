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



class Login_page:

# ============Register button===========

    def Reg_w(self):
        self.window.destroy()
        # import register
        win1=Tk()
        rg.s_reg(win1)

# ============Register button===========

    def __init__(self, window):
        self.window = window
        self.window.title("Team EXPO Login")
        li = ["Select Role","Student", "Parent", "Administrator"]

        # ============variables====================

        self.entry0 = StringVar()
        self.entry1 = StringVar()

        # ============variables====================

        # ===========Login button============

        def btn_clicked_login():
            ft = open("td.txt","r")
            tabN= ft.read()
            ft.close()
            tb = time.ctime(time.time())
            a, b, c, d, e = tb.split()
            ls = [a, b, c, d, e]
            f = b + e
            f = f.lower()
            print(tabN)
            print(f)
            if tabN != f:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aman", database="login_d")
                    my = conn.cursor()
                    my.execute(f"create table {f} (Username VARCHAR(100) PRIMARY KEY, Name VARCHAR(100),Rollno VARCHAR(45),Type VARCHAR(45))")
                    for i in range(1, 32):
                        j = str(i)
                        j = "Day" + j
                        ls=("H")
                        my.execute(f"ALTER TABLE {f} ADD {j} VARCHAR(45)")
                    conn.commit()
                    conn.close()
                    ft = open("td.txt", "w")
                    ft.write(f"{f}")
                    ft.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Error due to {str(es)}")
            else:
                pass

            if entry0.get()=="" or entry1.get()=="":
                messagebox.showerror("Error","Fill Username and Password both",parent=self.window)
            elif cb.get()=="Select Role":
                messagebox.showinfo("Select Role", "Please select valid Role")
            else:
                try:
                    con= mysql.connector.connect(host="localhost",username="root",password="Aman",database="login_d")
                    my_c=con.cursor()
                    my_c.execute("select * from login where Username=%s and Password=%s and Type=%s",(entry0.get(),entry1.get(),cb.get()))
                    data=my_c.fetchone()
                    # print(entry0.get())
                    # print(data)
                    if data == None:
                        messagebox.showerror("Error","Invalid Username, Password or Role",parent=self.window)
                    else:
                        f = open("ld.txt", "w")
                        f.write(f"{entry0.get()},{cb.get()}")
                        f.close()
                        if cb.get()=="Administrator":
                            window.destroy()
                            # import Teacher
                            win = Tk()
                            Te.Teacher(win)
                        else:
                            window.destroy()
                            # import Student_d
                            win=Tk()
                            sd.Students(win)
                        # messagebox.showinfo("Log","Logged in Sucessesfully")
                    con.commit()
                    con.close()

                except Exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.window)

        # ===========Login button============


        # ===========Forget password button===========

        def Forget():
            self.window.destroy()
            # import forg
            win=Tk()
            fg.Forget(win)

        self.window.geometry("1366x768")
        self.window.configure(bg="#ffffff")
        canvas = Canvas(
            self.window,
            bg="#ffffff",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"pic\Lbackground.png")
        background = canvas.create_image(
            680.5, 384.0,
            image=background_img)



        entry0_img = PhotoImage(file=f"pic\Limg_textBox0.png")
        entry0_bg = canvas.create_image(
            1013.0, 361.5,
            image=entry0_img)
        entry0 = Entry(self.window,
                       font=("inner_black", 12),
            bd=0,
            bg="#d6e8ed",
            highlightthickness=0)
        entry0.place(
            x=891.5, y=339,
            width=243.0,
            height=43)



        entry1_img = PhotoImage(file=f"pic\Limg_textBox1.png")
        entry1_bg = canvas.create_image(
            1013.0, 457.5,
            image=entry1_img)
        entry1 = Entry(self.window,
                       font=("inner_black", 12),
            bd=0,
            bg="#d6e8ed",
            show='*',
            highlightthickness=0)
        entry1.place(
            x=891.5, y=435,
            width=243.0,
            height=43)
        img1 = PhotoImage(file=f"pic\Limg1.png")
        b1 = Button(window,
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=Forget,
            relief="flat")
        b1.place(
            x=1070, y=482,
            width=69,
            height=14)

        img2 = PhotoImage(file=f"pic\Limg2.png")
        b2 = Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.Reg_w,
            relief="flat")

        b2.place(
            x=1043, y=384,
            width=110,
            height=17)

        img0 = PhotoImage(file=f"pic\Limg0.png")
        b0 = Button(window,
                    image=img0,
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_clicked_login,
                    relief="flat")

        b0.place(
            x=858, y=563,
            width=120,
            height=45)

        cb = ttk.Combobox(self.window,font = ("inner_black", 12), value=li, width=20, height=0,state="readonly")
        cb.current(0)
        cb.place(
            x=870.5, y=520
        )

        self.window.resizable(False, False)
        self.window.mainloop()




if __name__ == '__main__':
    window = Tk()
    obj = Login_page(window)
    window.mainloop()
# window = Tk()
# obj= Login_page(window)
# window.mainloop()

