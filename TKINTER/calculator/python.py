from tkinter import *

root=Tk()
root.title('CALCULATOR')
root.geometry("400x400")

fr=Frame(root,width = 200, height = 200)
fr.place(x=0,y=0)
gr=Frame(root)
gr.place(x=200,y=0)
rr=Frame(root)
rr.place(x=200,y=110)
def get(n,l):
    l.append(n)
    

def buttons(l):
    Button(gr,text="1",command=lambda: get(1,l)).grid(row=20,column=1)
    Button(gr,text="2",command=lambda: get(2,l)).grid(row=20,column=2)
    Button(gr,text="3",command=lambda: get(3,l)).grid(row=20,column=3)
    Button(gr,text="4",command=lambda: get(4,l)).grid(row=21,column=1)
    Button(gr,text="5",command=lambda: get(5,l)).grid(row=21,column=2)
    Button(gr,text="6",command=lambda: get(6,l)).grid(row=21,column=3)
    Button(gr,text="7",command=lambda: get(7,l)).grid(row=22,column=1)
    Button(gr,text="8",command=lambda: get(8,l)).grid(row=22,column=2)
    Button(gr,text="9",command=lambda: get(9,l)).grid(row=22,column=3)
    Button(gr,text="0",command=lambda: get(0,l)).grid(row=23,column=2)
    Button(gr,text="X",command=lambda: get("*",l)).grid(row=20,column=4)
    Button(gr,text="/",command=lambda: get("/",l)).grid(row=21,column=4)
    Button(gr,text="+",command=lambda: get("+",l)).grid(row=22,column=4)
    Button(gr,text="-",command=lambda: get("-",l)).grid(row=23,column=3)
    Button(gr,text="=",command=lambda: calc(l)).grid(row=23,column=4)
    Button(gr,text="Ac",command = lambda : del1(l)).grid(row=23,column=1)

    def on_enter(e):
        e.widget['background'] = 'lightblue'

    def on_leave(e):
        e.widget['background'] = 'SystemButtonFace'

    for button in gr.winfo_children():
        button.bind("<Enter>",on_enter)
        button.bind("<Leave>",on_leave)

def del1(n):
   
    n.clear()




def calc(l):
    a = ''
    for i in l:
        a += str(i)

    print(a)
    if a != '':
        try:
            b = eval(a)
            l.clear()
            l.append(b)
            show2(b)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
    else:
        print("No expression to evaluate.")

Label(rr,text="RESULT= ").pack(side=LEFT)
l2=Label(rr,text="")
l2.pack(side=LEFT)

def show2(a):
    l2.config(text=str(a))

    



def main():
    l=[]
    
    Label(fr,text="input1").place(anchor=NW,x=1,y=1)
    e1=Entry(fr)
    e1.place(x=40,y=1)
    Label(fr,text="input").place(anchor=NW,x=1,y=20)
    e2=Entry(fr)
    e2.place(x=40,y=20)

    
    
    buttons(l)
    
    
    

    print(l)
    
    
    
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