from tkinter import *

root=Tk()
root.title("CALCULATOR")
root.geometry("20x130")

gr=Frame(root)
gr.place(x=0,y=30)

rr=Frame(root)
rr.place(x=0,y=0)

def get(n,l):
    l.append(n)

def buttons(l):
    Button(gr,text="1",command=lambda: get(1,l)).grid(row=0,column=1)
    Button(gr,text="2",command=lambda: get(2,l)).grid(row=0,column=2)
    Button(gr,text="3",command=lambda: get(3,l)).grid(row=0,column=3)
    Button(gr,text="4",command=lambda: get(4,l)).grid(row=1,column=1)
    Button(gr,text="5",command=lambda: get(5,l)).grid(row=1,column=2)
    Button(gr,text="6",command=lambda: get(6,l)).grid(row=1,column=3)
    Button(gr,text="7",command=lambda: get(7,l)).grid(row=2,column=1)
    Button(gr,text="8",command=lambda: get(8,l)).grid(row=2,column=2)
    Button(gr,text="9",command=lambda: get(9,l)).grid(row=2,column=3)
    Button(gr,text="0",command=lambda: get(0,l)).grid(row=3,column=2)
    Button(gr,text="X",command=lambda: get("*",l)).grid(row=0,column=4)
    Button(gr,text="/",command=lambda: get("/",l)).grid(row=1,column=4)
    Button(gr,text="+",command=lambda: get("+",l)).grid(row=2,column=4)
    Button(gr,text="-",command=lambda: get("-",l)).grid(row=3,column=3)
    Button(gr,text="=",command=lambda: calc(l)).grid(row=3,column=4)
    Button(gr,text="Ac",command = lambda : del1(l)).grid(row=3,column=1)

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

Label(rr,text="RESULT =").pack(side=LEFT)
l2=Label(rr,text="")
l2.pack(side=LEFT)

def show2(a):
    l2.config(text=str(a))
def main():
    l=[]
    buttons(l)

main()
root.mainloop()