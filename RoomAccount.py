'''
Hello i  am Monu Saini (Tenali)
Hey i am Creating a software 
This Software will be mantain the expance of room and with room partners



'''
from datetime import datetime, time
from sqlite3.dbapi2 import SQLITE_DELETE, enable_shared_cache
from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkinter.font import ROMAN
from PIL import ImageTk,Image
from tkcalendar import Calendar


class ROOM():
    
    # Creating login Frame
    def Login(self):
        F6 = Frame(root,width=550,height=350,bg='crimson')
        # must be flat, groove, raised, ridge, solid, or sunken

        room = Label(F6,text='Welcome to Tenali Room Account',font=('Algerian',20),bg='crimson',fg='yellow',relief='ridge')
        room.place(x=40,y=5)
       
        UEN = StringVar()
        UPN = StringVar()
        f1 = Frame(F6,width=270,height=140,bg='gray',)
        l1 = Label(f1,text='Username: ',font=('Algerian',14),bg='gray',fg='white',relief='ridge')
        l1.place(x=0,y=10)       
        l2= Label(f1,text='Password: ',font=('Algerian',14),bg='gray',fg='white',relief='ridge')
        l2.place(x=0,y=65)

        E1 = Entry(f1,font=('Arial',15),fg='green',width=13,textvariable=UEN,relief='groove')
        E1.place(x=120,y=10)

        E2 = Entry(f1,font=('Arial',15),fg='green',width=13,show='*',textvariable=UPN,relief='groove')
        E2.place(x=120,y=65)

        def CheckLogin():
            a=0
            conn=sqlite3.connect('doc/test.db')
            query = "SELECT * FROM todo;"
            # r = conn.execute(query,())
            for item in conn.execute(query,()):
               
                if E1.get() in item and E2.get() in item:
                    messagebox.showinfo('WELCOME',"Login Successfully ")
                    a = 1

            if a==1:
            
            # if E1.get()==user and E2.get()==pas:
               
                UEN.set("")
                UPN.set("")
                Renter.Choice()
            elif E1.get()=="" and E2.get()=="":
                messagebox.showinfo('LogIn',"Please..! Enter Username and Password")
            elif E1.get()=="":
                messagebox.showinfo('LogIn',"Please..! Enter Username")
            elif E2.get()=="":
                messagebox.showinfo('LogIn',"Please..! Enter Password")

            else:
                messagebox.showinfo('LogIn',"Username and Password are Incorrect\nPlease.. Enter vailid Details")


        Button1 =Button(f1,cursor="hand2",relief='ridge',text='LogIn',command=CheckLogin,font=("Georgia",10),fg='blue',activeforeground='blue',activebackground='silver')
        Button1.place(x=220,y=110)
        Button2 =Button(root,cursor="hand2",relief='ridge',text='change password',command=Renter.changepass,font=("Georgia",7),fg='blue',activeforeground='blue',activebackground='silver')
        Button2.place(x=465,y=330)

        backButton = Button(root,cursor="hand2",relief='ridge',text='<=',bg='crimson',fg='yellow',activebackground='red',font=("",10),command=Renter.LogReg)
        backButton.place(x=0,y=330)
        
        f1.place(x=130,y=110)
        F6.place(x=0,y=0)

    # Creatinng Collender 
    def GetDate(self):
        F4 = Frame(root,width=550,height=350,bg='gray')
        now = datetime.now() # Use now() to access the current date and time   

        self.travel=[]
        self.travel.insert(0, now.strftime("%d"))
        self.travel.insert(1,now.strftime("%m"))
        self.travel.insert(2,now.strftime("%Y"))
        self.cal = Calendar(F4, selectmode = 'day',
                    year = int(self.travel[2]),
                    month = int(self.travel[1]),
                    day = int(self.travel[0])
                    )

        self.cal.pack(pady = 20)

        def grad_date():
            global number
            self.date.config(text = "Selected Date is: " + self.cal.get_date())
            g = self.cal.get_date().split('/')
            h = self.cal.get_displayed_month()
            v= f"{g[1]}/{g[0]}/{h[1]}"
            self.date = v
            self.Byna = self.Byname.get()
            self.prname = self.proname.get()
            self.prwate = self.prowate.get()
            self.prprice = self.proprice.get()
           
            self.prodate.set(self.cal.get_date())
            number = 2
            Renter.SetProduct()

        

        # Add Button and Label
        Button(F4,cursor="hand2", text = "Get Date",
            command = grad_date).pack(pady = 20)

        self.date = Label(F4, text = "")
        self.date.pack(pady = 20)
        F4.place(x=0,y=0)
    
    def Choice(self):
        F5 = Frame(root,width=550,height=350,bg='#094e42')
        root.geometry('550x350')
        # must be flat, groove, raised, ridge, solid, or sunken
        room = Label(F5,relief="ridge",border=3,text='Welcome to Tenali Room Account',font=('Algerian',20,UNDERLINE,'bold'),fg='white',bg='#094e42')
        room.place(x=23,y=5)
       
        Button3 =Button(F5,text='Set Product',cursor="hand2",relief='sunken',font=('Georgia',15,UNDERLINE,'bold'),bg='#094e42',fg='crimson',command=Renter.SetProduct)
        Button3.place(x= 80,y=100)

        Button4 =Button(F5,text='Get Record',cursor="hand2",relief='sunken',font=('Georgia',15,UNDERLINE,'bold'),bg='#094e42',fg='crimson',padx=4,command=Renter.GetRecord)
        Button4.place(x= 80,y=170)

        Button5 =Button(F5,text='Set Travel',cursor="hand2",relief='sunken',font=('Georgia',15,UNDERLINE,'bold'),bg='#094e42',fg='crimson',command=Renter.SetTraveling)
        Button5.place(x= 330,y=100)

        Button6 =Button(F5,text='Get Travel',cursor="hand2",relief='sunken',font=('Georgia',15,UNDERLINE,'bold'),bg='#094e42',fg='crimson',padx=1,command=Renter.GetTravel)
        Button6.place(x= 330,y=170)

        Button7 =Button(F5,text='By Name',cursor="hand2",relief='sunken',font=('Georgia',15,UNDERLINE,'bold'),bg='#094e42',fg='crimson',padx=13,command=Renter.FindbyName)
        Button7.place(x= 80,y=240)

        Button7 =Button(F5,text='Collage ',cursor="hand2",relief='sunken',font=('Georgia',15,UNDERLINE,'bold'),bg='#094e42',fg='crimson',padx=13,command=Renter.Collage)
        Button7.place(x= 330,y=240)


        F5.place(x=0,y=0)

        backButton = Button(F5,text='LoGOuT',relief='ridge',cursor="hand2",bg='#094e42',fg='yellow',activebackground='red',font=("",10),command=Renter.Login)
        backButton.place(x=0,y=325)
        conn=sqlite3.connect('doc/RoomAccount.db')
        querys = "SELECT Price FROM ins;"
        ammount = 0
        for items in conn.execute(querys,()):
            ammount = ammount+int(items[0])
        conn=sqlite3.connect('doc/traveling.db')
        querys = "SELECT ammount FROM tra;"
        
        for items in conn.execute(querys,()):
            ammount = ammount+int(items[0])

        expence = Label(F5,text=f"Total Expence ₹: {ammount}",font=('Georgia',10),fg='white',bg='#094e42',relief='ridge',padx=20)
        expence.place(x=350,y=326)
       
    def Collage(self):
        messagebox.showinfo('collage','Collage section is not developed \nmust be developed within 2 days\nPlease... Waite')
    # Linsting Record 
    def GetRecord(self):
        F3 = Frame(root,width=570,height=350,bg='blue')
        backButton = Button(F3,cursor="hand2",text='<=',bg='blue',fg='yellow',activebackground='blue',font=("",10),command=Renter.Choice)
        backButton.place(x=0,y=325)
        l7 = Label(F3,text=f"Product Name\tDate\t          Buyer Name\t   Quantity                price ",bg='blue',font=('Copperplate Gothic Bold',10),fg='yellow')
        l7.place(x=10,y=40)
        L9 = Label(F3,text=f'Tenali Group Total Expance',font=("Algerian",20),fg="white",bg='#3D1C02',padx=82,relief='raised')
        L9.place(x=0,y=0)
        conn=sqlite3.connect('doc/RoomAccount.db')
        querys = "SELECT Price FROM ins;"
        ammount = 0
        for items in conn.execute(querys,()):
            ammount = ammount+int(items[0])

        L9 = Label(F3,text=f'ToTaL                                        {ammount}',font=("Algerian",15),fg="white",bg='blue')
        L9.place(x=90,y=322)
        conn=sqlite3.connect('doc/RoomAccount.db')
        query = "SELECT * FROM ins;"
        
        root.geometry('570x350')
        scroll = Scrollbar(F3)
        scroll.place(x=552,y=70,height=250)

        L8 = Text(root,width=61,height=13,border=1,font=('Arial',13),yscrollcommand=scroll.set,bg='blue',fg='white')
        L8.place(x=0,y=70)
        scroll.config(command=L8.yview)

        for v,item in enumerate( conn.execute(query,())):
        
            a=1
            L8.insert(1.0,f"{v+1}.  {item[0]}\t\t{item[1]}\t      {item[2]}\t\t     {item[3]}\t\t{item[4]}\n")
            
            L9.update()
        conn.close()
        L8.config(state=DISABLED)
        F3.place(x=0,y=0)
   
