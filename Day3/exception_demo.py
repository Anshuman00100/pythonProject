from Negative import ValidNum

def checkBalance():
    balance = int(input("Enter a number"))
    if(balance < 0 ):
        raise ValidNum("Negative Balance")

try:
    checkBalance()
except ValidNum:
    print("Negative Balance")