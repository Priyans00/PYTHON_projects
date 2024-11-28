from js import document

def main(*args):
    # Add error checking for elements
    name1_elem = document.getElementById('name1')
    name2_elem = document.getElementById('name2')
    
    if not name1_elem or not name2_elem:
        print("Error: Input elements not found!")
        return
    
    n1 = name1_elem.value
    n2 = name2_elem.value
    
    if not n1 or not n2:
        document.getElementById('result').innerHTML = "Please enter both names"
        return
        
    l1 = list(n1)
    l2 = list(n2)
    temp = l1.copy()
    for i in temp:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
    k = len(l1) + len(l2)
    l = flames(k)
    return l

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
    if not l:
        return "Error in calculation"
        
    relationships = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    k = relationships[l[0]]
    result_elem = document.getElementById('result')
    if result_elem:
        result_elem.innerHTML = k

def calculate_flames(*args):
    l = main()
    if l:
        rel_check(l)

# Wait for document to load before binding
def init():
    button = document.getElementById('calculate')
    if button:
        button.onclick = calculate_flames

# Call init when document is ready
init()

