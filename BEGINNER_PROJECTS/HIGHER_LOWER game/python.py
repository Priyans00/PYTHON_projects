import random
from data12 import data2 as data
from replit import clear



def start():
    ch='Y'
    while ch=='Y':
        main()
        ch=input("you want to play again ? (Y,N)")
        clear()

def win():
    print("aap jeetgaye !!!")

def show(k,s1,s2,l):
    print(f" {data[k]['name']}'s follower count = {s1}")
    print(f" {data[l]['name']}'s follower count = {s2}")

def lost():
    print("you lost haha")

def main():
    k=random.randint(0,23)
    print(f"name= {data[k]['name']} , desc = {data[k]['description']} , origin = {data[k]['country']}")
    print("vs")
    while True:
        l=random.randrange(0,23)
        if l==k:
            continue
        else:
            print(f"name= {data[l]['name']} , desc = {data[l]['description']} , origin = {data[l]['country']}")
            break
    p=int(input("who has higher followers upper (1) or lower(2) ?"))
    s1=data[k]['follower_count']
    s2=data[l]['follower_count']
    m=max(s1,s2)
    ma=[s1,s2]
    if ma[p-1]==m:
        win()
    else:
        lost()
    show(k,s1,s2,l)   
    
start()