from tkinter import *

root=Tk()
root.title('CALCULATOR')
root.geometry("100x120")

fr=Frame(root,width = 100, height = 120)
fr.place(x=0,y=0)

def get(n,l):
    l.append(n)

def main():
    l=[]
    
    Label(fr,text="input1").place(anchor=NW,x=1,y=1)
    e1=Entry(fr)
    e1.place(x=40,y=1)

    Label(fr,text="input").place(anchor=NW,x=1,y=20)
    e2=Entry(fr)
    e2.place(x=40,y=20)

    Button(fr,text="X",command=lambda: multiply(int(e1.get()),int(e2.get()))).place(x=1,y=60)
    Button(fr,text="/",command=lambda: divide(int(e1.get()),int(e2.get()))).place(x=20,y=60)
    Button(fr,text="+",command=lambda: addi(int(e1.get()),int(e2.get()))).place(x=40,y=60)
    Button(fr,text="-",command=lambda: subtract(int(e1.get()),int(e2.get()))).place(x=60,y=60)
    
    
def addi(a,b):
    show(a+b)
    
def multiply(a,b):
    show(a*b)
def divide(a,b):
    show(a/b)

def subtract(a,b):
    show(a-b)

Label(fr,text="RESULT = ").place(x=20,y=90)
l1=Label(fr,text='')
l1.place(x=80,y=90)

def show(a):
    l1.config(text=str(a))

main()
root.mainloop()