a = int(input("please enter the first number: "))
b = int(input("please enter the second number: "))
temp = 0

def HCF(a,b):
  if a < b:
    temp = a
    a = b
    b = temp
  while b != 0:
    c = a%b
    a = b
    b = c
  return a

print("The Highest Common Factor is " + str(HCF(a,b)))
