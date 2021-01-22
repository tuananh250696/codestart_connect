from tkinter import *
import re
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

        self.adr_id = Entry(self.left, font=('arial 20 bold'), width=40,fg='red')
        self.adr_id.place(x=60, y=100)

        self.keymail = Label(self.left, text="Địa chỉ mail:", font=('arial 12 bold'), fg='black',
                                 bg='lightblue')
        self.keymail.place(x=50, y=150)
        self.adr_mail = Entry(self.left, font=('arial 20 bold'), width=40)
        self.adr_mail.place(x=60, y=210)

        self.keyacticett = Label(self.left, text="Mã KEY:", font=('arial 12 bold'), fg='black',
                                 bg='lightblue')
        self.keyacticett.place(x=50, y=260)
        # self.adr_actice = Entry(self.left, font=('arial 20 bold'), width=40)
        # self.adr_actice.place(x=60, y=310)
        self.adr_actice = Text(root, height=1,width=40,bg="light yellow", font=('arial 20 bold'), fg='red')
        self.adr_actice.place(x=60, y=310)
        # button
        self.bt_st_catalog = Button(self.left, text="TẠO MÃ ACTICE", width=20, height=4, font=('arial 14 bold'),
                                    bg='orange',command=self.Take_input)
        self.bt_st_catalog.place(x=200, y=420)

        self.bt_exit1 = Button(self.left, text="Đóng", width=20, height=4, font=('arial 14 bold'), bg='orange',command=self.quit)
        self.bt_exit1.place(x=480, y=420)
        # self.getserial()
        #print(self.getserial())
        #self.adr_actice.insert(END,self.getserial())
        hh1 = str('A88dH5e8867'+self.getserial())
        #self.adr_id.insert(END,hh1)
    def quit(self):
        root.withdraw()
        root.destroy()

    def Take_input(self):
        #name_dtn1 = self.adr_id.get()
        # self.adr_actice.delete(0, END)
        h1 = 'A88dH5e8867'+self.getserial()
        num1 = re.sub(r'\D', "", h1)
        name_dtn1 = self.getserial()
        nux=int(num1)
        n =  len(name_dtn1) * nux
        num = re.sub(r'\d', "", h1)
        h22= str(n)+str(num)
        
        self.adr_actice.insert(END,h22)

        # INPUT = inputtxt.get("1.0", "end-1c")
        # print(INPUT)
        # if (INPUT == "120"):
        #     Output.insert(END, 'Correct')
        # else:
        #     Output.insert(END, "Wrong answer")
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
root.geometry("1024x600+0+0")
b = Application(root)
root.mainloop()
