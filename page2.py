from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import time
import Login_page as lg
import Teacher
import register as rg
import Student_d as sd
import forg as fg
import Teacher as Te
import page as pa


class page:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1240x640+0+0")
        self.root.title("Student's Meal Attendance Sheet")

        def fetch_data(self):
            tb = time.ctime(time.time())
            a, b, c, d, e = tb.split()
            ls = [a, b, c, d, e]
            f = b + e
            f = f.lower()
            file = open("ld.txt", "r")
            dta, roll = file.read().split(",")
            dta = (dta)
            roll = (roll)
            file.close()
            # try:
            #     conn = mysql.connector.connect(host="localhost", username="root", password="Aman", database="login_d")
            #     my_c = conn.cursor()
            #     # my_c.execute(f"select Name, Rollno, Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22 from {f}")
            #     my_c.execute(f"select Rollno, Name, Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22,Day23,Day24,Day25,Day26,Day27,Day28,Day29,Day30,Day31 from {f}")
            #     data = my_c.fetchall()
            #     row = my_c.rowcount
            #     print(data)
            #     print(row)
            #
            #     if len(data) != 0:
            #         self.student_table.delete(*self.student_table.get_children())
            #         for i in data:
            #             self.student_table.insert("", END, values=i)
            #             # print(i)
            #
            #     conn.commit()
            #     conn.close()
            #
            # except Exception as es:
            #     messagebox.showerror("Error", f"Error due to: {str(es)} ", parent=self.root)

            if roll == "Administrator":
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aman",
                                                   database="login_d")
                    my_c = conn.cursor()
                    # my_c.execute(f"select Name, Rollno, Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22 from {f}")
                    my_c.execute(
                        f"select Rollno, Name, Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22,Day23,Day24,Day25,Day26,Day27,Day28,Day29,Day30,Day31 from meal")

                    data = my_c.fetchall()
                    row = my_c.rowcount
                    # print(data)
                    # print(row)

                    if len(data) != 0:
                        # self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("", END, values=i)
                            # print(i)

                    conn.commit()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)} ", parent=self.root)

            else:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Aman",
                                                   database="login_d")
                    my_c = conn.cursor()
                    var = f
                    # my_c.execute(f"select Name, Rollno, Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22 from {f}")
                    my_c.execute(
                        f"select Rollno, Name, Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22,Day23,Day24,Day25,Day26,Day27,Day28,Day29,Day30,Day31 from meal where Username=%s and Type=%s",
                        (dta, roll))

                    data = my_c.fetchall()
                    row = my_c.rowcount
                    # print(data)
                    # print(row)

                    if len(data) != 0:
                        # self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("", END, values=i)
                            # print(i)

                    conn.commit()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to: {str(es)} ", parent=self.root)

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=10, y=10, width=1200, height=600)
        img3 = Image.open(f"pic/students.jpg")
        img3 = img3.resize((1240, 640))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(main_frame, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1240, height=640)

        my_label1 = Label(self.root, text="Student's Meal Attendance sheet", font=("pacifico", 25, "bold"), fg="Black")
        my_label1.place(x=0, y=40, width=1220, height=35)

        def btn_clicked1():
            file = open("ld.txt", "r")
            dta, roll = file.read().split(",")
            dta = (dta)
            roll = (roll)
            file.close()
            if roll == "Student":
                self.root.destroy()
                win = Tk()
                sd.Students(win)
            else:
                self.root.destroy()
                win = Tk()
                Te.Teacher(win)

        img01 = PhotoImage(file=f"pic/Fimg0.png")
        b1 = Button(
            image=img01,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked1,
            relief="flat")

        b1.place(
            x=58, y=44,
            width=81,
            height=30)

        frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance", font=("times new roman", 12, "bold"))
        frame.place(x=100, y=60, width=1000, height=500)

        # Searchframe=LabelFrame(frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12, "bold"))
        # Searchframe.place(x=2,y=12,width=1160, height=460)

        scroll_x = ttk.Scrollbar(frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(frame, column=(
        "Roll", "Name", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Roll", text="Roll_number")
        self.student_table.heading("Name", text="Student_Name")

        self.student_table.heading("1", text="1")

        self.student_table.heading("2", text="2")

        self.student_table.heading("3", text="3")

        self.student_table.heading("4", text="4")

        self.student_table.heading("5", text="5")

        self.student_table.heading("6", text="6")

        self.student_table.heading("7", text="7")

        self.student_table.heading("8", text="8")

        self.student_table.heading("9", text="9")

        self.student_table.heading("10", text="10")

        self.student_table.heading("11", text="11")

        self.student_table.heading("12", text="12")

        self.student_table.heading("13", text="13")

        self.student_table.heading("14", text="14")

        self.student_table.heading("15", text="15")

        self.student_table.heading("16", text="16")

        self.student_table.heading("17", text="17")

        self.student_table.heading("18", text="18")

        self.student_table.heading("19", text="19")

        self.student_table.heading("20", text="20")

        self.student_table.heading("21", text="21")

        self.student_table.heading("22", text="22")

        self.student_table.heading("23", text="23")

        self.student_table.heading("24", text="24")

        self.student_table.heading("25", text="25")

        self.student_table.heading("26", text="26")

        self.student_table.heading("27", text="27")

        self.student_table.heading("28", text="28")

        self.student_table.heading("29", text="29")

        self.student_table.heading("30", text="30")

        self.student_table.heading("31", text="31")
        self.student_table["show"] = "headings"

        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.column("Roll", width=80)
        self.student_table.column("Name", width=90)
        self.student_table.column("1", width=10)
        self.student_table.column("2", width=10)
        self.student_table.column("3", width=10)
        self.student_table.column("4", width=10)
        self.student_table.column("5", width=10)
        self.student_table.column("6", width=10)
        self.student_table.column("7", width=10)

        self.student_table.column("8", width=10)
        self.student_table.column("9", width=10)
        self.student_table.column("10", width=10)
        self.student_table.column("11", width=10)
        self.student_table.column("12", width=10)
        self.student_table.column("13", width=10)
        self.student_table.column("14", width=10)
        self.student_table.column("15", width=10)
        self.student_table.column("16", width=10)
        self.student_table.column("17", width=10)
        self.student_table.column("18", width=10)
        self.student_table.column("19", width=10)
        self.student_table.column("20", width=10)
        self.student_table.column("21", width=10)
        self.student_table.column("22", width=10)
        self.student_table.column("23", width=10)
        self.student_table.column("24", width=10)
        self.student_table.column("25", width=10)

        self.student_table.column("26", width=10)
        self.student_table.column("27", width=10)
        self.student_table.column("28", width=10)
        self.student_table.column("29", width=10)
        self.student_table.column("30", width=10)
        self.student_table.column("31", width=10)

        fetch_data(self)

        self.root.resizable(False, False)
        self.root.mainloop()


# ================ ===============Trassh======================================


# fetch data
# def fetch_data(self):
#     tb = time.ctime(time.time())
#     a, b, c, d, e = tb.split()
#     ls = [a, b, c, d, e]
#     f = b + e
#     f = f.lower()
#     conn=mysql.connector.connect(host="localhost",username="root",password="Aman",database="testing")
#     my_c = conn.cursor()
# my_c.execute(f"select Name, Rollno, Day1,Day2,Day3,Day4,Day5,Day6,Day7,Day8,Day9,Day10,Day11,Day12,Day13,Day14,Day15,Day16,Day17,Day18,Day19,Day20,Day21,Day22 from {f}")
#     my_c.execute(f"select * from {f}")
#     data=my_c.fetchall()
#     row= my_c.rowcount
#     print(data)
#     print(row)
#
#     if len(data)!=0:
#         # self.student_table.delete(*self.student_table.get_children())
#         for i in data:
#             self.student_table.insert("",END,values=i)
#             print(i)
#         conn.commit()
#     conn.close()


# ================ ===============Trassh======================================


if __name__ == "__main__":
    root = Tk()
    obj = page(root)
    root.mainloop()

