from js import document

def display(message):
    # Get the output element
    output = document.getElementById('output')
    # Add the message with a line break
    output.innerHTML += str(message) + "<br>"

def clear_output():
    # Clear the output div
    document.getElementById('output').innerHTML = ""

def main(*args):
    try:
        # Clear previous output
        clear_output()
        
        # Get the starting player choice
        start_elem = document.getElementById('start')
        if not start_elem or not start_elem.value:
            display("Please select who starts (1 or 2)")
            return
            
        k = int(start_elem.value)
        if k not in [1, 2]:
            display("Please enter 1 or 2 only")
            return

        global n
        n = []
        flag = True
        
        while flag:
            if k == 1:
                human(n)
                if not check(n):
                    break
                comp(n)
                if not check(n):
                    break
            if k == 2:
                comp(n)
                if not check(n):
                    break
                human(n)
                if not check(n):
                    break
            flag = check(n)
            
    except Exception as e:
        display(f"An error occurred: {str(e)}")

def check(n):
    return 21 not in n

def human(n):
    try:
        if not n:
            l = 1
        else:
            l = n[-1] + 1
            
        # Get number input
        num_elem = document.getElementById('number')
        if not num_elem or not num_elem.value:
            display("Please enter a number (1-3)")
            n.append(21)  # Force game end
            return
            
        k = int(num_elem.value)
        
        if k not in [1, 2, 3]:
            display('You are disqualified from the game (must enter 1, 2, or 3)')
            n.append(21)
            return
            
        for i in range(l, l + k):
            n.append(i)
            
        if 21 in n:
            loose('you')
        else:
            display("Order of input after your turn is:")
            display(n)
            
    except Exception as e:
        display(f"Error in human turn: {str(e)}")
        n.append(21)

def comp(n):
    try:
        if not n:
            l = 1
        else:
            l = n[-1] + 1
        
        # Computer strategy
        remainder = l % 4
        if remainder == 1:
            k = 3
        elif remainder == 2:
            k = 2
        else:
            k = 1
            
        display(f"Computer chooses {k} number(s)")
        
        for i in range(l, l + k):
            n.append(i)
            
        if 21 in n:
            loose('Computer')
        else:
            display("Order of input after computer's turn is:")
            display(n)
            
    except Exception as e:
        display(f"Error in computer turn: {str(e)}")

def loose(s):
    display(f"{s} lost!")

# Initialize the game
def init():
    clear_output()
    display("Welcome to the 21 Game!")
    display("Choose who starts (1 for You, 2 for Computer)")
    
    # Bind the play button
    play_btn = document.getElementById('play_btn')
    if play_btn:
        play_btn.onclick = main

# Call init when document is ready
init()