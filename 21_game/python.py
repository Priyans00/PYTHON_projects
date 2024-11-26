import random 
def main():
    flag = True
    k = int(input("you want to start first(1) or second(2)"))
    global n
    n = []
    while flag == True:
        if k == 1:
            human(n)
            if check(n)==False:
                break
            comp(n)
            if check(n)==False:
                break
        if k == 2:
            comp(n)
            if check(n)==False:
                break
            human(n)
            if check(n)==False:
                break
        flag=check(n)

def check(n):
    if 21 in n:
        return False
    else:
        return True

def human(n):
    if n == []:
        l = 1
    else:
        l = n[-1]+1
    k = int(input("how many no you want to enter"))
    if k not in [1,2,3]:
        print('you are disqualified from the game ')
        n.append(21)
    for i in range(l,l+k):
        n.append(i)
    if 21 in n:
        loose('you')
    else :
        print("order of input after your turn is :")
        print(n)

def comp(n):
    if n==[]:
        l=1
    else:
        l=n[-1]+1
    
    remainder = l%4
    if remainder == 1:
        k=3
    else:
        if remainder == 2:
            k=2
        elif remainder == 3:
            k=1
        else:
            k=1



    for i in range(l,l+k):
        n.append(i)
    if 21 in n:
        loose('comp')
    print("order of input after comp's turn is :")
    print(n)

def loose(s):
    print(f"{s} lost")

def start():
    k = input("you want to play ? (y/Y)")
    while k == 'y' or k == 'Y':
        n=[]
        main()
        k = input('you want to play again ? (y/Y)')
start()