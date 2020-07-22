#Implementation of Linear Search in Python by James
#array = [1,2,3,4,5,6,7,8,9]

target = input("what are you looking for?:   ")
found  = False

def lin_search(array,target):
    for i in range(0, len (array)):
        if array[i] == target:
            print("found")
            found = True
            return found
            
if lin_search(array,target) != True:
    print ("the item isn't in the list")
