from tkinter import *
import sqlite3
import tkinter as tk
import tkinter.messagebox
from datetime import date
from tkinter import ttk
import datetime
import sys
from fpdf import FPDF
import webbrowser
import cv2
import os
from PyQt5 import QtCore, QtGui, QtWidgets  # uic
from PyQt5.QtWidgets import (QLabel)  # +++
from PyQt5.QtCore import QTimer
import shutil
from test2_ui import Ui_Form
import numpy as np
import time
import imutils
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import subprocess
import re

# Load Yolo
# net = cv2.dnn.readNet("yolov3-tiny_last.weights", "yolov3-tiny.cfg")
# classes = []
# with open("classes3.txt", "r") as f:
#     classes = [line.strip() for line in f.readlines()]

today = date.today()
date = datetime.datetime.now().date()
# temporary lists like sessions
products_list = []
product_price = []
product_quantity = []
product_id = []
# list for labels
# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()f
root = Tk()
# root1 = Tk()
# root2 = Tk()
# root.overrideredirect(True)
root.title("COMPANY BOSSCCOM")
newWindowaddf = Toplevel(root)
newWindowaddf.title("add infomation")
newWindowaddf.geometry("980x550+0+0")
#

addWindow = tk.Tk()
addWindow.title("Set form print")
addWindow.geometry("980x550+0+0")
#

labels_list = []
var = IntVar()
var1 = IntVar()
c = StringVar()
c1 = StringVar()
logic1 = 1
USERNAME = StringVar()
PASSWORD = StringVar()


