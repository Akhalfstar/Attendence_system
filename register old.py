import tkinter
from tkinter import *
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

class register_page:
    def __init__(self, Rpage):
        self.Rpage=Rpage
        self.Rpage.title("Team EXPO Registration")

        def Gologin():
            self.Rpage.destroy()
            # import Login_page
            win=Tk()
            lg.Login_page(win)

        # ============variables====================



        self.fname = StringVar()
        self.roll = StringVar()
        self.phone = StringVar()
        self.Email = StringVar()
        self.Pword = StringVar()
        self.School = StringVar()
        self.Gaurdian = StringVar()
        self.Lname = StringVar()
        self.cal = StringVar()
        self.Gender = StringVar()



        # ============variables====================

        def Reg(self):
            Emai = Email.get() + "@gmail.com"
            print(cal.get())
            # print(Emai)
            # print(Email.get())
            # print("Button Clicked")
            # print(f"{fname.get()}")
            # print(f"{roll.get()}")
            # print(f"{phone.get()}")
            # print(f"{Email.get()}")
            # print(f"{Pword.get()}")
            # print(f"{School.get()}")
            # print(f"{Gaurdian.get()}")
            # print(f"{Lname.get()}")
            # print(f"{cal.get()}")
            # print(f"{Gender.get()}")
            if fname.get() == "" or roll.get()=="" or Lname.get() ==""  or  phone.get()=="" or Email.get()=="" or Pword.get()=="" or School.get()=="" or Gaurdian.get()=="" or cal.get()=="" or Gender.get()=="":
                messagebox.showerror("Error","All feilds are must",parent=self.Rpage)
            elif cb.get()=="Select Role":
                messagebox.showinfo("Select Role", "Please select valid Role")
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
                    my_c.execute(f"insert into {f} (Username,Name,Rollno,Type) values(%s,%s,%s,%s)",( Emai,fullN,roll.get(),cb.get()))
                    my_c.execute("insert into login values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            Emai,
                            Pword.get(),
                            cb.get(),
                            fname.get(),
                            Lname.get(),
                            roll.get(),
                            phone.get(),
                            School.get(),
                            Gaurdian.get(),
                            cal.get(),
                            Gender.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","You have been Registered Successfully",parent=self.Rpage)
                    self.Rpage.destroy()
                    win=Tk()
                    # import Login_page
                    lg.Login_page(win)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.Rpage)


        self.Rpage.geometry("1240x640")
        self.Rpage.configure(bg="#ffffff")

        def correct(inp):
            if inp.isdigit():
                return True
            elif inp == "":
                return True
            else:
                return False
        re=Rpage.register(correct)


        def correct_gen(inp):
            if inp=="M" or inp =="F":
                return True
            elif inp == "":
                return True
            else:
                return False
        re_gen=Rpage.register(correct_gen)


        canvas = Canvas(
            self.Rpage,
            bg="#ffffff",
            height=640,
            width=1240,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"pic\Rbackground.png")
        background = canvas.create_image(
            622.0, 321.0,
            image=background_img)

        fname_img = PhotoImage(file=f"pic\img_textBox0.png")
        fname_bg = canvas.create_image(
            148.0, 174.5,
            image=fname_img)
        fname = Entry(Rpage,
                      font = ("inner_black", 12),
                      bd=0,
                      bg="#ffffff",
                      highlightthickness=0)
        fname.place(
            x=86.0, y=163.5,
            width=120.0,
            height=23)


        Lname_img = PhotoImage(file=f"pic\img_textBox7.png")
        Lname_bg = canvas.create_image(
            292.0, 174.5,
            image=Lname_img)
        Lname = Entry(Rpage,
                      font=("inner_black", 12),
                      bd=0,
                      bg="#ffffff",
                      highlightthickness=0)
        Lname.place(
            x=230.0, y=163.5,
            width=124.0,
            height=23)


        Email_img = PhotoImage(file=f"pic\img_textBox3.png")
        Email_bg = canvas.create_image(
            220.0, 231.5,
            image=Email_img)
        Email = Entry(Rpage,
                      font=("inner_black", 12),
                      bd=0,
                      bg="#ffffff",
                      highlightthickness=0)
        Email.place(
            x=86.0, y=220.5,
            width=180.0,
            height=23)



        Pword_img = PhotoImage(file=f"pic\img_textBox4.png")
        Pword_bg = canvas.create_image(
            220.0, 288.5,
            image=Pword_img)
        Pword = Entry(Rpage,
                      font=("inner_black", 12),
                      bd=0,
                      bg="#ffffff",
                      show='*',
                      highlightthickness=0)
        Pword.place(
            x=86.0, y=277.5,
            width=268.0,
            height=23)


        School_img = PhotoImage(file=f"pic\img_textBox5.png")
        School_bg = canvas.create_image(
            220.0, 346.5,
            image=School_img)
        School = Entry(Rpage,
                       font=("inner_black", 12),
                       bd=0,
                       bg="#ffffff",
                       highlightthickness=0)
        School.place(
            x=86.0, y=335.5,
            width=268.0,
            height=23)


        roll_img = PhotoImage(file=f"pic\img_textBox1.png")
        roll_bg = canvas.create_image(
            148.0, 403.5,
            image=roll_img)
        roll = Entry(Rpage,
            font=("inner_black", 12),
            bd=0,
            bg="#ffffff",
            highlightthickness=0)
        roll.place(
            x=86.0, y=392.5,
            width=124.0,
            height=23)



        tb = time.ctime(time.time())
        a, b, c, d, e = tb.split()
        ls = [a, b, c, d, e]
        print(ls)

        sel = tk.StringVar()  # declaring string variable

        cal = DateEntry(Rpage, selectmode='day', textvariable=sel,year=2000)
        cal.place(
            x=235.0, y=392.5,
            width=124.0,
            height=23)

        Date_img = PhotoImage(file=f"pic\img_textBox8.png")
        Date_bg = canvas.create_image(
            292.0, 403.5,
            image=Date_img)

        def my_upd(*args):  # triggered when value of string varaible changes
            l1.config(text=sel.get())  # read and display date

        l1 = tk.Label(Rpage,font = ("inner_black", 12), bg='white')  # Label to display date
        l1.place(
            x=230.0, y=392.5,
            width=110.0,
            height=23)

        sel.trace('w', my_upd)

        # def my_up(*args):
        #     l5.config(text=sel.get())

        # sel=tkinter.StringVar()
        # e=int(e)
        # cal= DateEntry(Rpage,selectmode='day',year=e,month=1,day=1)

        # l5=tk.Label(Rpage)
        # sel.trace('w',my_up)




        # Date = Entry(Rpage,
        #              font=("inner_black", 12),
        #              bd=0,
        #              bg="#ffffff",
        #              highlightthickness=0)



        Gaurdian_img = PhotoImage(file=f"pic\img_textBox6.png")
        Gaurdian_bg = canvas.create_image(
            220.0, 457.5,
            image=Gaurdian_img)
        Gaurdian = Entry(Rpage,
                         font=("inner_black", 12),
                         bd=0,
                         bg="#ffffff",
                         highlightthickness=0)
        Gaurdian.place(
            x=86.0, y=446.5,
            width=268.0,
            height=23)


        phone_img = PhotoImage(file=f"pic\img_textBox2.png")
        phone_bg = canvas.create_image(
            148.0, 515.5,
            image=phone_img)
        phone = Entry(Rpage,
                      font=("inner_black", 12),
            bd=0,
            bg="#ffffff",
            highlightthickness=0)
        phone.place(
            x=86.0, y=504.5,
            width=124.0,
            height=23)
        phone.config(validate="key",validatecommand=(re,"%P"))


        li=["Male","Female","Not prefred to tell"]
        Gender = ttk.Combobox(self.Rpage, value=li, width=22, height=0, state="readonly")
        Gender.current(0)
        Gender.place(
            x=226.0, y=504.5,
            width=134.0,
            height=23
        )

        gm=Label(text="@gmail.com",font=("inner_black",12),bg="#ffffff").place(x=256.0, y=220.5)

        # Gender_img = PhotoImage(file=f"pic\img_textBox9.png")
        # Gender_bg = canvas.create_image(
        #     294.0, 515.5,
        #     image=Gender_img)
        # Gender = Entry(Rpage,
        #     bd=0,
        #     bg="#ffffff",
        #     highlightthickness=0)
        # Gender.place(
        #     x=232.0, y=503,
        #     width=124.0,
        #     height=23)
        # Gender.config(validate="key", validatecommand=(re_gen, "%P"))

        img0 = PhotoImage(file=f"pic\img0.png")
        b0 = Button(Rpage,
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=Gologin,
            relief="flat")
        b0.place(
            x=1015, y=611,
            width=155,
            height=23)

        img1 = PhotoImage(file=f"pic\img1.png")
        b1 = Button(Rpage,
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: Reg(self),
            relief="flat")
        b1.place(
            x=92, y=560,
            width=216,
            height=36)

        li = ["Select Role", "Student", "Parent", "Administrator"]
        cb = ttk.Combobox(self.Rpage, value=li, width=20, height=0, state="readonly")
        cb.current(0)
        cb.place(
            x=130, y=535,
        )

        # li = ["Student", "Parent", "Administrator"]
        # cbz = ttk.Combobox(self.Rpage, value=li, width=20, height=0)
        # cbz.place(
        #     x=500.5, y=520
        # )

        self.Rpage.resizable(False, False)
        self.Rpage.mainloop()
    def Call_Login(self):
        self.window=Toplevel(self.Rpage)
        self.app=Login_page.Login_page(self.window)


# def reg():
#     obj = register_page(Rpage)
#     Rpage.mainloop()
#
# Rpage = Tk()
# obj = register_page(Rpage)
# Rpage.mainloop()

if __name__ == '__main__':
    window = Tk()
    obj = register_page(window)
    window.mainloop()
