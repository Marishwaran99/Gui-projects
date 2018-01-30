from tkinter import *
from tkinter import messagebox
import random,time,sqlite3
conn=sqlite3.connect('database.db')
c=conn.cursor()
root=Tk()
root.title("Ice Cream Billing system")
root.geometry("1200x800+0+0")
tf=Frame(root,width=1200,height=60,relief="raise",bd=10)
tf.pack(side=TOP)
lf=Frame(root,width=800,height=700,relief="raise",bd=10)
lf.pack(side=LEFT)
lf1=Frame(lf,width=800,height=500,relief="raise",bd=5)
lf1.pack(side=TOP)
lf2=Frame(lf,width=820,height=200,relief="raise",bd=5)
lf2.pack(side=BOTTOM)
lf2a=Frame(lf2,width=400,height=200,relief="raise",bd=5)
lf2a.pack(side=LEFT)
lf2b=Frame(lf2,width=400,height=200,relief="raise",bd=5)
lf2b.pack(side=RIGHT)
lf1a=Frame(lf1,width=400,height=500,relief="raise",bd=5)
lf1a.pack(side=LEFT)
lf1b=Frame(lf1,width=400,height=500,relief="raise",bd=5)
lf1b.pack(side=RIGHT)
rf=Frame(root,width=600,height=700,relief="raise",bd=10)
rf.pack(side=RIGHT)
rf1=Frame(rf,width=600,height=50,relief="raise",bd=6)
rf1.pack(side=TOP)
rf2=Frame(rf,width=600,height=450,relief="raise",bd=6)
rf2.pack(side=TOP)
rf3=Frame(rf,width=600,height=150,relief="raise",bd=6)
rf3.pack(side=TOP)
title=Label(tf,font=("arial",40,"bold"),fg="blue",text="     Ice Cream Billing system     ")
title.pack(side=RIGHT)
#-====================Functions===================================
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS data(bill_no TEXT,amount REAL)")
    conn.commit()
def insert(bno,cost):
    c.execute("INSERT INTO data (bill_no ,amount) VALUES(?,?)",(bno,cost))
    conn.commit()
def reciept():
    bno=random.randrange(11111,99999)
    txt.configure(state='normal')
    txt.insert("1.0","\t A-Z IceCream \t \n ")
    txt.insert(END,"--------------------------------------------- \n")
    txt.insert(END,"Bill no. \t \t" +str(bno)+"\n \n")
    txt.insert(END,"Chocobar \t \t" +str(var1.get())+"\n \n")
    txt.insert(END,"Strawberry \t \t" +str(var2.get())+" \n  \n")
    txt.insert(END,"Vanilla \t \t" +str(var3.get())+" \n \n")
    txt.insert(END,"Butterscotch\t \t" +str(var4.get())+" \n \n")
    txt.insert(END,"Kulfi \t \t" +str(var5.get())+"\n \n")
    txt.insert(END,"Ice cream cake \t \t" +str(var6.get()) +"\n \n")
    txt.insert(END,"Mint Ice cream \t \t" +str(var7.get())+"\n \n")
    txt.insert(END,"Cone ice \t \t" +str(var8.get())+"\n \n")
    txt.insert(END,"Cup ice \t \t" +str(var9.get())+"\n \n")
    txt.insert(END,"Mango bar \t \t" +str(var10.get())+"\n \n")
    txt.insert(END,"------------------------------------ \n \n")
    txt.insert(END,"Sub total \t \t" +str(var11.get())+"\n \n")
    txt.insert(END,"Service charge \t \t" +str(var12.get())+"\n \n")
    txt.insert(END,"Tax \t \t" +str(var13.get())+"\n \n")
    txt.insert(END,"Total cost \t \t" +str(var14.get())+"\n \n")
    txt.configure(state='disabled')
    create_table()
    insert(bno,var14.get())
def total():
    global bno
    subtot=var1.get()*10+var2.get()*20+var3.get()*20+var4.get()*30+var5.get()*15+var6.get()*75+var7.get()*50+var8.get()*40+var9.get()*30+var10.get()*35
    var11.set(subtot)
    tax=var1.get()*10*0.05+var2.get()*20*0.05+var3.get()*2*0.050+var4.get()*3*0.050+var5.get()*15*0.05+var6.get()*75*0.05+var7.get()*50*0.05+var8.get()*40*0.05+var9.get()*30*0.05+var10.get()*35*0.05
    var13.set(tax)
    sc=round(subtot*0.06,2)
    var12.set(sc)
    tot=subtot+tax+sc
    var14.set(tot)
def quit():
    e=messagebox.askyesno("Billing System","Do you want to exit")
    if e>0:
        root.destroy()
def reset():
    txt.configure(state='normal')
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0.0")
    var12.set("0.0")
    var13.set("0.0")
    var14.set("0.0")
    txt.delete("1.0",END)
    txt.configure(state='disabled')
