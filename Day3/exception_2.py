from Negative import ValidNum
def checkBalance():
    balance = input("Enter a number")
    if type(balance) != int:
        raise ValidNum("Not a valid Number")
try:
    checkBalance()
except ValidNum:
    print('Not a valid Number')