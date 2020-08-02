#A very old and very basic implementation of quick sort which doesn't use a space efficient partitioning scheme, instead opting to append the items less than the pivot to one array and the items greater than the pivot to another. Illustrative none the less.
#2017 - Hamish Starling.
def quick(list1):
  pivot = list1[0]
  less = []
  greater = []
  for item in list1[1:]:
    if item < pivot:
      less.append(item)
    else:
      greater.append(item)
  if len(less) > 1:
      less = quick(less)
  if len(greater) > 1:
      greater = quick(greater)
  return less + [pivot] + greater
