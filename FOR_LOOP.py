def grt_3(a = int(input('enter a')) , b = int(input('enter b')) , c = int(input('enter c'))):
    if a > b and a > c:
        print(a)
    elif b > a and b>c:
        print(b)
    elif c > a and c > b:
        print(c)
    else:
        print(a,b,c)


grt_3(3,4,5)
