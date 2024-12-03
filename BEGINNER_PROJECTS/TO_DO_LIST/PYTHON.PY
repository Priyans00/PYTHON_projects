import tkinter as tk
import csv


root = tk.Tk()
def write1(k,n):
    f=open("storage.csv","a")
    c=csv.writer(f)
    c.writerow([k,n])
    f.close() 

def input_task():
    tk.Label(root,text="input the task").grid(row=0)
    e1=tk.Entry(root)
    e1.grid(row=0,column=1)
    tk.Label(root,text="input  the deadline").grid(row=1)
    e2=tk.Entry(root)
    e2.grid(row=1,column=1)
    button = tk.Button(root,text="confirm",command= write1(e1,e2))
    button.grid(row=2,column=1)
    button = tk.Button(root,text="go back to menu",command=menu)
    button.grid(row=3,column=1)
        

def see_task():
    f=open('storage.csv','r')
    c=csv.reader(f)
    l=tk.Label(root,"")
    l.pack()
    for row in c.readrow():
        l.config(row)
        
    f.close()

def menu():
    button = tk.Button(root,text="input",command=input_task)
    button.grid(column=0)
    button1 = tk.Button(root,text="show",command=see_task)
    button1.grid(column=1)

menu()

root.mainloop()

