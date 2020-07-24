#A translation into Python of my Iterative Merge Sort Code. Don't do it this way please! It takes hours to get right. Instead use recursion which is so much more simple and logical.
import copy
def merge_sort(list):
	splits = [[list]] #Looks like [[[3,6,2,4]]] as list is [3,6,2,4] for example. Will become [[[3,6,2,4]],[[3,6],[2,4]],[[3],[6],[2],[4]]]
	while len(splits[len(splits)-1]) != len(list): #Starts off as 1, then 2, then 4 etc, doubling each time although that depends on the presence of odd numbers
		thisSplit = []
		for item in splits[len(splits)-1]:
			lengthOfEachHalf = ((len(item)-1)// 2) +1
			thisSplit.append(item[0:lengthOfEachHalf])
			if (lengthOfEachHalf!=len(item)):
				thisSplit.append(item[lengthOfEachHalf:len(item)])
		splits.append(thisSplit)
	results = [splits[len(splits)-1]] #We initialise the results variable which will contain the merged results at each level, using 
	for i in range(0,len(splits)-1):
		nextMergeLevel = splits[len(splits)-2-i]
		thisMergeLevel = []
		counter = 0
		for item in nextMergeLevel:
			itemsToMerge = [] #Will hold the items that need to be merged to form a sorted version of item
			lengthToMerge = len(item)
			j = 0
			toAddToCounter = 0
			while (j <= len(results[i]) -1 - counter):
				lengthToMerge = lengthToMerge - len(results[i][counter+j])
				itemsToMerge.append(results[i][counter+j])
				toAddToCounter +=1
				if (lengthToMerge == 0): #We have found enough sub-lists to merge to make up the same length as the corresponding list at the level above
					break
				j+=1
			counter += toAddToCounter
			if (len(itemsToMerge) == 1):
				merged_result = itemsToMerge[0]
			else:
				merged_result = []
				while (len(itemsToMerge[0]) > 0 and len(itemsToMerge[1]) > 0): #Do the merging
					if (itemsToMerge[0][0] < itemsToMerge[1][0]):					
						merged_result.append(itemsToMerge[0][0])
						del itemsToMerge[0][0]
					else:
						merged_result.append(itemsToMerge[1][0])
						del itemsToMerge[1][0]
				merged_result += itemsToMerge[0]
				merged_result += itemsToMerge[1]
			thisMergeLevel.append(merged_result)
		results.append(thisMergeLevel)
	return results[len(results)-1][0]

print(merge_sort([5,3,4,1]))
print(merge_sort([5,3,4,1,36,21,94,10,16,84,36,12]))