#    Geting product details from user
    def SetProduct(self):
        global number
    
        
        def Import():
            if self.E3.get()=='' or self.E4.get()=='' or self.E5.get()=='' or self.E6.get()=='':
                messagebox.showinfo('LogIn','Please.. Enter Details')
            elif self.E3.get()!='' and self.E4.get()!='' and self.E5.get()!='' or self.E6.get()!='':
                conn=sqlite3.connect('doc/RoomAccount.db')
                conn.execute('''CREATE TABLE IF NOT EXISTS ins(
                Product_Name TEXT NOT NULL,
                Buy_date TEXT NOT NULL,
                byer_name TEXT NOT NULL,
                Wate TEXT NOT NULL,
                Price TEXT NOT NULL
               
                
                );''')
                query = "INSERT INTO ins(Product_Name,Buy_date,byer_name,wate,Price)  VALUES (?,?,?,?,?);"
                conn.execute(query,(self.E3.get().capitalize(),self.E4.get().capitalize(),self.E5.get().capitalize(),self.E6.get(),self.E7.get()))
                conn.commit()
                conn.close()

                # with open('Room_Accound.txt','a') as I:
                #     I.write(str(f"{self.E3.get()}\t{self.E4.get()}\t{self.E5.get()}\t{self.E6.get()}\n"))
                self.proname.set("")
                self.prodate.set("")
                self.Byname.set("")
                self.prowate.set("")
                self.proprice.set("")
                messagebox.showinfo('LogIn','Details are successfully Imported')
            else:
                messagebox.showinfo('LogIn','Invailid Details')
            


        self.proname = StringVar()
        self.prodate = StringVar()
        self.Byname = StringVar()
        self.prowate = StringVar()
        self.proprice = StringVar()
        F2 = Frame(root,width=570,height=350,bg='crimson')
       
        backButton = Button(F2,cursor="hand2",text='<=',bg='crimson',fg='yellow',activebackground='red',font=("",10),command=Renter.Choice)
        backButton.place(x=0,y=330)
        l0 = Label(F2,text='Enter Product Details here',font=('Algerian',20),fg='lime',bg='crimson')
        l0.place(x=75,y=0)

        l3 = Label(F2,text='product Name:',font=('Algerian',15),fg='yellow',bg='crimson')
        l3.place(x=50,y=80)

        l4 = Label(F2,text='product Date:',font=('Algerian',15),fg='yellow',bg='crimson')
        l4.place(x=50,y=130)

        l5 = Label(F2,text='Buyer Name:',font=('Algerian',15),fg='yellow',bg='crimson')
        l5.place(x=50,y=180)

        l6 = Label(F2,text=' Quantity:',font=('Algerian',15),fg='yellow',bg='crimson')
        l6.place(x=50,y=230)
        l7 = Label(F2,text='product price:',font=('Algerian',15),fg='yellow',bg='crimson')
        l7.place(x=50,y=280)

        self.E3 = Entry(F2,font=('Arial',15),fg='green',width=13,textvariable=self.proname)
        self.E3.place(x=230,y=80)

        self.E4 = Entry(F2,font=('Arial',15),fg='green',width=13,textvariable=self.prodate)
        self.E4.place(x=230,y=130)
        Button0 = Button(F2,cursor="hand2", text = "^",command = Renter.GetDate,bg='white')
        Button0.place(x=360,y=130)


        self.E5 = Entry(F2,font=('Arial',15),fg='green',width=13,textvariable=self.Byname)
        self.E5.place(x=230,y=180)

        self.E6 = Entry(F2,font=('Arial',15),fg='green',width=13,textvariable=self.prowate)
        self.E6.place(x=230,y=230)

        self.E7 = Entry(F2,font=('Arial',15),fg='green',width=13,textvariable=self.proprice)
        
        self.E7.place(x=230,y=280)

        if number==2:
            def Insert():
                self.proname.set(self.prname)
                self.prodate.set(self.date)
                self.Byname.set(self.Byna)
                self.prowate.set(self.prwate)
                self.proprice.set(self.prprice)
                
            Insert()
            
        Button2 =Button(F2,text='IMPORT',cursor="hand2",font=('Georgia',10,'bold'),bg='yellow',fg='crimson',command=Import)
        
        Button2.place(x= 470,y=320)

        F2.place(x=0,y=0)
    
    def changepass(self):
        self.oldpass = StringVar()
        self.newpass = StringVar()
        self.confirm = StringVar()
        F6 = Frame(root,width=550,height=350,bg='#008080')
        l14 = Label(F6,text='Forgote Password Here',font=('Algerian',20,UNDERLINE),fg='lime',bg='#008080',relief='ridge',padx=110)
        l14.place(x=0,y=0)
        
        # must be flat, groove, raised, ridge, solid, or sunken

        l9 = Label(F6,text='old password:',font=('Algerian',15),fg='white',bg='#008080',relief='sunken')
        l9.place(x=50,y=80)
        
        l10 = Label(F6,text='New Password:',font=('Algerian',15),fg='white',bg='#008080',relief='sunken')
        l10.place(x=50,y=130)

        l11 = Label(F6,text='Confirm Macth:',font=('Algerian',15),fg='white',bg='#008080',relief='sunken')
        l11.place(x=50,y=180)

        self.E12 = Entry(F6,font=('Arial',15),fg='green',width=13,textvariable=self.oldpass,relief='ridge',border=2)
        self.E12.place(x=230,y=80)

        self.E13 = Entry(F6,font=('Arial',15),fg='green',width=13,textvariable=self.newpass,relief='ridge',border=2)
        self.E13.place(x=230,y=130)

        self.E14 = Entry(F6,font=('Arial',15),fg='green',width=13,textvariable=self.confirm,relief='ridge',border=2)
        self.E14.place(x=230,y=180)

        def Confirm():
            conn=sqlite3.connect('doc/test.db')
            query = "SELECT Passd FROM todo;"
            # r = conn.execute(query,())
            for item in conn.execute(query,()):
                self.oldpassword = item[0]
            if self.oldpassword!=self.oldpass.get():
                messagebox.showerror('Forgote Password','Old Password is Incorrect\nPlease... Enter vailid password')
            if self.newpass.get()!= self.confirm.get():
                self.E14['fg']= 'red'
                messagebox.showerror('Forgote Password','Password Mismacth\nPlease.. Enter same Password')
            self.E14['fg']= 'green'
            if self.oldpass.get()==self.oldpassword and self.newpass.get()==self.confirm.get():
                conn=sqlite3.connect('doc/test.db')
                solve = "SELECT Passd FROM ins;"
                for item in conn.execute(query,()):
                    self.oldpassword = item[0]
                update = "UPDATE todo SET Passd = ?;"
                conn.execute(update,(self.newpass.get(),))
                conn.commit()
                conn.close()
        



                
                messagebox.showinfo('Forgote Password','Password is Successfully Changed')
                self.oldpass.set("")
                self.newpass.set("")
                self.confirm.set("")


        Button4 = Button(F6,cursor="hand2",text='Change',font=('Algerian',10),command=Confirm,bg='#008080',fg='white',relief='solid',border=2)
        Button4.place(x=480,y=320)
        backButton = Button(F6,cursor="hand2",text='<=',relief='ridge',bg='#008080',fg='yellow',activebackground='red',font=("",10),command=Renter.Login)
        backButton.place(x=0,y=330)


        F6.place(x=0,y=0)

    def Registration(self):
        self.PartDate = StringVar()
        global a 
        
        def GetDate():
            self.todaydate=[]
            from datetime import date  
            now = datetime.now() # Use now() to access the current date and time   
            self.todaytime= now.strftime(" %I:%M:%S")
            
            self.todaydate.insert(0, now.strftime("%d"))
            self.todaydate.insert(1,now.strftime("%m"))
            self.todaydate.insert(2,now.strftime("%Y"))

            F4 = Frame(root,width=550,height=350,bg='gray')

            self.cal = Calendar(F4, selectmode = 'day',
                        year = int(self.todaydate[2]),
                        month = int(self.todaydate[1]),
                        day = int(self.todaydate[0])
                    )

            self.cal.pack(pady = 20)

            def grad_date():
               
                global a
                if self.cal.get_date():
                    self.Date.config(text = "Selected Date is: " + self.cal.get_date())
                    self.Date = self.cal.get_date()
                    self.year = self.cal.get_displayed_month()
                
                    self.Date =self.Date.split('/')
                    d = self.Date[1]
                    f = self.Date[2]
                    self.Date.remove(d)
                    self.Date.remove(f)

                    self.Date.insert(0,d)
                    self.Date.insert(2,self.year[1])
                    self.Date = f"{self.Date[0]}/{self.Date[1]}/{self.Date[2]}"
                    self.PartDate.set(self.Date)
                    self.part = self.DT.get()
                    a= 2
                    Renter.Registration()

            # Add Button and Label
            Button(F4,cursor="hand2", text = "Get Date",
                command = grad_date).pack(pady = 20)

            self.Date = Label(F4, text = "")
            self.Date.pack(pady = 20)
            F4.place(x=0,y=0)

        F6  = Frame(root,width=550,height=350,bg='crimson')
        backButton = Button(F6,cursor="hand2",text='Next',bg='crimson',fg='yellow',activebackground='red',font=("Colonna MT",15),command=Renter.Partname)
        backButton.place(x=492,y=312)

        l0 = Label(F6,text='Welcome to Tenali Room Group',font=('Algerian',20),fg='lime',bg='crimson')
        l0.place(x=55,y=0)

        l3 = Label(F6,text='Select Partners:',font=('Algerian',15),fg='yellow',bg='crimson')
        l3.place(x=50,y=110)

        l4 = Label(F6,text='Selct Date:',font=('Algerian',15),fg='yellow',bg='crimson')
        l4.place(x=50,y=170)

        self.DT =StringVar()
        # self.a=1
        list = (1,2,3,4,5)
        self.E3 = ttk.Combobox(F6, width = 8,values=list,foreground='green', textvariable = self.DT,font=("Algerian",10))
        
        self.E3.place(x=250,y=110)

        self.E4 = Entry(F6,font=('Arial',15),fg='green',width=13,textvariable=self.PartDate)
        self.E4.place(x=230,y=170)
        if a==2:
            self.DT.set(self.part)
            self.PartDate.set(self.Date)

        Button0 = Button(F6, text = "^",cursor="hand2",command = GetDate,bg='white')
        Button0.place(x=360,y=170)
        backButton = Button(root,text='<=',cursor="hand2",bg='crimson',fg='yellow',activebackground='red',font=("",10),command=Renter.LogReg)
        backButton.place(x=0,y=325)
        
        F6.place(x=0,y=0)
 
    def Partname(self):
        if self.DT.get()=="" or self.PartDate.get()=="":
            messagebox.showinfo('Registration',"Please.. Select The Details\nWe can some do after select the Details")
        else:
            F7 = Frame(root,width=550,height=350,bg='crimson')
            def GetNames():

                self.List = []
                z = 1
                if self.Num1.get()!="":
                    self.List.insert(0,self.Num1.get())
                    z = 0
                z = 1
                if self.Num2.get()!="":
                    z = 0
                    self.List.insert(1,self.Num2.get())
                z = 1            
                if self.Num3.get()!="":
                    z = 0
                    self.List.insert(2,self.Num3.get())
                z = 1            
                if self.Num4.get()!="":
                    z = 0
                    self.List.insert(3,self.Num4.get())
                z = 1           
                if self.Num5.get()!="":
                    z = 0
                    self.List.insert(4,self.Num5.get())
                z = 1
                if self.Group.get()!="":
                    z = 0
                    self.List.insert(5,self.Group.get())
                
                n = 0
                for i in range(0,int(self.DT.get())):
                    if self.Numlist[i].get()=="" or self.Group.get()=="":
                        # n = n+1
                        messagebox.showerror("Partnerns Name","Please.. Ente All Details \nThis Details May be use full for you")
                        break
                
                

            # Storing the data in a file using my sql database system
                conn=sqlite3.connect('doc/Partners.db')
                conn.execute('''CREATE TABLE IF NOT EXISTS part(
                Part1 TEXT ,
                Part2 TEXT ,
                Part3 TEXT,
                Part4 TEXT,
                Part5 TEXT,
                Gname TEXT
                                
                );''')
                query = "INSERT INTO part(Part1,Part2,Part3,Part4,Part5,Gname)  VALUES (?,?,?,?,?,?);"
                conn.execute(query,(
                self.Num1.get().capitalize(),
                self.Num2.get().capitalize(),
                self.Num3.get().capitalize(),
                self.Num4.get().capitalize(),
                self.Num5.get().capitalize(),
                self.Group.get().capitalize(),
                
                ))
                conn.commit()
                conn.close()
                if z==0:
                    for i in range(int(self.DT.get())):
                        self.Numlist[i].set("")
                        self.Group.set("")
                
                Renter.IdPass()

                
            self.Num1 = StringVar()
            self.Num2 = StringVar()
            self.Num3 = StringVar()
            self.Num4 = StringVar()
            self.Num5 = StringVar()
            self.Group = StringVar()
            self.Numlist = [self.Num1,self.Num2,self.Num3,self.Num4,self.Num5]
            self.xx = 50
            self.yy = 70
            from datetime import date  
            now = datetime.now() # Use now() to access the current date and time   
            self.todaytime= now.strftime(" %I:%M:%S")
            l1 = Label(F7,text='Welcome to SherShah group',font=('Algerian',20),fg='yellow',bg='crimson')
            l1.place(x=65,y=10)
            

            l2 = Label(F7,text='Partners Group Name:',font=('Algerian',15),fg='yellow',bg='crimson')
            l2.place(x=40,y=300)
            self.E5 = Entry(F7,font=('Arial',15),fg='red',width=13,textvariable=self.Group)
            self.E5.place(x=300,y=300)
            backButton = Button(F7,text='Next',bg='crimson',fg='yellow',activebackground='red',font=("Colonna MT",15),command=GetNames)
            backButton.place(x=492,y=312)

            l3 = Label(F7,text=f'Starting Date\n\n{self.Date}\n\nTime: {self.todaytime}',font=('Algerian',15),fg='white',bg='crimson')
            l3.place(x=350,y=100)
            backButton = Button(F7,cursor="hand2",text='<=',bg='crimson',fg='yellow',activebackground='red',font=("",10),command=Renter.Registration)
            backButton.place(x=0,y=330)
            for i in range(0,int(self.DT.get())):
                l0 = Label(F7,text=f'Partner{i+1}',font=('Algerian',15),fg='yellow',bg='crimson')
                l0.place(x=self.xx,y=self.yy)
                self.E4 = Entry(F7,font=('Arial',15),fg='green',width=13,textvariable=self.Numlist[i])
                self.E4.place(x=180,y=self.yy)
                self.yy = self.yy+30
            F7.place(x=0,y=0)
    
    def LogReg(self):
        import time
        F8 = Frame(root,width=550,height=350,bg='crimson')
        self.Regs=  0
        l4 = Label(F8,text=':Welcome to Tenali Room Accountens:',font=('Algerian',20),fg='yellow',bg='crimson',relief='groove')
        l4.place(x=8,y=0)
        Login = Button(F8,cursor="hand2",relief='ridge',border=5,text='Login',bg='white',fg='blue',activebackground='red',font=("Magneto",15,UNDERLINE),command=Renter.Login)
        Login.place(x=140,y=150)
        def REG():
            conn=sqlite3.connect('doc/test.db')
            query = "SELECT DOB FROM todo;"
            for item in conn.execute(query,()):
                self.Regs =  item[0]
           
            if self.Regs==str(0):
                
                Renter.Registration()
                self.Regs=1

                update = "UPDATE todo SET DOB = ?;"
                conn.execute(update,(self.Regs,))
            else:
               
                
                messagebox.showwarning("Registration","You have Alrady Registered on this divice")
            
            conn.commit()
            conn.close()
        Reg = Button(F8,cursor="hand2",relief='groove',border=5,text='Regs.',bg='white',fg='red',activebackground='red',font=("Magneto",15,UNDERLINE),command=REG)
        Reg.place(x=350,y=150)
        
        F8.place(x=0,y=0)
       
        self.x = 565    
        self.text = '🤫🤥This Software is Devloped by Mr. Monu Saini😎 ! This Software will be help you to mantain your Room Partners Expentions ! It is Provide Good Result🤫🤥 '
        
        # must be flat, groove, raised, ridge, solid, or sunken

        L30 = Frame(F8,width=550,height=40,relief='raised',border=2,bg='crimson')
        L1 = Label(L30,fg='yellow',font=('Magneto',13),bg='crimson')
        L30.place(x=0,y=321)

       
        self.yyy = 0
        for i in self.text:
            while(True):
                L1.config(text=self.text)
                L1.place(y=self.yyy,x=self.x)
                self.x = self.x-1
                
                L1.update()
                if self.x==-1200:
                    self.x=460
                time.sleep(0.0000001)
 
    def IdPass(self):
        self.usname = StringVar()
        self.uspass = StringVar()
        F9 = Frame(root,width=550,height=350,bg='blue')
        l1 = Label(F9,text='Creante New Username and Password',font=('Algerian',17),fg='yellow',bg='blue')
        l1.place(x=50,y=20)
        F9.place(x=0,y=0)
        l2 = Label(F9,text=f'Username:',font=('Algerian',17),fg='lime',bg='blue')
        l2.place(x=110,y=96)
        self.E10 = Entry(F9,font=('Arial',15),fg='green',width=13,textvariable=self.usname)
        self.E10.place(x=250,y=100)
        
        l3 = Label(F9,text=f'Username:',font=('Algerian',17),fg='lime',bg='blue')
        l3.place(x=110,y=147)
        self.E11 = Entry(F9,font=('Arial',15),fg='green',width=13,textvariable= self.uspass)
        self.E11.place(x=250,y=150)


        def Update():
            
            if self.usname.get()=="" or self.uspass.get()=="":
                messagebox.showwarning("Registration","Please... don't leave blank\nFill the Details and Continous")
            elif self.usname.get().isnumeric():
                messagebox.showwarning("Registration","Username is not Vailid\nPlease.. fill the vailid Username")
            elif len( self.uspass.get())<6:
                messagebox.showwarning("Registration","Password is to short\nMinimum Length of Password is '6'")

            else:
                conn=sqlite3.connect('doc/test.db')
                query = "SELECT Passd FROM todo;"
                update = "UPDATE todo SET Passd = ?;"
                conn.execute(update,(self.uspass.get(),))
                update = "UPDATE todo SET UName = ?;"
                conn.execute(update,(self.usname.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo('Registration','Your Registration is Successfull\nNow you can use our services on this software')
                Renter.LogReg()
            
        Regis = Button(F9,cursor="hand2",text='Register Now',bg='blue',fg='yellow',activebackground='#0343DF',command=Update)
        Regis.place(x=468,y=325)

    def FindbyName(self):
        F1 = StringVar()
        F7 = Frame(bg='#094e42',width=570,height=350)
        
        # must be flat, groove, raised, ridge, solid, or sunken

        L1  = Label(F7,text="Partner Name: ",font=("Arial",15),bg='#094e42',fg='white',relief='ridge')
        L1.place(x=45,y=50)
        E1 = Entry(F7,font=("Arial",15),textvariable=F1,border=2,relief='ridge')
        E1.place(x=190,y=50)
        
        def SearchData():

            L1  = Label(F7,text="Product name",font=("Arial",13),fg="white",bg='#094e42')
            L1.place(x=0,y=120)

            L2  = Label(F7,text="Buy Date",font=("Arial",13),fg="white",bg='#094e42')
            L2.place(x=125,y=120)

            L3  = Label(F7,text="Buyer Name",font=("Arial",13),fg="white",bg='#094e42')
            L3.place(x=250,y=120) 

            L4  = Label(F7,text="Quantity",font=("Arial",13),fg="white",bg='#094e42')
            L4.place(x=380,y=120)

            L5  = Label(F7,text="Price",font=("Arial",13),fg="white",bg='#094e42')
            L5.place(x=490,y=120)

            conn=sqlite3.connect('doc/RoomAccount.db')
            query = "SELECT * FROM ins;"
            
            a = 0
            total=  0
            

            root.geometry('570x350')
                    
            # def fg(self):
            scroll = Scrollbar(root)
            scroll.place(x=550,y=150,height=200)

            L8 = Text(root,width=61,height=11,font=('Arial',13),yscrollcommand=scroll.set,bg='#094e42',fg='white')
            L8.place(x=0,y=150)
            scroll.config(command=L8.yview)



            L9 = Label(F7,font=("Algerian",15),fg="white",bg='#094e42',padx=10)
            L9.place(x=50,y=5)
            for item in conn.execute(query,()):
                if F1.get().capitalize() in item:
                    total = total+int((item[4]))
                    a=1
                    L8.insert(1.0,f"{item[0]}\t\t{item[1]}\t      {item[2]}\t\t     {item[3]}\t\t{item[4]}\n")
                    L9.config(text=f'ToTaL                    =                 {total}',)
                    L9.update()
            F1.set("")

            if a==0:
                L9.config(text="                                                                                            ")
                L9.update()
                messagebox.showinfo("Error","No data Found")
            L8.config(state=DISABLED)
            conn.close()
                # FindbyName()
        B1 = Button(F7,cursor="hand2",text="Search",font=("Arial",13),command=SearchData)
        B1.place(x=347,y=90,height=20)
        
        backButton = Button(F7,cursor="hand2",text='<=',bg='#094e42',fg='yellow',activebackground='red',font=("",10),command=Renter.Choice)
        backButton.place(x=0,y=80)
        F7.place(x=0,y=0)

    def SetTraveling(self):
        global finish
        def Tradate():
            from datetime import date  
            now = datetime.now() # Use now() to access the current date and time   
            
            
            self.travel=[]
            self.travel.insert(0, now.strftime("%d"))
            self.travel.insert(1,now.strftime("%m"))
            self.travel.insert(2,now.strftime("%Y"))

            F4 = Frame(root,width=550,height=350,bg='gray')
            self.dat = Calendar(F4, selectmode = 'day',
                        year = int(self.travel[2]),
                        month = int(self.travel[1]),
                        day = int(self.travel[0]))
            def filldate():
                global finish
                s = self.dat.get_date().split('/')
                b= self.dat.get_displayed_month()
                print(f"{s[1]}/{s[0]}/{b[1]}")
                # print(self.Trafrom.get())
                # print(self.Trato.get())
                # print(self.Traammount.get())
                # print(self.Traname.get())
                self.Tname = self.Traname.get()
                
                # self.Tname = self.Traname.get()
                self.Tammount = self.Traammount.get()
                self.Tfrom = self.Traammount.get()
                self.Tto = self.Trato.get()
                self.Tammount = self.Traammount.get()
                finish = 1
                Renter.SetTraveling()
                self.Tradate.set(f"{s[1]}/{s[0]}/{b[1]}")

            self.dat.pack(pady = 20)
            F4.place(x=0,y=0)
            datebutton  = Button(F4,cursor="hand2",text='FiNiSh',font=("",8,'bold'),padx=120,fg='yellow',bg='gray',activebackground='silver',activeforeground='yellow',command=filldate)
            datebutton.place(x=0,y=205)
           
        def Import():
            if self.Tradate.get()=='' or self.Traname.get()=='' or self.Trafrom.get()=='' or self.Trato.get()=='' or self.Traammount.get()=='':
                messagebox.showinfo('Travelng','Please.. Fill the all  Details')
            elif self.E3.get()!='' and self.E4.get()!='' and self.E5.get()!='' or self.E6.get()!='':
                conn=sqlite3.connect('doc/traveling.db')
                conn.execute('''CREATE TABLE IF NOT EXISTS tra(
                date TEXT,
                name TEXT,
                start TEXT,
                end TEXT ,
                ammount TEXT 
                );''')
                query = "INSERT INTO tra(date,name,start,end,ammount)  VALUES (?,?,?,?,?);"
                conn.execute(query,(self.Tradate.get(),self.Traname.get(),self.Trafrom.get(),self.Trato.get(),self.Traammount.get()))
                conn.commit()
                conn.close()
                print(self.Tradate.get(),self.Traname.get(),self.Trafrom.get(),self.Trato.get(),self.Traammount.get())

                self.Tradate.set("")
                self.Traname.set("")
                self.Trafrom.set("")
                self.Trato.set("")
                self.Traammount.set("")
                messagebox.showinfo('Traveling','Your Traveling details are successfully Recorded\nFill more details after the next travele')
            else:
                messagebox.showinfo('Traveling','Invailid Details')
     
        self.Traname = StringVar()
        self.Tradate = StringVar()
        self.Trafrom = StringVar()
        self.Trato = StringVar()
        self.Traammount = StringVar()
        F2 = Frame(root,width=550,height=350,bg='#008080')
        conn=sqlite3.connect('doc/Partners.db')
        query = "SELECT * FROM part;"
        for item in conn.execute(query,()):
            self.partlist = item
       
        backButton = Button(F2,cursor="hand2",text='<=',bg='crimson',fg='yellow',activebackground='red',font=("",10),command=Renter.Choice)
        backButton.place(x=0,y=330)
        l0 = Label(F2,text='Welcome to tenali traveling \nsystem',font=('Algerian',20),fg='yellow',bg='#008080')
        l0.place(x=75,y=0)
        if finish==1:
            self.Traname.set(self.Tname)
            self.Traammount.set(self.Tammount)
            self.Trafrom.set(self.Tfrom)
            self.Trato.set(self.Tto)
        else:
            print('not get')

        # Geting traveling date
        l4 = Label(F2,text='Traveling Date:',font=('Georgia',10,'bold'),fg='yellow',bg='#008080')
        l4.place(x=100,y=90)
        self.E4 = Entry(F2,font=('Arial',15),fg='green',width=13,textvariable=self.Tradate)
        self.E4.place(x=100,y=115)
        Button0 = Button(F2,cursor="hand2", text = "^",bg='white',command=Tradate)
        Button0.place(x=230,y=116)
        # Finishing the traveling date
        # Geting the Traveler Name
        l5 = Label(F2,text='Traveler Name:',font=('Georgia',10,'bold'),fg='yellow',bg='#008080')
        l5.place(x=330,y=90)
        self.E3 = ttk.Combobox(F2,font=('Arial',15),width=13,foreground='green',textvariable=self.Traname,values=self.partlist)
        self.E3.place(x=330,y=116)

        l = Label(F2,text='Select Location of Your Travel Aria',font=('Rockwell',15),fg='white',bg='#008080')
        l.place(x=115,y=165)
        l7 = Label(F2,text='From:',font=('Algerian',12),fg='yellow',bg='#008080')
        l7.place(x=30,y=210)

        self.E5 = Entry(F2,font=('Arial',15),fg='green',width=13,textvariable=self.Trafrom)
        self.E5.place(x=100,y=210)

        l7 = Label(F2,text='To:',font=('Algerian',12),fg='yellow',bg='#008080')
        l7.place(x=290,y=210)

        self.E6 = Entry(F2,font=('Arial',15),fg='green',width=14,textvariable=self.Trato)
        self.E6.place(x=335,y=210)

        l7 = Label(F2,text='Enter Traveling Ammount:  ₹:',font=('Rockwell',13),fg='yellow',bg='#008080')
        l7.place(x=10,y=280)

        self.E7 = Entry(F2,font=('Arial',15),fg='green',width=8,textvariable=self.Traammount)
        
        self.E7.place(x=250,y=280)



        if number==2:
            def Insert():
                self.proname.set(self.prname)
                self.prodate.set(self.date)
                self.Byname.set(self.Byna)
                self.prowate.set(self.prwate)
                self.proprice.set(self.prprice)
                
            Insert()
            
        Button2 =Button(F2,text='FiNiSh',font=('Georgia',10,'bold'),bg='yellow',fg='crimson',command=Import)
        
        Button2.place(x= 470,y=320)

        F2.place(x=0,y=0)

    def GetTravel(self):
        F16 = Frame(root,width=570,height=350,bg='#06C2AC')
        backButton = Button(F16,cursor="hand2",text='<=',bg='#06C2AC',fg='blue',activebackground='blue',font=("",10),command=Renter.Choice)
        backButton.place(x=0,y=325)
        l = Label(F16,text="------------------------------------------------------------------------------------------------------------------------- ",bg='#008080',font=('Copperplate Gothic Bold',20),fg='lime')
        l.place(x=0,y=17)
        l7 = Label(F16,text="Your Last Traveling Record ",bg='#008080',padx=80,font=('Copperplate Gothic Bold',20),fg='white')
        l7.place(x=0,y=0)

        l7 = Label(F16,text=f"s.    Date\t                   Traveller               From\t\t        To\t              Ammount ",bg='#06C2AC',font=('Copperplate Gothic Bold',10),fg='yellow')
        l7.place(x=10,y=40)

        conn=sqlite3.connect('doc/traveling.db')
        querys = "SELECT ammount FROM tra;"
        ammount = 0
        for items in conn.execute(querys,()):
            ammount = ammount+int(items[0])

        L9 = Label(F16,text=f'\t\tToTaL                                      {ammount}',font=("Algerian",15),fg="white",bg='#06C2AC')
        L9.place(x=50,y=320)
        conn=sqlite3.connect('doc/traveling.db')
        query = "SELECT * FROM tra;"
        
        root.geometry('570x350')
        scroll = Scrollbar(F16)
        scroll.place(x=552,y=70,height=250)

        L8 = Text(root,width=61,height=13,border=1,font=('Arial',13),yscrollcommand=scroll.set,bg='#06C2AC',fg='crimson')
        L8.place(x=0,y=70)
        scroll.config(command=L8.yview)

        for v,item in enumerate( conn.execute(query,())):
        
            a=1
            L8.insert(1.0,f"{v+1}.  {item[0]}\t\t{item[1]}\t      {item[2]}\t\t     {item[3]}\t\t{item[4]}\n")
            
            L9.update()
        conn.close()
        L8.config(state=DISABLED)
        F16.place(x=0,y=0)
if __name__ == '__main__':
    root  = Tk()
    number =  1
    cout = 0
    size= 15
    a = 1
    finish = 0
    root.geometry('550x350')
    root.title('Tenali Account')
    root.resizable(0,0)
    root.wm_iconbitmap('doc/tenali.ico')

    # set the background Image 
    Renter = ROOM()

    # Renter.Login()
    # Renter.Registration()
    # Renter.GetRecord()
    Renter.LogReg()
    # Renter.Choice()
    # Renter.Partname()
    # Renter.FindbyName()
    # Renter.SetProduct()
    # Renter.fg()
    # Renter.IdPass()
    # Renter.SetTraveling()
    # Renter.GetTravel()
    # Renter.changepass()
    root.mainloop()