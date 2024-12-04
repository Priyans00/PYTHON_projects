import tkinter as tk
import csv
from replit import clear


root = tk.Tk()
def write1(k,n):
    with open("BEGINNER_PROJECTS/TO_DO_LIST_tkinter/storage.csv","a",newline='') as f:
        c = csv.writer(f)
        c.writerow([k,n])
    tk.Label(root,text=k ).grid(row=1,column=4)

def input_task(): 
    tk.Label(root,text="input the task").grid(row=0)
    e1=tk.Entry(root)
    e1.grid(row=0,column=1)
    tk.Label(root,text="input  the deadline").grid(row=1)
    e2=tk.Entry(root)
    e2.grid(row=1,column=1)
    button = tk.Button(root,text="confirm",command= lambda: write1(e1.get(),e2.get()))
    button.grid(row=2,column=1)
    button = tk.Button(root,text="go back to menu",command=menu)
    button.grid(row=3,column=1)
    
        

def see_task():
    with open("BEGINNER_PROJECTS/TO_DO_LIST_tkinter/storage.csv","r",newline='') as f:
        c=csv.reader(f)
        label = tk.Label(root,text='')
        label.grid(row=4,column=4)
    
        for row in c:
            for j in row:
                label.config(text= j )


def menu():
    clear()
    button = tk.Button(root,text="input",command=input_task)
    button.grid(row=0,column=0)
    button1 = tk.Button(root,text="show",command=see_task)
    button1.grid(column=0,row=1)

menu()

root.mainloop()

