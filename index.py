from tkinter import *
import sqlite3
import tkinter.messagebox
# import sys
# from PyQt5.QtWidgets import *

#w = root.winfo_screenwidth()
#h = root.winfo_screenheight()f
root = Tk()
root.title("COMPANY BOSSCCOM")
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#=======================================VARIABLES=====================================
# USERNAME = StringVar()
# PASSWORD = StringVar()
# FIRSTNAME = StringVar()
# LASTNAME = StringVar()


class Application:
    def __init__(self, master):
        self.master = master
        self.logic1 = 1
        # frame
        self.left = Frame(master, width=1000, height=580, bg='lightblue')
        self.left.pack(side=LEFT)
        # components
        self.keyactive = Label(self.left, text="MÃ ID THIẾT BỊ:", font=('arial 12 bold'), fg='black',
                                 bg='lightblue')
        self.keyactive.place(x=50, y=40)

        self.adr_id = Entry(self.left, font=('arial 20 bold'), width=40)
        self.adr_id.place(x=60, y=100)

        self.keymail = Label(self.left, text="Địa chỉ mail:", font=('arial 12 bold'), fg='black',
                                 bg='lightblue')
        self.keymail.place(x=50, y=150)
        self.adr_mail = Entry(self.left, font=('arial 20 bold'), width=40)
        self.adr_mail.place(x=60, y=210)

        self.keyacticett = Label(self.left, text="Key Actice:", font=('arial 12 bold'), fg='black',
                                 bg='lightblue')
        self.keyacticett.place(x=50, y=260)
        self.adr_actice = Entry(self.left, font=('arial 20 bold'), width=40)
        self.adr_actice.place(x=60, y=310)

        # button
        self.bt_st_catalog = Button(self.left, text="Cập Nhật Mã Active", width=20, height=4, font=('arial 14 bold'),
                                    bg='orange',command=self.database_1)
        self.bt_st_catalog.place(x=100, y=420)

        self.bt_exit1 = Button(self.left, text="Đóng", width=20, height=4, font=('arial 14 bold'), bg='orange', command=self.quit)
        self.bt_exit1.place(x=355, y=420)


    def database_1(self):
        name_dtn1 = self.adr_id.get()
        name_dtn222 =  self.adr_mail.get()
        name_dtn3 =  self.adr_actice.get()

        conn = sqlite3.connect("d.db")
        cursor = conn.cursor()
        if name_dtn222 == '' or name_dtn1 == "" or name_dtn3 == "":
            tkinter.messagebox.showinfo("Error", "Điền đầy đủ thông tin.")
        else:
            # n=len(name_dtn222)+25061996
            # print(n)
            cursor.execute("DELETE FROM member WHERE id=1")
            cursor.execute('CREATE TABLE IF NOT EXISTS member (dt_id TEXT,address TEXT,key TEXT)')
            cursor.execute('INSERT INTO member (dt_id,address,key) VALUES(?,?,?)',
                           ( name_dtn1,name_dtn222,name_dtn3))
            tkinter.messagebox.showinfo("Success", "Đã ACtice")
            conn.commit()
            cursor.close()

    def quit(self):
        root.withdraw()
        root.destroy()

root.geometry("1024x600+0+0")
b = Application(root)
root.mainloop()