#===================Labels======================================
l1=Label(lf1a,text="Chocobar",font=('arial',20,'bold'),fg='chocolate')
l1.grid(row=0,column=0,padx=10,pady=10,sticky=W)
l2=Label(lf1a,text="Strawberry",font=('arial',20,'bold'),fg='deeppink')
l2.grid(row=1,column=0,padx=10,pady=10,sticky=W)
l3=Label(lf1a,text="Vanilla",font=('arial',20,'bold'),fg="blue4")
l3.grid(row=2,column=0,padx=10,pady=10,sticky=W)
l4=Label(lf1a,text="Butterscotch",font=('arial',20,'bold'),fg='gold3')
l4.grid(row=3,column=0,padx=10,pady=10,sticky=W)
l5=Label(lf1a,text="Kulfi",font=('arial',20,'bold'),fg='orange')
l5.grid(row=4,column=0,padx=10,pady=10,sticky=W)
l6=Label(lf1b,text="Icecream cake",font=('arial',20,'bold'),fg='magenta')
l6.grid(row=0,column=0,padx=10,pady=10,sticky=W)
l7=Label(lf1b,text="Mint Ice cream",font=('arial',20,'bold'),fg='green')
l7.grid(row=1,column=0,padx=10,pady=10,sticky=W)
l8=Label(lf1b,text="Cone Ice",font=('arial',20,'bold'),fg='red')
l8.grid(row=2,column=0,padx=10,pady=10,sticky=W)
l9=Label(lf1b,text="Cup Ice",font=('arial',20,'bold'),fg='cyan4')
l9.grid(row=3,column=0,padx=10,pady=10,sticky=W)
l10=Label(lf1b,text="Mango bar",font=('arial',20,'bold'),fg='gold2')
l10.grid(row=4,column=0,padx=10,pady=10,sticky=W)
l11=Label(lf2a,text="Sub total",font=('arial',20,'bold'),fg='red2')
l11.grid(row=0,column=0,padx=10,pady=10,sticky=W)
l12=Label(lf2a,text="Service charge",font=('arial',20,'bold'),fg='red2')
l12.grid(row=1,column=0,padx=10,pady=10,sticky=W)
l13=Label(lf2b,text="Tax",font=('arial',20,'bold'),fg='red2')
l13.grid(row=0,column=0,padx=10,pady=10,sticky=W)
l14=Label(lf2b,text="Total Cost",font=('arial',20,'bold'),fg='red2')
l14.grid(row=1,column=0,padx=10,pady=10,sticky=W)
l15=Label(lf2a,text="Rs/-",font=('arial',20,'bold'),fg='red2')
l15.grid(row=0,column=2,pady=10,sticky=W)
l16=Label(lf2a,text="Rs/-",font=('arial',20,'bold'),fg='red2')
l16.grid(row=1,column=2,pady=10,sticky=W)
l17=Label(lf2b,text="Rs/-",font=('arial',20,'bold'),fg='red2')
l17.grid(row=0,column=2,pady=10,sticky=W)
l18=Label(lf2b,text="Rs/-",font=('arial',20,'bold'),fg='red2')
l18.grid(row=1,column=2,pady=10,sticky=W)
l19=Label(rf1,text="Receipt",font=('arial',15,'bold'),fg='red2')
l19.grid(row=0,column=0,padx=10,sticky=W)
#====================textvariables===================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=DoubleVar()
var12=DoubleVar()
var13=DoubleVar()
var14=DoubleVar()
#===================Entries==========================
e1=Entry(lf1a,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var1)
e1.grid(row=0,column=1,sticky=E,padx=10,pady=10)
e2=Entry(lf1a,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var2)
e2.grid(row=1,column=1,sticky=E,padx=10,pady=10)
e3=Entry(lf1a,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var3)
e3.grid(row=2,column=1,sticky=E,padx=10,pady=10)
e4=Entry(lf1a,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var4)
e4.grid(row=3,column=1,sticky=E,padx=10,pady=10)
e5=Entry(lf1a,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var5)
e5.grid(row=4,column=1,sticky=E,padx=10,pady=10)
e6=Entry(lf1b,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var6)
e6.grid(row=0,column=1,sticky=E,padx=10,pady=10)
e7=Entry(lf1b,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var7)
e7.grid(row=1,column=1,sticky=E,padx=10,pady=10)
e8=Entry(lf1b,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var8)
e8.grid(row=2,column=1,sticky=E,padx=10,pady=10)
e9=Entry(lf1b,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var9)
e9.grid(row=3,column=1,sticky=E,padx=10,pady=10)
e10=Entry(lf1b,font=('arial',20,'bold'),fg="blue",width=5,textvariable=var10)
e10.grid(row=4,column=1,sticky=E,padx=10,pady=10)
e11=Entry(lf2a,font=('arial',20,'bold'),fg="blue",width=7,textvariable=var11)
e11.grid(row=0,column=1,sticky=E,padx=10,pady=10)
e12=Entry(lf2a,font=('arial',20,'bold'),fg="blue",width=7,textvariable=var12)
e12.grid(row=1,column=1,sticky=E,padx=10,pady=10)
e13=Entry(lf2b,font=('arial',20,'bold'),fg="blue",width=7,textvariable=var13)
e13.grid(row=0,column=1,sticky=E,padx=10,pady=10)
e14=Entry(lf2b,font=('arial',20,'bold'),fg="blue",width=7,textvariable=var14)
e14.grid(row=1,column=1,sticky=E,padx=10,pady=10)
#=================Textbox=================
txt=Text(rf2,font=('arial',15,'bold'),fg="blue4",width=30,height=15)
txt.grid(row=0,column=0)
s=Scrollbar(rf2)
s.grid(row=0,column=1,ipady=15)
s.config(command=txt.yview)
txt.configure(state='disabled',yscrollcommand=s.set)
#=================buttons====================
b1=Button(rf3,text="Total",font=("arial",15,'bold'),fg="red",command=total)
b1.grid(row=0,column=0)
b2=Button(rf3,text="Receipt",font=("arial",15,'bold'),fg="red",command=reciept)
b2.grid(row=0,column=1)
b3=Button(rf3,text="Reset",font=("arial",15,'bold'),fg="red",command=reset)
b3.grid(row=0,column=2)
b4=Button(rf3,text="Quit",font=("arial",15,'bold'),fg="red",command=quit)
b4.grid(row=0,column=3)
root.mainloop()
