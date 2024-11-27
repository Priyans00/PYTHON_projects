def main():
    n1=input("enter 1st name")
    n2=input("enter 2nd name")
    l1=list(n1)
    l2=list(n2)
    temp=l1.copy()
    for i in temp:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
    k=len(l1)+len(l2)
    l=flames(k)
    rel_check(l)

def flames(n):
    l=['F','L','A','M','E','S'] 
    k=len(l)
    p=n
    while k>1:
        k=len(l)
        if k+1>p:
            l.pop(p-1)
            o=k-p
            k=len(l)
            for i in range(o):
                l.insert(0,l.pop())
            
        
        else:
            s=p%k
            l.pop(s-1)
            k=len(l)
            o=k-s
            for i in range(o):
                l.insert(0,l.pop())
            
    return l

def rel_check(l):
    
    relationships = {
    'F': 'Friends',
    'L': 'Lovers',
    'A': 'Affection',
    'M': 'Marriage',
    'E': 'Enemies',
    'S': 'Siblings'
    }
    k=relationships[l[0]]
    print(f"The relationship status is: {k}")

main()