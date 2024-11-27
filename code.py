total = 0
fee = 0
name = ''
membership = ''

def addMembership():
    global fee, name, membership
    if membership == "F":
        fee = 160
        name = "Full"
    elif membership == "J":
        fee = 80
        name = "Junior"
    elif membership == "P":
        fee = 30
        name = "Pensioner"
    elif membership == "X":
        return
    else:
        fee = 0
        name = "Invalid"
    
    function1()

def function1():
    global total, fee, membership
    total += fee
    print(f"Fee: {fee}, Membership: {name}, Total: {total}")
    membership = input("Membership type? ")
    addMembership()


function1()

print(total)