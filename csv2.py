import pandas as pd
import time
import os


tb = time.ctime(time.time())
a, b, c, d, e = tb.split()
ls = [a, b, c, d, e]
print(ls)
date = input("Enter date in dd-mm-yyyy  format")
df = pd.read_csv("Attendance\Attendance_" + date + ".csv")
df_id = df["Id"].unique()
print(df_id)
df_name = df["Name"].unique()
print(df_name)
