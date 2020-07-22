#Some code I wrote in Python in 2017 (Gosh!Ancient!) to accomplish this task, based on some pseudocode from Dr Hedges
def euclid(x,y):
  if x<y:
    tmp = x
    x = y
    y = tmp
  while not y == 0:
    z = x%y
    x = y
    y = z
  return x

a = int(input("Enter first number"))
b = int(input("Enter second number"))
print("GCD = " + str(euclid(a,b)))
