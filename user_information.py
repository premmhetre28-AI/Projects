from tkinter import*
from tkinter import messagebox
import re
import mysql.connector
con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="user_form"
    )
cursor=con.cursor()
con.commit()
def submit():
    name=name_entry.get()
    email=email_entry.get()
    age=age_entry.get()
    if(name==""):
        messagebox.showerror("Error","Name can not be empty")
        return
    # proper email validation
    pattern=r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+$"
    if(not re.match(pattern,email)):
        messagebox.showerror("Error","Enter valid Email")
        return
    if(not age.isdigit() or int(age)<0):
        messagebox.showerror("Error","Enter valid Age")
        return
    messagebox.showinfo("Successs","Form submited Successsful")
win=Tk()
win.title("User Info")
Label(win,text="name").grid(row=0,column=0,padx=5,pady=10)
name_entry=Entry(win)
name_entry.grid(row=0,column=1,padx=5,pady=10)
Label(win,text="Email").grid(row=1,column=0,padx=5,pady=10)
email_entry=Entry(win)
email_entry.grid(row=1,column=1,padx=5,pady=10)
Label(win,text="Age").grid(row=2,column=0,padx=5,pady=10)
age_entry=Entry(win)
age_entry.grid(row=2,column=1,padx=5,pady=10)
Button(win,text="Submit",command=submit).grid(row=3,column=1,padx=5,pady=10)
win.mainloop()