def euclid(a,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    print(a)

a = int(input("enter the larger number: "))
b = int(input("enter the smaller number: "))

euclid(a,b)
