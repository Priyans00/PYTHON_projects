from tkinter import *

root=Tk()
root.title('CALCULATOR')

fr=Frame(root,width = 200, height = 200)
fr.place(x=0,y=0)
def main():
    Label(fr,text="input1").place(anchor=NW,x=1,y=1)
    e1=Entry(fr,textvariable=int)
    e1.place(x=40,y=1)
    
    
    
    Label(fr,text="input").place(anchor=NW,x=1,y=20)
    e2=Entry(fr,textvariable=int)
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

def show(a):
    Label(fr,text="RESULT = ").place(x=20,y=90)
    Label(fr,text=str(a)).place(x=80,y=90)

main()
root.mainloop()