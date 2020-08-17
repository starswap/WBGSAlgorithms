list = [7,5,6,3,1] 

def sort(list, is_sorted=False):
    if is_sorted:
        return list[::order]
        
    is_sorted = True
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            is_sorted = False
    return sort(list, is_sorted)
                
    

        
order = int(input("do you want the list to be ascending?(1) or descending(-1): "))
print(sort(list))