class Application:
    def __init__(self, master):
        connkey = sqlite3.connect("d.db")
        cursorkey = connkey.cursor()

        # cursorkey.execute(
        #     "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")
        # self.leftkey = Frame(master,width=1000, height=550, bg='lightblue')
        # self.leftkey.pack(side=LEFT)
        # self.LABELKEY = Label( self.leftkey, text="WELL COME TO DEVICE BOSSCOM - INPUT KEY ACTIVE", font=('arial 20 bold'), fg='black',bg='lightblue')
        # self.LABELKEY.place(x=150, y=60)
        #
        # self.LABELKEY1 = Label(self.leftkey, text="Mã ID THIẾT BỊ:",
        #                       font=('arial 28 bold'), fg='black', bg='lightblue')
        # self.LABELKEY1.place(x=120, y=110)
        #
        # self.name_key = Entry(self.leftkey, font=('arial 26 bold'), width=40)
        # self.name_key.place(x=150, y=160)
        #
        # self.LABELKEY2 = Label(self.leftkey, text="ĐỊA CHỈ EMAIL:",
        #                        font=('arial 28 bold'), fg='black', bg='lightblue')
        # self.LABELKEY2.place(x=120, y=230)
        # self.mail= Entry(self.leftkey, font=('arial 26 bold'), width=40)
        # self.mail.place(x=150, y=280)
        #
        #
        # self.LABELKEY3 = Label(self.leftkey, text="KEY ACTICE:",
        #                        font=('arial 28 bold'), fg='black', bg='lightblue')
        # self.LABELKEY3.place(x=120, y=380)
        # self.name_keyK = Entry(self.leftkey, font=('arial 26 bold'), width=40)
        # self.name_keyK.place(x=150, y=430)
        h1 = 'A88dH5e8867' + self.getserial()
        num1 = re.sub(r'\D', "", h1)
        name_dtn1 = self.getserial()
        nux = int(num1)
        n = len(name_dtn1) * nux
        num = re.sub(r'\d', "", h1)
        h22 = str(n) + str(num)
        USERNAME1 = h1
        USERNAME2 = str(h22)

        cursorkey.execute("SELECT * FROM `member` WHERE `dt_id` = ? and `address` = ? and `key` = ?",
                          (USERNAME1, USERNAME2, USERNAME2))
        if cursorkey.fetchone() is not None:
            self.master = master
            self.logic1 = 1
            self.logic2 = 1
            self.logic3 = 1
            # frame
            self.left = Frame(master, width=215, height=600, bg='white')
            self.left.pack(side=LEFT)
            # components
            self.date_l = Label(self.left,
                                text="Today's Date: " + str(today.day) + "-" + str(today.month) + "-" + str(today.year),
                                font=('arial 12 bold'), bg='lightblue',
                                fg='white')
            self.date_l.place(x=10, y=0)

            # button
            self.bt_st_catalog = Button(self.left, text="Hồ sơ bệnh nhân", width=16, height=4, font=('arial 14 bold'),
                                        bg='orange', command=self.ajax)
            self.bt_st_catalog.place(x=5, y=30)

            self.bt_st_form = Button(self.left, text="Nội soi", width=16, height=4, font=('arial 14 bold'), bg='orange',
                                     command=self.endoscopy)  # get_itemsdatabase)
            self.bt_st_form.place(x=5, y=136)

            self.bt_patient = Button(self.left, text="Biểu mẫu in", width=16, height=4, font=('arial 14 bold'),
                                     bg='orange',
                                     command=self.add_to_bn)
            self.bt_patient.place(x=5, y=242)

            self.bt_endoscop = Button(self.left, text="Danh mục khám", width=16, height=4, font=('arial 14 bold'),
                                      bg='orange', command=self.createNewWindow)
            self.bt_endoscop.place(x=5, y=348)

            self.bt_exit1 = Button(self.left, text="Thoát", width=16, height=4, font=('arial 14 bold'), bg='orange',
                                   command=self.quit)
            self.bt_exit1.place(x=5, y=454)

            addWindow.withdraw()
            newWindowaddf.withdraw()

        else:
            h1 = 'A88dH5e8867' + self.getserial()
            self.left = Frame(root, width=1000, height=580, bg='lightblue')
            self.left.pack(side=LEFT)
            # components
            self.keyactive = Label(self.left, text="MÃ ID THIẾT BỊ:", font=('arial 12 bold'), fg='black',
                                   bg='lightblue')
            self.keyactive.place(x=50, y=40)

            self.adr_id = Text(root, height=1, width=40, bg="light yellow", font=('arial 20 bold'), fg='red')
            self.adr_id.place(x=60, y=100)
            self.adr_id.insert(END, h1)

            self.keymail = Label(self.left, text="Địa chỉ mail:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.keymail.place(x=50, y=150)
            self.adr_mail = Entry(self.left, font=('arial 20 bold'), width=40)
            self.adr_mail.place(x=60, y=210)

            self.keyacticett = Label(self.left, text="Key Actice:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.keyacticett.place(x=50, y=260)
            self.adr_actice = Entry(self.left, font=('arial 20 bold'), width=40)
            self.adr_actice.place(x=60, y=310)

            # button
            self.bt_st_catalog = Button(self.left, text="Cập Nhật Mã Active", width=20, height=4,
                                        font=('arial 14 bold'), bg='orange', command=self.database_1)
            self.bt_st_catalog.place(x=100, y=420)

            self.bt_exit1 = Button(self.left, text="Đóng", width=20, height=4, font=('arial 14 bold'), bg='orange',
                                   command=self.quitdd)
            self.bt_exit1.place(x=355, y=420)
            addWindow.withdraw()
            newWindowaddf.withdraw()

    def database_1(self):
        h1 = 'A88dH5e8867' + self.getserial()
        name_dtn1 = h1
        name_dtn222 = self.adr_actice.get()
        name_dtn3 = self.adr_actice.get()

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
                           (name_dtn1, name_dtn222, name_dtn3))
            tkinter.messagebox.showinfo("Success", "Đã ACtice")
            conn.commit()
            cursor.close()
    #  root.withdraw()

    # def quit(self):
    # root.destroy()
    def getserial(self):
        # Extract serial from cpuinfo file
        cpuserial = "0000000000000000"
        try:
            f = open('/proc/cpuinfo', 'r')
            for line in f:
                if line[0:6] == 'Serial':
                    cpuserial = line[10:26]
                    # print(cpuserial)
            # print(cpuserial)
            f.close()
        except:
            cpuserial = "ERROR000000000"

        return cpuserial

        #  self.leftkey = Frame(root, width=1000, height=550, bg='lightblue')
        #  self.leftkey.pack(side=LEFT)
        #  self.LABELKEY = Label(self.leftkey, text="XIN VUI LÒNG ĐIỀN MÃ ACTICE TRƯỚC KHI SỬ DỤNG",
        #                       font=('arial 24 bold'), fg='red', bg='lightblue')
        #  self.LABELKEY.place(x=50, y=250)
        #  self.LABELKEY22 = Label(self.leftkey, text="LIỆN HỆ TRỢ GIÚP : BOSSCOM COMPANY",
        #                        font=('arial 16 bold'), fg='red', bg='lightblue')
        #  self.LABELKEY22.place(x=120, y=300)

        # self.name_key.focus()

    #  self.LoginForm()

    def Search(self):
        # =====================================Table WIDGET=========================================
        self.tree.delete(*self.tree.get_children())
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM `member` WHERE `name` LIKE ? AND `job` LIKE ? AND `address` LIKE ? AND `age` LIKE ?",
            ('%' + str(self.name_infos.get()) + '%', '%' + str(self.from_jobs.get()) + '%',
             '%' + str(self.from_addss.get()) + '%', '%' + str(self.born_agess.get()) + '%'))
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        self.name_infos.delete(0, tk.END)
        self.from_jobs.delete(0, tk.END)
        self.from_addss.delete(0, tk.END)
        self.born_agess.delete(0, tk.END)

    def ajax(self):
        if (self.logic1 == 1):
            self.right = Frame(root, width=800, height=92, bg='white')
            self.right.pack(side=TOP)

            self.bottom = Frame(root, width=800, height=220, bg='lightblue')
            self.bottom.pack(side=TOP)

            self.bottom1 = Frame(root, width=800, height=80, bg='yellow')
            self.bottom1.pack(side=TOP)

            self.bottom2 = Frame(root, width=800, height=550, bg='lightblue')
            self.bottom2.pack(side=TOP)

            self.Top = Frame(self.bottom2, width=800, bd=2, relief=SOLID)
            self.Top.pack(side=TOP)
            self.MidFrame = Frame(self.bottom2, width=800)
            self.MidFrame.pack(side=TOP)
            self.RightForm = Frame(self.MidFrame, width=800)
            self.RightForm.pack(side=RIGHT)

            self.bt_add_patient = Button(self.right, text="Lưu hồ sơ", width=11, height=4, font=('arial 12 bold'),
                                         bg='white', command=self.get_itemsdatabase)
            self.bt_add_patient.place(x=0, y=0)

            self.bt_open_file = Button(self.right, text="Mở hồ sơ", width=11, height=4, font=('arial 12 bold'),
                                       bg='white',
                                       command=self.create_pdf1)
            self.bt_open_file.place(x=123, y=0)
            #
            self.bt_save_file = Button(self.right, text="Làm mới", width=11, height=4, font=('arial 12 bold'),
                                       bg='white',
                                       command=self.delete_text)
            self.bt_save_file.place(x=246, y=0)
            #
            self.bt_delele1 = Button(self.right, text="Xóa", width=11, height=4, font=('arial 12 bold'), bg='white',
                                     command=self.Deletedata)
            # command=self.Deletedata)
            self.bt_delele1.place(x=369, y=0)
            #
            self.bt_thoat = Button(self.right, text="Đóng", width=12, height=4, font=('arial 12 bold'), bg='white',
                                   command=self.add_to_cart)

            self.bt_thoat.place(x=492, y=0)
            self.bt_thoat = Button(self.right, text="Khôi phục cài đặt gốc", width=16, height=4, font=('arial 12 bold'),
                                   bg='white', command=self.Deletealldata)
            self.bt_thoat.place(x=625, y=0)

            self.tenbenhnhan = Label(self.bottom, text="Tên bệnh nhân:", font=('arial 12 bold'), fg='black',
                                     bg='lightblue')
            self.tenbenhnhan.place(x=15, y=5)

            self.name_p = Entry(self.bottom, font=('arial 20 bold'), width=20)
            self.name_p.place(x=5, y=30)
            self.name_p.focus()

            self.adr = Label(self.bottom, text="Địa chỉ:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.adr.place(x=15, y=75)

            self.adr_p = Entry(self.bottom, font=('arial 20 bold'), width=20)
            self.adr_p.place(x=5, y=100)

            self.year_b = Label(self.bottom, text="Năm sinh:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.year_b.place(x=15, y=150)

            self.y_b = Entry(self.bottom, font=('arial 20 bold'), width=20)
            self.y_b.place(x=5, y=175)

            self.job = Label(self.bottom, text="Nghề nghiệp:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.job.place(x=330, y=5)
            self.jobw = Entry(self.bottom, font=('arial 20 bold'), width=18)
            self.jobw.place(x=320, y=30)

            self.st = Label(self.bottom, text="Triệu chứng:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.st.place(x=330, y=75)
            self.stom = Entry(self.bottom, font=('arial 20 bold'), width=18)
            self.stom.place(x=320, y=100)

            self.sbh = Label(self.bottom, text="Số bảo hiểm:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.sbh.place(x=330, y=150)
            self.nbh = Entry(self.bottom, font=('arial 20 bold'), width=18)
            self.nbh.place(x=320, y=175)

            self.tel = Label(self.bottom, text="Điện thoại:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.tel.place(x=615, y=5)
            self.telw = Entry(self.bottom, font=('arial 20 bold'), width=12)
            self.telw.place(x=605, y=30)

            # self.enteride = Entry(self.bottom, width=25, font=('arial 18 bold'), bg='lightblue')
            # self.enteride.place(x=800, y=175)
            # self.enteride.focus()

            self.droplist = OptionMenu(self.bottom, c, 'NAM', 'NỮ')
            self.droplist.pack()
            self.menu = self.droplist.nametowidget(self.droplist.menuname)
            self.menu.configure(font=('arial 20 bold'))
            c.set('NAM')
            self.droplist.config(width=10, font=('arial 18 bold'))
            self.droplist.place(x=610, y=95)

            self.seachinfo = Button(self.bottom1, text="Tìm kiếm", width=12, height=2, font=('arial 14 bold'),
                                    bg='orange',
                                    command=self.Search)
            self.seachinfo.place(x=640, y=10)

            self.name_info = Label(self.bottom1, text="Tên:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.name_info.place(x=5, y=10)

            self.name_infos = Entry(self.bottom1, width=18, font=('arial 18 bold'), bg='white')
            self.name_infos.place(x=5, y=38)

            self.job_s = Label(self.bottom1, text="Nghề nghiệp:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.job_s.place(x=245, y=10)
            self.from_jobs = Entry(self.bottom1, font=('arial 18 bold'), width=12)
            self.from_jobs.place(x=245, y=38)

            self.aadd_s = Label(self.bottom1, text="Địa Chỉ:", font=('arial 12 bold'), fg='black', bg='lightblue')
            self.aadd_s.place(x=410, y=10)
            self.from_addss = Entry(self.bottom1, font=('arial 18 bold'), width=10)
            self.from_addss.place(x=410, y=38)

            self.born_s2 = Label(self.bottom1, text="Năm sinh:", font=('arial 10 bold'), fg='black', bg='lightblue')
            self.born_s2.place(x=550, y=10)
            self.born_agess = Entry(self.bottom1, font=('arial 18 bold'), width=6)
            self.born_agess.place(x=550, y=38)

            self.scrollbarx = Scrollbar(self.RightForm, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.RightForm, orient=VERTICAL)
            self.tree = ttk.Treeview(self.RightForm, columns=("Id", "Name", "Job", "Address", "Age"),
                                     selectmode="extended",
                                     height=400, yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
            self.scrollbary.config(command=self.tree.yview)
            self.scrollbary.pack(side=RIGHT, fill=Y)
            self.scrollbarx.config(command=self.tree.xview)
            self.scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree.column('#1', stretch=NO, minwidth=0, width=50)
            self.tree.column('#2', stretch=NO, minwidth=0, width=300)
            self.tree.column('#3', stretch=NO, minwidth=0, width=160)
            self.tree.column('#4', stretch=NO, minwidth=0, width=160)

            self.tree.pack()
            self.tree.heading('Id', text="Id", anchor=W)
            self.tree.heading('Name', text="Name", anchor=W)
            self.tree.heading('Job', text="Job", anchor=W)
            self.tree.heading('Address', text="Address", anchor=W)
            self.tree.heading('Age', text="Age", anchor=W)
            self.logic1 = 2

    def Deletedata(self):

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item in self.tree.selection():
            # print(selected_item)  # it prints the selected row id
            cursor.execute("DELETE FROM member WHERE id=?", (self.tree.set(selected_item, '#1'),))
            self.tree.delete(selected_item)
        conn.commit()
        conn.close()

    def Deletealldata(self):
        shutil.rmtree("anh")
        conn = sqlite3.connect("db_member.db")
        cur = conn.cursor()
        sql = 'DELETE FROM member'
        cur.execute(sql)
        conn.commit()

    def get_itemsdatabase(self):

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()

        if self.logic1 == 1 or self.name_p.get() == '' or self.adr_p.get() == '' or self.y_b.get() == '' or self.jobw.get() == '' or self.stom.get() == '' or self.nbh.get() == '' or c.get() == '' or self.telw.get() == '':
            tkinter.messagebox.showinfo("Error", "Điền đầy đủ thông tin bệnh nhân.")
        else:

            cursor.execute('INSERT INTO member (name, address, age, job, symptom,sbh,sex,tel ) VALUES(?,?,?,?,?,?,?,?)',
                           (
                               self.name_p.get(), self.adr_p.get(), self.y_b.get(), self.jobw.get(), self.stom.get(),
                               self.nbh.get(),
                               c.get(), self.telw.get()))
            conn.commit()
            self.name_p.delete(0, END)
            self.adr_p.delete(0, END)
            self.y_b.delete(0, END)
            self.jobw.delete(0, END)
            self.stom.delete(0, END)
            self.nbh.delete(0, END)
            self.telw.delete(0, END)
            self.endoscopy()
            # textbox insert
            # tkinter.messagebox.showinfo("Success", "Successfully added to the database")

    def add_to_cart(self):

        self.right.destroy()
        self.bottom.destroy()
        self.bottom1.destroy()
        self.bottom2.destroy()
        self.logic1 = 1

    def delete_text(self, *args, **kwargs):

        self.name_p.delete(0, END)
        self.adr_p.delete(0, END)
        self.y_b.delete(0, END)
        self.jobw.delete(0, END)
        self.stom.delete(0, END)
        self.nbh.delete(0, END)

    def database_print(self, *args, **kwargs):

        namepk = self.adr2_p.get()
        name_dt = self.doctor_p.get()
        address_pk = self.n2_p.get()
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if namepk == '' or name_dt == '' or address_pk == '':
            # self.logic2 = 2
            # tkinter.messagebox.showinfo("Error", "Điền đầy đủ thông tin.")
            self.addrn = Label(self.rightw3, text="Điền đầy đủ thông tin! ", font=('arial 18 bold'), fg='black', bg='white')
            self.addrn.place(x=200, y=520)
        else:

            cursor.execute("DELETE FROM print_dt WHERE id=1")
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dt (name_pk TEXT,dt_name TEXT,address TEXT)')
            cursor.execute('INSERT INTO print_dt (name_pk,dt_name,address) VALUES(?,?,?)',
                           (namepk, name_dt, address_pk))
            # tkinter.messagebox.showinfo("Success", "Đã thêm thông tin")

            conn.commit()
            cursor.close()
            self.adr2_p.delete(0, END)
            self.doctor_p.delete(0, END)
            self.n2_p.delete(0, END)

            self.rightw2.destroy()
            self.rightw3.destroy()
            addWindow.update()
            addWindow.deiconify()
            self.rightw2 = Frame(addWindow, width=550, height=600, bg='lightblue')
            self.rightw2.pack(side=RIGHT)
            self.rightw3 = Frame(addWindow, width=600, height=600, bg='lightblue')
            self.rightw3.pack(side=LEFT)

            self.adr2 = Label(self.rightw3, text="Phòng khám:", font=('arial 16 bold'), fg='black', bg='lightblue')
            self.adr2.place(x=10, y=10)
            self.adr2_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
            self.adr2_p.place(x=150, y=10)

            self.doctor = Label(self.rightw3, text=" Bác sĩ :", font=('arial 16 bold'), fg='black', bg='lightblue')
            self.doctor.place(x=10, y=85)

            self.doctor_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
            self.doctor_p.place(x=150, y=75)

            self.n2 = Label(self.rightw3, text="Địa chỉ:", font=('arial 16 bold'), fg='black', bg='lightblue')
            self.n2.place(x=10, y=155)

            self.n2_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
            self.n2_p.place(x=150, y=150)

            self.add_dt = Button(self.rightw3, text="Cập nhật", width=15, height=3, font=('arial 18 bold'),
                                 bg='orange',
                                 command=self.database_print)
            self.add_dt.place(x=40, y=220)

            self.add_dltd = Button(self.rightw3, text="Xóa", width=15, height=3, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.Deletedata_print)  # command=self.quit_print2)
            self.add_dltd.place(x=275, y=220)

            self.addrn = Label(self.rightw3, text="Icon Addr:", font=('arial 18 bold'), fg='black', bg='lightblue')
            self.addrn.place(x=10, y=360)

            self.addrn_p = Entry(self.rightw3, font=('arial 22 bold'), width=25)
            self.addrn_p.place(x=130, y=360)

            self.add_dl = Button(self.rightw3, text="Thêm Icon", width=15, height=3, font=('arial 18 bold'),
                                 bg='orange', command=self.openfile)
            self.add_dl.place(x=35, y=410)
            self.add_dl = Button(self.rightw3, text="Đóng", width=15, height=3, font=('arial 18 bold'),
                                 bg='orange', command=self.quit11)
            self.add_dl.place(x=260, y=410)
            self.addrn = Label(self.rightw3, text="Đã thêm đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=200, y=520)

            self.scrollbarx = Scrollbar(self.rightw2, orient=HORIZONTAL)
            self.scrollbary = Scrollbar(self.rightw2, orient=VERTICAL)
            self.tree1 = ttk.Treeview(self.rightw2, columns=("Id", "Phòng khám", "Bác sĩ", "Địa chỉ"),
                                      selectmode="extended",
                                      height=400, yscrollcommand=self.scrollbary.set,
                                      xscrollcommand=self.scrollbarx.set)
            self.scrollbary.config(command=self.tree1.yview)
            self.scrollbary.pack(side=RIGHT, fill=Y)
            self.scrollbarx.config(command=self.tree1.xview)
            self.scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree1.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree1.column('#1', stretch=NO, minwidth=0, width=20)
            self.tree1.column('#2', stretch=NO, minwidth=0, width=180)
            self.tree1.column('#3', stretch=NO, minwidth=0, width=120)
            self.tree1.column('#4', stretch=NO, minwidth=0, width=80)

            self.tree1.pack()
            self.tree1.heading('Id', text="Id", anchor=W)
            self.tree1.heading('Phòng khám', text="Phòng khám", anchor=W)
            self.tree1.heading('Bác sĩ', text="Bác sĩ", anchor=W)
            self.tree1.heading('Địa chỉ', text="Địa chỉ", anchor=W)
            self.tree1.pack()

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `print_dt`")
            fetch = cursor.fetchall()
            for data in fetch:
                self.tree1.insert('', 'end', values=(data))
            cursor.close()
            conn.close()



    def Deletedata_print(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree1.selection():
            print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt WHERE id=?", (self.tree1.set(selected_item1, '#1'),))
            conn.commit()
            self.tree1.delete(selected_item1)
        conn.commit()
        cursor.close()

    def Chosedata_print(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree1.selection():
            #print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt WHERE id=?", (self.tree1.set(selected_item1, '#1'),))
            conn.commit()
            self.tree1.delete(selected_item1)
        conn.commit()
        cursor.close()

    def database_print111(self):
        nameadd22 = c1.get() + " " + self.ad_if2.get()
        name_dt22 = self.ad_if2.get()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if nameadd22 == '' or name_dt22 == '':

            self.addrn = Label(self.rightw333, text="Điền đầy đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=70, y=460)

        else:
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dt22 (name_pk22 TEXT,dt_name22 TEXT)')
            cursor.execute('INSERT INTO print_dt22 (name_pk22,dt_name22) VALUES(?,?)', (nameadd22, name_dt22))

            # tkinter.messagebox.showinfo("Success", "Đã thêm thông tin")
            conn.commit()
            cursor.close()

            self.ad_if2.delete(0, END)

            self.rightw222.destroy()
            self.rightw444.destroy()
            self.rightw333.destroy()
            newWindowaddf.update()
            newWindowaddf.deiconify()

            self.rightw222 = Frame(newWindowaddf, width=205, height=500, bg='lightblue')
            self.rightw222.pack(side=RIGHT)
            self.rightw444 = Frame(newWindowaddf, width=205, height=500, bg='lightyellow')
            self.rightw444.pack(side=RIGHT)
            self.rightw333 = Frame(newWindowaddf, width=540, height=500, bg='lightblue')
            self.rightw333.pack(side=LEFT)

            self.n3 = Label(self.rightw333, text="Danh Mục Chẩn Đoán:", font=('arial 14 bold'), fg='black',
                            bg='lightblue')
            self.n3.place(x=10, y=10)

            self.ad_if2 = Entry(self.rightw333, font=('arial 28 bold'), width=16)
            self.ad_if2.place(x=188, y=39)

            # self.n4 = Label(self.rightw3, text="Danh Mục:", font=('arial 14 bold'), fg='black', bg='lightblue')
            # self.n4.place(x=10, y=90)

            self.droplist1 = OptionMenu(self.rightw333, c1, 'TAI', 'MŨI', 'HỌNG')
            self.droplist1.pack()

            self.menu = self.droplist1.nametowidget(self.droplist1.menuname)
            self.menu.configure(font=('arial 28 bold'))
            c1.set('HỌNG')

            self.droplist1.config(width=9, height=1, font=('arial 20 bold'))
            self.droplist1.place(x=5, y=40)

            self.add_ifmt = Button(self.rightw333, text="Cập Nhật", width=12, height=2, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.database_print111)
            self.add_ifmt.place(x=5, y=90)

            self.n4 = Label(self.rightw333, text="Phương Pháp Điều Trị:", font=('arial 14 bold'), fg='black',
                            bg='lightblue')
            self.n4.place(x=10, y=185)

            self.ad_j2 = Entry(self.rightw333, font=('arial 28 bold'), width=24)
            self.ad_j2.place(x=10, y=215)

            self.add_ifmj = Button(self.rightw333, text="Cập nhật", width=12, height=2, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.database_printnn1)
            self.add_ifmj.place(x=5, y=270)

            self.add_dltifmtjj = Button(self.rightw333, text="Xóa", width=16, height=2, font=('arial 18 bold'),
                                        bg='orange', command=self.Deletedata_NewWindow)
            self.add_dltifmtjj.place(x=25, y=375)
            self.add_dltifmtjj = Button(self.rightw333, text="Đóng", width=16, height=2, font=('arial 18 bold'),
                                        bg='orange', command=self.quit22)
            self.add_dltifmtjj.place(x=260, y=375)
            self.addrn = Label(self.rightw333, text="Đã thêm đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=70, y=460)

            # self.add_dltd = Button(self.rightw3, text="Đóng", width=14, height=2, font=('arial 20 bold'),
            #                        bg='orange', command=self.quit_print1)
            # self.add_dltd.place(x=5, y=400)
            scrollbary = Scrollbar(self.rightw222, orient=VERTICAL)
            scrollbarx = Scrollbar(self.rightw222, orient=HORIZONTAL)
            self.tree2 = ttk.Treeview(self.rightw222, columns=("Danh Mục", "Chẩn Đoán"),
                                      selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                      xscrollcommand=scrollbarx.set)
            scrollbary.config(command=self.tree2.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=self.tree2.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree2.heading('Danh Mục', text="Danh Mục", anchor=W)
            self.tree2.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
            self.tree2.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree2.column('#1', stretch=NO, minwidth=0, width=200)
            self.tree2.column('#2', stretch=NO, minwidth=0, width=0)
            self.tree2.pack()

            scrollbary = Scrollbar(self.rightw444, orient=VERTICAL)
            scrollbarx = Scrollbar(self.rightw444, orient=HORIZONTAL)
            self.tree4 = ttk.Treeview(self.rightw444, columns=("Danh Mục Chẩn Đoán", "Chỉ Định"),
                                      selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                      xscrollcommand=scrollbarx.set)
            scrollbary.config(command=self.tree4.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=self.tree2.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree4.heading('Danh Mục Chẩn Đoán', text="Danh Mục Chẩn Đoán", anchor=W)
            self.tree4.heading('Chỉ Định', text="Chỉ Định", anchor=W)
            self.tree4.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree4.column('#1', stretch=NO, minwidth=0, width=0)
            self.tree4.column('#2', stretch=NO, minwidth=0, width=195)
            self.tree4.pack()

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor1 = conn.cursor()
            cursor.execute("SELECT * FROM `print_dt22`")
            fetch = cursor.fetchall()
            cursor1.execute("SELECT * FROM `print_jb22`")
            fetch1 = cursor1.fetchall()
            for data in fetch:
                self.tree2.insert('', 'end', values=(data))
            for data1 in fetch1:
                self.tree4.insert('', 'end', values=(data1))
            cursor.close()
            conn.close()
            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            # addWindow.withdraw()
            # self.createNewWindow()


    def database_printnn1(self):
        name_dtn222 = self.ad_j2.get()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if name_dtn222 == '':
            self.addrn = Label(self.rightw333, text="Điền đầy đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=70, y=460)

        else:
            # cursor.execute('CREATE TABLE IF NOT EXISTS print_jb22 (name_pjb22 TEXT)')
            # cursor.execute('INSERT INTO print_jb22 (name_pjb22) VALUES(?)',(name_dtn222))
            cursor.execute('CREATE TABLE IF NOT EXISTS print_jb22 (name_j22 TEXT,dt_namej TEXT)')
            cursor.execute('INSERT INTO print_jb22 (name_j22,dt_namej) VALUES(?,?)', (name_dtn222, name_dtn222))



            conn.commit()
            cursor.close()

            self.ad_j2.delete(0, END)

            self.rightw222.destroy()
            self.rightw444.destroy()
            self.rightw333.destroy()
            newWindowaddf.update()
            newWindowaddf.deiconify()

            self.rightw222 = Frame(newWindowaddf, width=205, height=500, bg='lightblue')
            self.rightw222.pack(side=RIGHT)
            self.rightw444 = Frame(newWindowaddf, width=205, height=500, bg='lightyellow')
            self.rightw444.pack(side=RIGHT)
            self.rightw333 = Frame(newWindowaddf, width=540, height=500, bg='lightblue')
            self.rightw333.pack(side=LEFT)


            self.n3 = Label(self.rightw333, text="Danh Mục Chẩn Đoán:", font=('arial 14 bold'), fg='black',
                            bg='lightblue')
            self.n3.place(x=10, y=10)

            self.ad_if2 = Entry(self.rightw333, font=('arial 28 bold'), width=16)
            self.ad_if2.place(x=188, y=39)

            # self.n4 = Label(self.rightw3, text="Danh Mục:", font=('arial 14 bold'), fg='black', bg='lightblue')
            # self.n4.place(x=10, y=90)

            self.droplist1 = OptionMenu(self.rightw333, c1, 'TAI', 'MŨI', 'HỌNG')
            self.droplist1.pack()

            self.menu = self.droplist1.nametowidget(self.droplist1.menuname)
            self.menu.configure(font=('arial 28 bold'))
            c1.set('HỌNG')

            self.droplist1.config(width=9, height=1, font=('arial 20 bold'))
            self.droplist1.place(x=5, y=40)

            self.add_ifmt = Button(self.rightw333, text="Cập Nhật", width=12, height=2, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.database_print111)
            self.add_ifmt.place(x=5, y=90)

            self.n4 = Label(self.rightw333, text="Phương Pháp Điều Trị:", font=('arial 14 bold'), fg='black',
                            bg='lightblue')
            self.n4.place(x=10, y=185)

            self.ad_j2 = Entry(self.rightw333, font=('arial 28 bold'), width=24)
            self.ad_j2.place(x=10, y=215)

            self.add_ifmj = Button(self.rightw333, text="Cập nhật", width=12, height=2, font=('arial 18 bold'),
                                   bg='orange',
                                   command=self.database_printnn1)
            self.add_ifmj.place(x=5, y=270)

            self.add_dltifmtjj = Button(self.rightw333, text="Xóa", width=16, height=2, font=('arial 18 bold'),
                                        bg='orange', command=self.Deletedata_NewWindow)
            self.add_dltifmtjj.place(x=25, y=375)
            self.add_dltifmtjj = Button(self.rightw333, text="Đóng", width=16, height=2, font=('arial 18 bold'),
                                        bg='orange', command=self.quit22)
            self.add_dltifmtjj.place(x=260, y=375)
            self.addrn = Label(self.rightw333, text="Đã thêm đủ thông tin! ", font=('arial 18 bold'), fg='black',
                               bg='white')
            self.addrn.place(x=70, y=460)

            # self.add_dltd = Button(self.rightw3, text="Đóng", width=14, height=2, font=('arial 20 bold'),
            #                        bg='orange', command=self.quit_print1)
            # self.add_dltd.place(x=5, y=400)
            scrollbary = Scrollbar(self.rightw222, orient=VERTICAL)
            scrollbarx = Scrollbar(self.rightw222, orient=HORIZONTAL)
            self.tree2 = ttk.Treeview(self.rightw222, columns=("Danh Mục", "Chẩn Đoán"),
                                      selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                      xscrollcommand=scrollbarx.set)
            scrollbary.config(command=self.tree2.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=self.tree2.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree2.heading('Danh Mục', text="Danh Mục", anchor=W)
            self.tree2.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
            self.tree2.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree2.column('#1', stretch=NO, minwidth=0, width=200)
            self.tree2.column('#2', stretch=NO, minwidth=0, width=0)
            self.tree2.pack()

            scrollbary = Scrollbar(self.rightw444, orient=VERTICAL)
            scrollbarx = Scrollbar(self.rightw444, orient=HORIZONTAL)
            self.tree4 = ttk.Treeview(self.rightw444, columns=("Danh Mục Chẩn Đoán", "Chỉ Định"),
                                      selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                      xscrollcommand=scrollbarx.set)
            scrollbary.config(command=self.tree4.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=self.tree2.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            self.tree4.heading('Danh Mục Chẩn Đoán', text="Danh Mục Chẩn Đoán", anchor=W)
            self.tree4.heading('Chỉ Định', text="Chỉ Định", anchor=W)
            self.tree4.column('#0', stretch=NO, minwidth=0, width=0)
            self.tree4.column('#1', stretch=NO, minwidth=0, width=0)
            self.tree4.column('#2', stretch=NO, minwidth=0, width=195)
            self.tree4.pack()

            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            cursor1 = conn.cursor()
            cursor.execute("SELECT * FROM `print_dt22`")
            fetch = cursor.fetchall()
            cursor1.execute("SELECT * FROM `print_jb22`")
            fetch1 = cursor1.fetchall()
            for data in fetch:
                self.tree2.insert('', 'end', values=(data))
            for data1 in fetch1:
                self.tree4.insert('', 'end', values=(data1))
            cursor.close()
            conn.close()
            conn = sqlite3.connect("db_member.db")
            cursor = conn.cursor()
            # addWindow.withdraw()
            # self.createNewWindow()


    def openfile(self):  # open the file\
        # namepk = self.adr2_p.get()
        # name_dt = self.doctor_p.get()
        # address_pk = self.n2_p.get()

        address_addrn = self.addrn_p.get()
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        if address_addrn == '':
            self.addrn = Label(self.rightw3, text="Điền đầy đủ thông tin! ", font=('arial 18 bold'), fg='blue',
                               bg='white')
            self.addrn.place(x=200, y=520)
        else:
            cursor.execute("DELETE FROM print_dtadd WHERE addressadd=1")
            cursor.execute('CREATE TABLE IF NOT EXISTS print_dtadd (name_pkadd TEXT,dt_nameadd TEXT)')
            cursor.execute('INSERT INTO print_dtadd (name_pkadd,dt_nameadd) VALUES(?,?)',
                           (address_addrn, address_addrn))
            self.addrn = Label(self.rightw3, text="Đã thêm biểu tượng   ! ", font=('arial 18 bold'), fg='blue',
                               bg='white')
            self.addrn.place(x=200, y=520)
            conn.commit()
            cursor.close()

    def createNewWindow(self, *args, **kwargs):
        # root.withdraw()

        newWindowaddf.update()
        newWindowaddf.deiconify()
        self.rightw222 = Frame(newWindowaddf, width=205, height=500, bg='lightblue')
        self.rightw222.pack(side=RIGHT)
        self.rightw444 = Frame(newWindowaddf, width=205, height=500, bg='lightyellow')
        self.rightw444.pack(side=RIGHT)
        self.rightw333 = Frame(newWindowaddf, width=540, height=500, bg='lightblue')
        self.rightw333.pack(side=LEFT)

        self.n3 = Label(self.rightw333, text="Danh Mục Chẩn Đoán:", font=('arial 14 bold'), fg='black', bg='lightblue')
        self.n3.place(x=10, y=10)

        self.ad_if2 = Entry(self.rightw333, font=('arial 28 bold'), width=16)
        self.ad_if2.place(x=188, y=39)

        # self.n4 = Label(self.rightw3, text="Danh Mục:", font=('arial 14 bold'), fg='black', bg='lightblue')
        # self.n4.place(x=10, y=90)

        self.droplist1 = OptionMenu(self.rightw333, c1, 'TAI', 'MŨI', 'HỌNG')
        self.droplist1.pack()

        self.menu = self.droplist1.nametowidget(self.droplist1.menuname)
        self.menu.configure(font=('arial 28 bold'))
        c1.set('HỌNG')

        self.droplist1.config(width=9, height=1, font=('arial 20 bold'))
        self.droplist1.place(x=5, y=40)

        self.add_ifmt = Button(self.rightw333, text="Cập Nhật", width=12, height=2, font=('arial 18 bold'), bg='orange',
                               command=self.database_print111)
        self.add_ifmt.place(x=5, y=90)

        self.n4 = Label(self.rightw333, text="Phương Pháp Điều Trị:", font=('arial 14 bold'), fg='black',
                        bg='lightblue')
        self.n4.place(x=10, y=185)

        self.ad_j2 = Entry(self.rightw333, font=('arial 28 bold'), width=24)
        self.ad_j2.place(x=10, y=215)

        self.add_ifmj = Button(self.rightw333, text="Cập nhật", width=12, height=2, font=('arial 18 bold'), bg='orange',
                               command=self.database_printnn1)
        self.add_ifmj.place(x=5, y=270)

        self.add_dltifmtjj = Button(self.rightw333, text="Xóa", width=16, height=2, font=('arial 18 bold'),
                                    bg='orange', command=self.Deletedata_NewWindow)
        self.add_dltifmtjj.place(x=25, y=375)
        self.add_dltifmtjj = Button(self.rightw333, text="Đóng", width=16, height=2, font=('arial 18 bold'),
                                    bg='orange', command=self.quit22)
        self.add_dltifmtjj.place(x=260, y=375)

        # self.add_dltd = Button(self.rightw3, text="Đóng", width=14, height=2, font=('arial 20 bold'),
        #                        bg='orange', command=self.quit_print1)
        # self.add_dltd.place(x=5, y=400)
        scrollbary = Scrollbar(self.rightw222, orient=VERTICAL)
        scrollbarx = Scrollbar(self.rightw222, orient=HORIZONTAL)
        self.tree2 = ttk.Treeview(self.rightw222, columns=("Danh Mục", "Chẩn Đoán"),
                                  selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                  xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree2.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree2.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree2.heading('Danh Mục', text="Danh Mục", anchor=W)
        self.tree2.heading('Chẩn Đoán', text="Chẩn Đoán", anchor=W)
        self.tree2.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree2.column('#1', stretch=NO, minwidth=0, width=200)
        self.tree2.column('#2', stretch=NO, minwidth=0, width=0)
        self.tree2.pack()

        scrollbary = Scrollbar(self.rightw444, orient=VERTICAL)
        scrollbarx = Scrollbar(self.rightw444, orient=HORIZONTAL)
        self.tree4 = ttk.Treeview(self.rightw444, columns=("Danh Mục Chẩn Đoán", "Chỉ Định"),
                                  selectmode="extended", height=250, yscrollcommand=scrollbary.set,
                                  xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree4.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree2.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree4.heading('Danh Mục Chẩn Đoán', text="Danh Mục Chẩn Đoán", anchor=W)
        self.tree4.heading('Chỉ Định', text="Chỉ Định", anchor=W)
        self.tree4.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree4.column('#1', stretch=NO, minwidth=0, width=0)
        self.tree4.column('#2', stretch=NO, minwidth=0, width=195)
        self.tree4.pack()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor1 = conn.cursor()
        cursor.execute("SELECT * FROM `print_dt22`")
        fetch = cursor.fetchall()
        cursor1.execute("SELECT * FROM `print_jb22`")
        fetch1 = cursor1.fetchall()
        for data in fetch:
            self.tree2.insert('', 'end', values=(data))
        for data1 in fetch1:
            self.tree4.insert('', 'end', values=(data1))
        cursor.close()
        conn.close()
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()


        # # root.withdraw()

    def add_to_bn(self, *args, **kwargs):
        # root.withdraw()


        addWindow.update()
        addWindow.deiconify()
        self.rightw2 = Frame(addWindow, width=550, height=600, bg='lightblue')
        self.rightw2.pack(side=RIGHT)
        self.rightw3 = Frame(addWindow, width=600, height=600, bg='lightblue')
        self.rightw3.pack(side=LEFT)

        self.adr2 = Label(self.rightw3, text="Phòng khám:", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.adr2.place(x=10, y=10)
        self.adr2_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
        self.adr2_p.place(x=150, y=10)

        self.doctor = Label(self.rightw3, text=" Bác sĩ :", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.doctor.place(x=10, y=85)

        self.doctor_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
        self.doctor_p.place(x=150, y=75)

        self.n2 = Label(self.rightw3, text="Địa chỉ:", font=('arial 16 bold'), fg='black', bg='lightblue')
        self.n2.place(x=10, y=155)

        self.n2_p = Entry(self.rightw3, font=('arial 20 bold'), width=26)
        self.n2_p.place(x=150, y=150)

        self.add_dt = Button(self.rightw3, text="Cập nhật", width=15, height=3, font=('arial 18 bold'), bg='orange',
                             command=self.database_print)
        self.add_dt.place(x=40, y=220)

        self.add_dltd = Button(self.rightw3, text="Xóa", width=15, height=3, font=('arial 18 bold'), bg='orange',
                               command=self.Deletedata_print)  # command=self.quit_print2)
        self.add_dltd.place(x=275, y=220)

        self.addrn = Label(self.rightw3, text="Icon Addr:", font=('arial 18 bold'), fg='black', bg='lightblue')
        self.addrn.place(x=10, y=360)

        self.addrn_p = Entry(self.rightw3, font=('arial 22 bold'), width=25)
        self.addrn_p.place(x=130, y=360)

        self.add_dl = Button(self.rightw3, text="Thêm Icon", width=15, height=3, font=('arial 18 bold'),
                             bg='orange', command=self.openfile)
        self.add_dl.place(x=35, y=410)
        self.add_dl = Button(self.rightw3, text="Đóng", width=15, height=3, font=('arial 18 bold'),
                             bg='orange', command=self.quit11)
        self.add_dl.place(x=260, y=410)

        self.scrollbarx = Scrollbar(self.rightw2, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.rightw2, orient=VERTICAL)
        self.tree1 = ttk.Treeview(self.rightw2, columns=("Id", "Phòng khám", "Bác sĩ", "Địa chỉ"),
                                  selectmode="extended",
                                  height=400, yscrollcommand=self.scrollbary.set,
                                  xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree1.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree1.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree1.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree1.column('#1', stretch=NO, minwidth=0, width=20)
        self.tree1.column('#2', stretch=NO, minwidth=0, width=180)
        self.tree1.column('#3', stretch=NO, minwidth=0, width=120)
        self.tree1.column('#4', stretch=NO, minwidth=0, width=80)

        self.tree1.pack()
        self.tree1.heading('Id', text="Id", anchor=W)
        self.tree1.heading('Phòng khám', text="Phòng khám", anchor=W)
        self.tree1.heading('Bác sĩ', text="Bác sĩ", anchor=W)
        self.tree1.heading('Địa chỉ', text="Địa chỉ", anchor=W)
        self.tree1.pack()

        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `print_dt`")
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree1.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def Deletedata_NewWindow(self):
        conn = sqlite3.connect("db_member.db")
        cursor = conn.cursor()
        for selected_item1 in self.tree2.selection():
            # print(selected_item1)  # it prints the selected row id
            cursor.execute("DELETE FROM print_dt22 WHERE name_pk22=?", (self.tree2.set(selected_item1, '#1'),))
            conn.commit()
            self.tree2.delete(selected_item1)
        for selected_item3 in self.tree4.selection():
            # print(selected_item3)  # it prints the selected row id
            cursor.execute("DELETE FROM print_jb22 WHERE name_j22=?", (self.tree4.set(selected_item3, '#1'),))
            conn.commit()
            self.tree4.delete(selected_item3)
        conn.commit()
        cursor.close()

    def quit(self):
       #  addWindow.destroy()
       #  #addWindow.deiconify()
       # # root.withdraw()
       # # newWindowaddf.update()
       #  newWindowaddf.destroy()
       # root.withdraw()

        root.withdraw()
        root.destroy()
        addWindow.destroy()

        # newWindowaddf.withdraw()
        # newWindowaddf.destroy()
        # root1.destroy()
        # root2.destroy
    def quit11(self):
        self.rightw2.destroy()
        self.rightw3.destroy()

        addWindow.withdraw()
        # root.deiconify()
        # root.update()
        # root1.destroy()
        # root2.destroy()
    def quit22(self):
        # root.deiconify()
        # root.update()
        self.rightw222.destroy()
        self.rightw444.destroy()
        self.rightw333.destroy()

        newWindowaddf.withdraw()
        # root.deiconify()
        # root.update()
        # root1.destroy()
        # root2.destroy()

    # def quit_print1(self):
    #
    #     tkinter.messagebox.showinfo("Success", "Thoát cài đặt danh mục")
    #     # root1.withdraw()
    #
    # def quit_print2(self):
    #     # root2.withdraw()
    #     tkinter.messagebox.showinfo("Success", "Thoát cài đặt biểu mẫu")
    #
    # def hide(self):
    #     root.withdraw()
    #
    # def show(self):
    #     root.update()
    #     root.deiconify()

    def create_pdf1(self):
        # Set up a logo
        conn = sqlite3.connect("db_member.db")
        conn.row_factory = sqlite3.Row
        for selected_item in self.tree.selection():
            print(selected_item)
        cur = conn.cursor()
        cur.execute("SELECT * FROM `member` WHERE id=?", (self.tree.set(selected_item, '#1'),))
        rows = cur.fetchall()
        for row in rows:
            row["id"]
        # webbrowser.open_new(r'doccument/%s.pdf' % ("a" + str(row["id"])))
        webbrowser.open_new(r'doccument/%s.pdf' % ("a" + str(row["id"])))


    def endoscopy(self):
        #         root.overrideredirect(False)
        #
        class Window2(QMainWindow):  # <===

            def __init__(self):
                super().__init__()
                self.anh1 = 1
                self.anh2 = 2
                self.anh3 = 3
                self.anh4 = 4
                self.anh5 = 5
                self.anh6 = 6
                self.cou = 0
                self.title = "Print Window"
                self.top = 0
                self.left = 0
                self.width = 1000
                self.height = 560

                self.listWidget = QtWidgets.QListWidget(self)
                self.listWidget.setGeometry(QtCore.QRect(680, 5, 300, 545))  # (2, 115, 213, 475))
                self.listWidget.setObjectName("ListWidgetItem")
                self.listWidget.setIconSize(QtCore.QSize(270, 180))
                self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
                self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)

                self.it = QtWidgets.QListWidgetItem(self.listWidget)
                self.it1 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it2 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it3 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it4 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it5 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it6 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it7 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it8 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it9 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it10 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it11 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it12 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it13 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it14 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it15 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it16 = QtWidgets.QListWidgetItem(self.listWidget)
                self.it17 = QtWidgets.QListWidgetItem(self.listWidget)
                conn = sqlite3.connect("db_member.db")
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("SELECT max(id) FROM member")
                rows = cur.fetchall()
                # INSERT
                # INTO
                # print_jb22(name_j22, dt_namej)
                # VALUES(?, ?)

                # cur2 = conn.cursor()
                # cur2.execute("SELECT name_j22 FROM print_jb22")
                # rows2 = cur2.fetchall()
                # for row2 in rows2:
                #     row2["name_j22"]
                #     # print("%s" % (row2["name_j22(1)"]))
                # # completer = QCompleter(row2["name_j22"])
                directory = "anh/"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                for row in rows:
                    # print("%s" % (row["max(id)"]))
                    row["max(id)"]

                font = QFont('Times', 16)

                self.it.setFont(font)
                self.it.setText("1  ")
                self.it1.setFont(font)
                self.it1.setText("2  ")
                self.it2.setFont(font)
                self.it2.setText("3  ")
                self.it3.setFont(font)
                self.it3.setText("4  ")
                self.it4.setFont(font)
                self.it4.setText("5  ")
                self.it5.setFont(font)
                self.it5.setText("6  ")
                self.it6.setFont(font)
                self.it6.setText("7  ")
                self.it7.setFont(font)
                self.it7.setText("8  ")
                self.it8.setFont(font)
                self.it8.setText("9  ")
                self.it9.setFont(font)
                self.it9.setText("10  ")
                self.it10.setFont(font)
                self.it10.setText("11  ")
                self.it11.setFont(font)
                self.it11.setText("12  ")
                self.it12.setFont(font)
                self.it12.setText("13  ")
                self.it13.setFont(font)
                self.it13.setText("14  ")
                self.it14.setFont(font)
                self.it14.setText("15  ")
                self.it15.setFont(font)
                self.it15.setText("16  ")
                self.it16.setFont(font)
                self.it16.setText("17  ")
                self.it17.setFont(font)
                self.it17.setText("18 ")

                self.TEXT = QtWidgets.QTextBrowser(self)
                self.TEXT.setGeometry(QtCore.QRect(100, 480, 450, 60))
                self.TEXT.setObjectName("TEXT")
                font1 = QFont('Times', 24)
                self.TEXT.setFont(font1)
                self.TEXT.setText('%s : png' % (
                            str(self.anh1) + ":" + str(self.anh2) + ":" + str(self.anh3) + ":" + str(
                        self.anh4) + ":" + str(self.anh5) + ":" + str(self.anh6)))

                self.it.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(1))))
                self.it1.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(2))))
                self.it2.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(3))))
                self.it3.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(4))))
                self.it4.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(5))))
                self.it5.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(6))))
                self.it6.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(7))))
                self.it7.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(8))))
                self.it8.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(9))))
                self.it9.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(10))))
                self.it10.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(11))))
                self.it11.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(12))))
                self.it12.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(13))))
                self.it13.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(14))))
                self.it14.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(15))))
                self.it15.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(16))))
                self.it16.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(17))))
                self.it17.setIcon(
                    QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(18))))

                self.pushButton = QPushButton("In Phiếu Khám", self)
                self.pushButton.setGeometry(QtCore.QRect(80, 360, 250, 100))
                self.pushButton.setToolTip("<h3>Start Print</h3>")

                # self.pushButton1 = QPushButton("Chọn Ảnh Thủ Công", self)
                # self.pushButton1.setGeometry(QtCore.QRect(250, 360, 200, 100))
                # self.pushButton1.setToolTip("<h3>Start Print</h3>")

                self.pushButton2 = QPushButton("Đóng", self)
                self.pushButton2.setGeometry(QtCore.QRect(332, 360, 250, 100))
                self.pushButton2.setToolTip("<h3>Close</h3>")

                font = QtGui.QFont()
                font.setPointSize(20)
                font1 = QtGui.QFont()
                font1.setPointSize(16)

                self.text2 = QtWidgets.QLabel("Chẩn Đoán : ", self)
                self.text2.setGeometry(QtCore.QRect(90, 20, 225, 50))
                self.text2.setFont(font1)
                self.text1 = QtWidgets.QLabel("Điều Trị : ", self)
                self.text1.setGeometry(QtCore.QRect(90, 125, 200, 50))
                self.text1.setFont(font1)

                self.text2 = QtWidgets.QLabel("Chỉ Định : ", self)
                self.text2.setGeometry(QtCore.QRect(90, 225, 200, 50))
                self.text2.setFont(font1)

                # names = ["Apple", "Alps", "Berry", "Cherry"]
                # completer = QCompleter(names)

                self.lineEdit = QtWidgets.QLineEdit(self)
                self.lineEdit.setGeometry(QtCore.QRect(70, 70, 530, 50))
                self.lineEdit.setObjectName("lineEdit")
                self.lineEdit.setPlaceholderText('chẩn đoán')
                # self.lineEdit.setCompleter(completer)
                self.lineEdit.setFont(font)

                self.completer = QCompleter()
                self.lineEdit.setCompleter(self.completer)
                self.model = QStringListModel()
                self.completer.setModel(self.model)

                self.lineEdit_2 = QtWidgets.QLineEdit(self)
                self.lineEdit_2.setGeometry(QtCore.QRect(70, 170, 530, 50))
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_2.setPlaceholderText('Phương pháp điều trị')
                self.lineEdit_2.setFont(font)

                self.completer_2 = QCompleter()
                self.lineEdit_2.setCompleter(self.completer_2)
                self.model_2 = QStringListModel()
                self.completer_2.setModel(self.model_2)

                self.lineEdit_3 = QtWidgets.QLineEdit(self)
                self.lineEdit_3.setGeometry(QtCore.QRect(70, 270, 530, 50))
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.lineEdit_3.setPlaceholderText('Chỉ định của bác sĩ')
                self.lineEdit_3.setFont(font)
                #  self.pushButton.move(275,420)
                self.pushButton.clicked.connect(self.create_pdf2)  # self.create_pdf2)
                # self.pushButton1.clicked.connect(self.window3)
                self.pushButton2.clicked.connect(self.winc)
                # self.listWidget.itemChanged.connect(self.call)
                self.listWidget.itemSelectionChanged.connect(self.on_change)
                # self.listWidget.itemClicked.connect(self.call)
                self.main_window()
                self.get_data()
                self.get_data1()

            def main_window(self):
                self.setWindowTitle(self.title)
                self.setGeometry(self.top, self.left, self.width, self.height)
                self.show()

            def get_data(self):
                conn = sqlite3.connect("db_member.db")
                c = conn.cursor()
                c.execute(" SELECT name_pk22 FROM print_dt22")
                results = c.fetchall()
                new_list = [i[0] for i in results]
                # print(new_list)  # Test print
                self.model.setStringList(new_list)  # From here up I was able to get the
                # code to work but there's no auto completion in the QLineEdit.

            def get_data1(self):
                conn = sqlite3.connect("db_member.db")
                cur2 = conn.cursor()
                cur2.execute("SELECT name_j22 FROM print_jb22")

                # print("%s" % (row2["name_j22(1)"]))
                # completer = QCompleter(row2["name_j22"])
                results = cur2.fetchall()
                new_list = [i[0] for i in results]
                # print(new_list)  # Test print
                self.model_2.setStringList(new_list)  # From here up I was able to get the
                # code to work but there's no auto completion in the QLineEdit.

            def on_change(self):
                self.cou = self.cou + 1

                inn = str([item.text() for item in self.listWidget.selectedItems()])
                # print(inn)
                k = inn[2:4]
                self.kk = int(k)
                # print(self.kk)
                # self.kk = int(k)
                if self.cou == 1:
                    self.anh1 = self.kk
                if self.cou == 2:
                    self.anh2 = self.kk
                if self.cou == 3:
                    self.anh3 = self.kk
                if self.cou == 4:
                    self.anh4 = self.kk
                if self.cou == 5:
                    self.anh5 = self.kk
                if self.cou == 6:
                    self.anh6 = self.kk
                self.TEXT.setText('%s.png' % (str(self.anh1) + ":" + str(self.anh2) + ":" + str(self.anh3) + ":" + str(
                    self.anh4) + ":" + str(self.anh5) + ":" + str(self.anh6)))

                if self.cou > 6:
                    self.cou = 0

                #     print(self.kk)
                # if self.kk==1:
                #     self.item.setCheckState(1)
                #     self.anh1=16

            # def call(self, qList):
            #     print(str(qList))
            #     index = self.listWidget.indexFromItem(qList)

            def winc(self):
                self.hide()

            # def call(self, qList):
            #     checkedItem = 0
            #     for index in range(self.listWidget.count()):
            #         if self.listWidget.item(index).checkState() == Qt.Checked:
            #             checkedItem += 1
            #     print(str(checkedItem))
            #
            #     imn = [str(item.text()) for item in self.listWidget.selectedItems()]
            #     print(imn)
            #     print(imn[5])
            #     #self.on_change()
            #     #self.on_change()

            def create_pdf2(self):
                # Set up a logo
                shost = self.lineEdit.text()
                shost2 = self.lineEdit_2.text()
                shost3 = self.lineEdit_3.text()

                conn = sqlite3.connect("db_member.db")
                conn.row_factory = sqlite3.Row
                cur = conn.cursor()
                cur.execute("SELECT max(id) FROM member")
                rows = cur.fetchall()
                for row in rows:
                    row["max(id)"]

                cur2 = conn.cursor()
                cur2.execute("SELECT name_pk FROM print_dt")
                cur3 = conn.cursor()
                cur3.execute("SELECT address FROM print_dt")
                cur4 = conn.cursor()
                cur4.execute("SELECT dt_name FROM print_dt")
                cur5 = conn.cursor()
                cur5.execute("SELECT * FROM `member`")
                cur6 = conn.cursor()
                cur6.execute("SELECT name_pkadd FROM print_dtadd")

                rows6 = cur6.fetchall()
                rows5 = cur5.fetchall()
                rows4 = cur4.fetchall()
                rows3 = cur3.fetchall()
                rows2 = cur2.fetchall()

                for row5 in rows5:
                    row5[6]
                for row2 in rows2:
                    row2["name_pk"]

                for row3 in rows3:
                    row3["address"]

                for row4 in rows4:
                    row4["dt_name"]

                for row6 in rows6:
                    row6["name_pkadd"]

                t = row2["name_pk"]
                t1 = row3["address"]
                t2 = "BS: " + row4["dt_name"]
                t3 = row6["name_pkadd"]

                pdf = FPDF()
                pdf.set_font("Arial", size=12)
                pdf.add_page()

                pdf.image(t3, 8, 6, 25)
                pdf.add_font('DejaVu', '', 'DejaVuSerif-Italic.ttf', uni=True)
                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(35)
                pdf.cell(0, 5, t, ln=1)
                pdf.set_font('DejaVu', '', 14)

                pdf.cell(70)
                pdf.cell(0, 10, t2, ln=1)
                pdf.set_font('DejaVu', '', 14)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(30)

                pdf.cell(0, 0, "ĐC:", ln=1)
                pdf.set_font('DejaVu', '', 12)
                pdf.set_text_color(0, 0, 0)
                pdf.cell(40)
                pdf.cell(0, 0, t1, ln=1)
                pdf.set_draw_color(0, 0, 0)
                pdf.set_line_width(1)
                pdf.line(30, 30, 180, 30)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(255, 0, 40)
                pdf.cell(35)
                pdf.cell(0, 5, ' ', ln=1)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(255, 0, 40)
                pdf.cell(35)
                pdf.cell(0, 15, 'PHIẾU KHÁM NỘI SOI TAI-MŨI-HỌNG', ln=1)

                pdf.set_font('DejaVu', '', 12)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(75)
                pdf.cell(0, 0, 'Số Phiếu : ' + str(row5[0]), ln=1)

                pdf.set_font('DejaVu', '', 16)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.cell(5)
                pdf.cell(0, 0, 'Tên bệnh nhân : ' + str(row5[1]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Tuổi : ' + str(row5[4]), ln=1)
                pdf.cell(135)
                pdf.cell(0, 0, 'Giới tính : ' + str(row5[6]), ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)
                pdf.cell(5)
                pdf.cell(0, 0, 'Địa chỉ : ' + str(row5[3]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Số bảo hiểm : ' + str(row5[7]), ln=1)
                pdf.cell(135)
                pdf.cell(0, 0, 'Nghề nghiệp : ' + str(row5[2]), ln=1)

                pdf.set_font('DejaVu', '', 10)
                pdf.set_text_color(0, 70, 255)
                pdf.cell(0, 8, ' ', ln=1)
                pdf.cell(5)
                pdf.cell(0, 0, 'Triệu chứng : ' + str(row5[5]), ln=1)
                pdf.cell(85)
                pdf.cell(0, 0, 'Điện thoại: ' + str(row5[8]), ln=1)

                pdf.set_font('DejaVu', '', 14)
                pdf.cell(0, 15, ' ', ln=1)
                pdf.cell(70)
                pdf.cell(0, 0, 'HÌNH ẢNH NỘI SOI ', ln=1)
                #
                file_name = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh1)))
                file_name1 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh2)))
                file_name2 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh3)))
                file_name3 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh4)))
                file_name4 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh5)))
                file_name5 = ('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.anh6)))
                #

                pdf.set_font('DejaVu', '', 16)
                pdf.cell(0, 130, ' ', ln=1)
                pdf.cell(60)
                pdf.cell(0, 0, 'MÔ TẢ KẾT QUẢ NỘI SOI ', ln=1)
                pdf.set_font('DejaVu', '', 12)
                pdf.cell(0, 5, ' ', ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Chẩn đoán : %s' % (shost), ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Điều trị : %s' % (shost2), ln=1)
                pdf.cell(12)
                pdf.cell(0, 7, 'Chỉ định bác sĩ : %s' % (shost3), ln=1)

                pdf.set_x(120)
                pdf.cell(0, 14, " Ngày " + str(today.day) + " Tháng " + str(today.month) + " Năm " + str(today.year),
                         ln=1)
                pdf.set_x(145)
                pdf.cell(0, 6, 'Bác sĩ : ', ln=1)
                pdf.cell(0, 15, ' ', ln=1)
                pdf.set_x(126)
                pdf.cell(0, 0, t2, ln=1)
                # if file_name == '' or file_name1 == True or file_name2 == True or file_name3 == True or file_name4 == True or file_name5 == True :
                if os.path.exists(file_name) and os.path.exists(file_name1) and os.path.exists(
                        file_name2) and os.path.exists(file_name3) and os.path.exists(file_name4) and os.path.exists(
                    file_name5):
                    pdf.image(file_name, 12, 90, 60)
                    pdf.image(file_name1, 12, 150, 60)
                    pdf.image(file_name2, 74, 90, 60)
                    pdf.image(file_name3, 74, 150, 60)
                    pdf.image(file_name4, 136, 90, 60)
                    pdf.image(file_name5, 136, 150, 60)
                # pdf.image(file_name, 12, 90, 60)
                # pdf.image(file_name1, 12, 150, 60)
                # pdf.image(file_name2, 74, 90, 60)
                # pdf.image(file_name3, 74, 150, 60)
                # pdf.image(file_name4, 136, 90, 60)
                # pdf.image(file_name5, 136, 150, 60)

                directory1 = "doccument/"
                if not os.path.exists(directory1):
                    os.makedirs(directory1)
                pdf.output('doccument/%s.pdf' % ("a" + str(row["max(id)"])))
                webbrowser.open_new(r'doccument/%s.pdf' % ("a" + str(row["max(id)"])))
                #                 pdf.output('doccument/%s.pdf' % ("a" + str(row["max(id)"])))
                #                 webbrowser.open_new(r'doccument\%s.pdf' % ("a" + str(row["max(id)"])))
                conn.commit()
                cur.close()

                # self.winc()

        class video(QtWidgets.QDialog, Ui_Form):

            def __init__(self):
                #                 root.overrideredirect(False)
                root.withdraw()
                super().__init__()
                self.value = 0  # ---
                self.value1 = 0
                self.value2 = 0
                self.valueh = 5
                self.valuem = 11
                self.valuea = 1
                self.setupUi(self)  # ++
                self.CAPTURE.clicked.connect(self.capture_image)
                self.NEXT_3.clicked.connect(self.window2)

                # # adding items to the combo box
                # self.available_cameras = QCameraInfo.availableCameras()
                self.camera_selector.addItem("  CAMERA USB3.0")
                # self.camera_selector.add Items([camera.description()
                #                                for camera in self.available_cameras])
                self.camera_selector1.addItem("  Chụp Thủ Công ")
                self.camera_selector1.addItem("  Chụp Tự Động")
                self.camera_selector.currentIndexChanged.connect(self.select_camera)
                # self.camera_selector.stateChanged.connect(self.select_camera)

                self.NEXT_7.clicked.connect(self.w1)
                self.imgLabel.setScaledContents(True)
                self.cap = None  # -capture <-> +cap
                self.timer = QtCore.QTimer(self, interval=5)
                self.timer.timeout.connect(self.update_frame)
                self._image_counter = 0
                self.start_webcam()
                self.saveTimer = QTimer()

                # self.listWidget.itemChanged.connect(self.call)
                # self.listWidget.itemSelectionChanged.connect(self.on_change)
                # self.item.clicked.connect(self.w1)
                # self.item.setCheckState(True)
                # self.TEXT.setText.setText("True" if self.item1.setCheckState() else "False")

            @QtCore.pyqtSlot()
            def start_webcam(self):
                if self.cap is None:
                    self.cap = cv2.VideoCapture(0)
                    # self.imgLabel.setText("No Single")
                self.timer.start()
                font = QFont('Times', 42)
                self.imgLabel.setFont(font)
                self.imgLabel.setText("No Single : Kiểm Tra Tín Hiệu !")

                # else:
                # self.imgLabel.setText("No Single")

            @QtCore.pyqtSlot()
            def select_camera(self):

                print()

            def update_frame(self):
                ret, image = self.cap.read()
                # Define the codec and create VideoWriter object
                # image = imutils.resize(image, width=320, height=256)
                # time.sleep(2.0)
                if ret == True:
                    # image =cv2.resize(image, (320, 256))
                    image = cv2.resize(image, (960, 540))
                    # image = cv2.flip(image, 1)
                    # frame1 = cv2.resize(image, (416, 416))
                    frame2 = cv2.resize(image, (200, 150))
                    self.displayImage(image, True)
                else:
                    self.cap.release()

            @QtCore.pyqtSlot()
            def capture_image(self):

                flag, frame = self.cap.read()

                if flag == True and self.value1 < 18:
                    frame = imutils.resize(frame, width=240, height=170)
                    self.value1 = self.value1 + 1
                    conn = sqlite3.connect("db_member.db")
                    conn.row_factory = sqlite3.Row
                    cur = conn.cursor()
                    cur.execute("SELECT max(id) FROM member")
                    rows = cur.fetchall()
                    directory = "anh/"
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    for row in rows:
                        row["max(id)"]
                    cv2.imwrite('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(self.value1)), frame)
                    # self.TEXT.setText('your Image have been Saved')
                    self.label = QLabel(self)

                    self.it.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(1))))
                    self.it1.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(2))))
                    self.it2.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(3))))
                    self.it3.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(4))))
                    self.it4.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(5))))
                    self.it5.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(6))))
                    self.it6.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(7))))

                    self.it7.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(8))))
                    self.it8.setIcon(QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(9))))
                    self.it9.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(10))))
                    self.it10.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(11))))
                    self.it11.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(12))))
                    self.it12.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(13))))
                    self.it13.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(14))))
                    self.it14.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(15))))
                    self.it15.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(16))))
                    self.it16.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(17))))
                    self.it17.setIcon(
                        QtGui.QIcon('anh/%s.png' % ("a" + str(row["max(id)"]) + "a" + str(18))))
                    # self.TEXT.setText(str(row["max(id)"]) + label+ str(self.value))
                    self.TEXT.setText('anh/%s.png' % (self.value1))

                if flag == False:
                    font = QFont('Times', 42)
                    self.imgLabel.setFont(font)
                    self.imgLabel.setText("No Single : Kiểm Tra Tín Hiệu !")

                # else:
                # font = QFont('Times', 42)
                # self.imgLabel.setFont(font)
                # self.imgLabel.setText("No Single : Kiểm Tra Tín Hiệu !")

            def window2(self):  # <===
                self.w = Window2()
                self.w.show()
                # self.w1()

            def displayImage(self, img, window=True):
                qformat = QtGui.QImage.Format_Indexed8
                if len(img.shape) == 3:
                    if img.shape[2] == 4:
                        qformat = QtGui.QImage.Format_RGBA8888
                    else:
                        qformat = QtGui.QImage.Format_RGB888
                outImage = QtGui.QImage(img, img.shape[1], img.shape[0], img.strides[0], qformat)
                outImage = outImage.rgbSwapped()
                if window:
                    self.imgLabel.setPixmap(QtGui.QPixmap.fromImage(outImage))

            def w1(self):
                window.close()
                self.cap.release()
                root.update()
                root.deiconify()

        window = video()
        window.setGeometry(0, 0, 1024, 570)
        #         window.overrideredirect(True)
        window.show()

        try:
            sys.exit(app.exec_())
        except:
            logic1 = 1


app = QApplication(sys.argv)
# root.overrideredirect(True)root.overrideredirect(True)
root.geometry("1024x600+0+0")
b = Application(root)
root.mainloop()


