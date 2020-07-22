#array = [2,83,6,6,88,97,5,154,3,4,35,7,8,2,5,10,7,8,18]

sorted = False
def bubble_sort (array,sorted):
    while sorted == False:
        #sorted = False
        changed = False # sets changed back to false 
        for i in range (len (array)-1):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]   # swapping the variables around
                array[i+1] = tmp
                changed = True          # used to check if a swap has occured at any point during a run down the list
                #sorted = False
                
        if changed == False:    # checking if the list is sorted
            sorted = True       # this could probably be more optimized 



bubble_sort (array,sorted)
print(array)
