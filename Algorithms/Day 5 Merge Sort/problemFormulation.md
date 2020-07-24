TL;DR - Make the Merge Sort algorithm for integer and string sorting. You can use an iterative method or a recursive method, but I <strong>highly</strong> recommend a recursive method. The Merge Sort algorithm works by repeatedly splitting a list in half until we get to individual elements. These elements are merged in pairs to create lists of two elements, which are successively merged in pairs, with the number of lists halving and the list lengths doubling at each level, until we are left with 1 single list which is a sorted version of the original list.
<h1>Day 5</h1>
<h2>Merge Sort</h2>
<h3>Problem</h3>
In the final installment of the GCSE Searching and Sorting Algorithms Series (leaving some new content for the weekend), today we are going to tackle Merge Sort, arguably the most challenging of the four GCSE Algorithms.

Here is an appropriate link: https://en.wikipedia.org/wiki/Merge_sort

In many ways, Merge Sort is the sorting equivalent of Binary Search. Both algorithms involve repeatedly splitting the array in half, then acting upon one (in Binary Search) or both (Merge Sort) of these halves.

The Merge Sort Algorithm has log linear time complexity O(n log(n)), which means that it is less complex and so more efficient than Linear Search, but slightly more complex / less efficient than binary search, and of course much better than the quadratic Bubble Sort. One must remember that we shouldn't necessarily compare algorithms for two different purposes in terms of their efficiency, as they are ultimately very different. 

<img src="https://cdn-images-1.medium.com/max/1600/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg" />
[Source https://www.bigocheatsheet.com/]


A disadvantage of the Merge Sort algorithm in comparison to the Bubble Sort algorithm is that it is less memory/space efficient. This is because the sorting is not carried out on the original list, instead a copy is used at each level. This means we use more memory than for Bubble Sort. It is however, more time efficient than the Bubble Sort algorithm, with a more consistent run-time that is shorter for longer lists. Bubble sort does maintain two other advantages, though, these being the ease of programming (merge sort is a bit complex), and the efficiency as a check to see whether a list is sorted. In Merge sort the whole algorithm must be carried out to do this check, including all of the splitting and merging, while 1 simple pass of Bubble Sort will verify the state of a given list.




In the Merge sort algorithm, we repeatedly split a list in two until we are left with individual elements. We then repeatedly re-join pairs of elements in the right order to produce lists that are at each stage double the size, merging each pair of these sorted lists into another sorted list at the next level up, until eventually we are only left with one list, a sorted version of the one that we started with.

For Example:

[3,7,6,9,4,0]

[[3,7,6],[9,4,0]]

[[3,7],[6],[9,4],[0]]

[[3],[7],[6],[9],[4],[0]]

[[3,7],[6],[4,9],[0]]

[[3,6,7],[0,4,9]]

[0,3,4,6,7,9]
 

As with Binary Search, we can choose to implement the algorithm either recursively or iteratively. Recursively is more challenging to get your head around, but in my opinion produces more readable and clear code. Once you get used to it, it becomes difficult not to start using it everywhere as it is a powerful tool, even though the iterative method might have some computational advantages.

Here are the two options:
(These algorithms being more complicated than those we have studied previously, I have provided very detailed pseudocode, with code comments)

<h5>Recursion</h5>

```
FUNCTION merge_sort(list):
    IF (LENGTH(list) <= 1):                                    #If we have split the list into individual elements
        RETURN list                                            #One individual element is already 'sorted' with respect to itself so we can return it one level up
    ELSE                                                       #Otherwise we have been given an unsorted list which needs to be split and then merged to sort it.
        result = []                                            #This variable will hold the sorted version of the list variable, which will be returned at the end of the function - the function's job is to sort the list variable
        a = list[0 : (LENGTH(list)-1) DIV 2]                   #Treating as inclusive at both ends (check your language docs to see if it is the same there), we take the first half of the list and call it a.
        sorted_a = merge_sort(a)                               #We sort a, calling the same merge sort algorithm on it. This means that it will be split and merged back together sorted in another instance of the function, and miraculously returned sorted.
        b = list[(LENGTH(list)-1 DIV 2)+1 : LENGTH(list)-1]    #Inclusive again, we take the second half of the list and call it b.
	sorted_b = merge_sort(b)                               #We sort b in yet another instance of the function. We now have two separate sorted sides which need to be merged back together.
        WHILE (LENGTH(sorted_a) > 0 OR LENGTH(sorted_b) > 0):  #While at least one of the lists contains items that haven't been merged (while there are any items left to merge).
	    IF (LENGTH(sorted_a) == 0):                        #If there are none left in a, b must contain some. We have already checked the last item in a to find that it is before the first item left in b, and b is sorted already. This means we can just append the rest of b to the sorted list.
		ARRAY_APPEND_ALL_ITEMS(result,sorted_b)                  #Do the appending of all of the remaining items in sorted_b to result.
		BREAK                                          #There are now no elements left to sort in the sorted_a and sorted_b variables, so we can stop this step.
	    ENDIF
	    ELSE IF (LENGTH(sorted_b) == 0):                   #If there are no items left in b, we can add the rest of a to the sorted list as above.
		ARRAY_APPEND_ALL_ITEMS(result,sorted_a)        #Append all of the remaining items in sorted_a to result
		BREAK

            IF (sorted_b[0]<sorted_a[0]):                      #This is the main body of the loop. We repeatedly compare the first (i.e. lowest) values in sorted_a and sorted_b to check which one is lower and should be merged next.
		ARRAY_APPEND(result, sorted_b[0])              #If the first item in sorted_b is lower, we merge that next, and delete it from sorted_b as it has already been merged.
		ARRAY_DELETE(sorted_b,0)
	    ELSE
		ARRAY_APPEND(result,sorted_a[0])               #If the first item is sorted_a is lower, we merge that next, and delete it from sorted_a as it has already been merged.
		ARRAY_DELETE(sorted_a,0)
	    ENDIF
        ENDWHILE
        RETURN result                                          #Return the sorted version of the list variable to the outer function call or simply to the main program once the whole list has been sorted.
    ENDIF
END_FUNCTION
```
<h5>Iteration</h5>
We could save memory in a real implementation by using fewer varaibles, but clarity would be lost.

```

FUNCTION merge_sort(list):
	splits = [[list]] #Looks like [[[3,6,2,4]]] as list is [3,6,2,4] for example. Will become [[[3,6,2,4]],[[3,6],[2,4]],[[3],[6],[2],[4]]]
	WHILE (LENGTH(splits[LENGTH(splits)-1]) != LENGTH(list))): # The first term starts off as 1, then 2, then 4 etc, doubling each time although that depends on the presence of odd numbers. That is to say "while we haven't split the list down to single values"
		thisSplit = []		
		FOR item IN splits[LENGTH(splits)-1]:  #For every value in the current level of splitting
			lengthOfEachHalf = (LENGTH(item)-1)DIV 2 + 1 #Split that in half by calculating how many sub-values should make up the first half(which is always bigger in case of an odd split)
			ARRAY_APPEND(thisSplit,item[0:lengthOfEachHalf-1]) #As in the Recursive implementation we are assuming that the [ra:nge] operator includes both ends. Make the of the current value and append the first new half to thisSplit
			IF (lengthOfEachHalf != LENGTH(item)):#If we are splitting more than 1 single value (as if we are only splitting one, the first half already contains that 1 val.)			
				ARRAY_APPEND(thisSplit,item[lengthOfEachHalf:LENGTH(item)-1]) #Append to the current split the second half of the split list.
			END_IF
		END_FOR		
		ARRAY_APPEND(splits,thisSplit)#We now append the list after the current iteration of splitting to the list splits so that by the end this contains a number of arrays of sub-lists, each array representing a step in the splitting process, up to the final split which is just a list of single values.
	END_WHILE
	results = [splits[LENGTH(splits)-1]] #We initialise the results variable which will contain the merged results at each level, using the final split a the starting point
	FOR i=0 TO LENGTH(splits)-1: # For every time we split the list originally, we want to merge it back up again.
		nextMergeLevel = splits[LENGTH(splits)-2-i] #Peek at the level we are trying to get to in order to know how we want to build back up (we need to know if we are adding two ones, two twos, a two and a one, or maybe just a single one) in order to build back up in the right order.
		thisMergeLevel = [] #This will hold the result of the current merge operation as we conduct it.
		counter = 0 #In order to be able to know how many elements have already been merged, we use this variable to keep track
		FOR item IN nextMergeLevel: #Loop through all values in the next level up (the unsorted version of the one that we are creating), and for each one work out which values at the current level need to be merged to produce a list of the same length.
			itemsToMerge = [] #Will hold the items that need to be merged to form a sorted version of item
			lengthToMerge = LENGTH(item) #The goal is to find a set of elements starting from the beginning of the list that add up to this length.		
			j = 0 #Loop counter variable
			toAddToCounter = 0 #At the end of the loop we add this to counter to allow it to persist over several iterations of the outer loop without affecting the inner loop immediately.	
			WHILE (j <= LENGTH(results[i]) -1 - counter): #Go through every single element at the current level that remains to be merged.
				lengthToMerge = lengthToMerge - LENGTH(results[i][counter+j]) #Subtract the length of this element so we know how many items we are still waiting for.
				ARRAY_APPEND(itemsToMerge,results[i][counter+j]) #Collect the list of items to merge, including this one in it.
				toAddToCounter++ #Increment to allow persistence
				IF (lengthToMerge == 0): #We have found enough sub-lists to merge to make up the same length as the corresponding list at the level above so exit the loop as we don't need any more.
					BREAK
				END_IF
				j++
			END_FOR
			counter += toAddToCounter #Update counter so it takes effect on the next iteration of the loop we are currently inside.
			IF (LENGTH(itemsToMerge) == 1): #If we are only merging one item (because we are going from [2],[1],[3] to [1,2],[3] for example when we merge the 3)
				merged_result = itemsToMerge[0] #We don't need to check the sorting of this single val as it must be "sorted"
			ELSE  #Otherwise we want to merge the two items together keeping the smallest values at the beginning of the merged result
				merged_result = []
				WHILE (LENGTH(itemsToMerge[0]) > 0 AND LENGTH(itemsToMerge[1]) > 0): #While we still have items to compare in the two lists
					IF (itemsToMerge[0][0] < itemsToMerge[1][0]):#We know that these two lists are already sorted, so we either need to merge the first value in one list or the first value in the next list next. Check which one is lower and then merge the correct one so that after this merge the current sub-list stays sorted					
						ARRAY_APPEND(merged_result,itemsToMerge[0][0])
						ARRAY_DELETE(itemsToMerge[0],0)
					ELSE
						ARRAY_APPEND(merged_result,itemsToMerge[1][0])
						ARRAY_DELETE(itemsToMerge[1],0)
					END_IF
				END_WHILE
				ARRAY_APPEND_ALL_ITEMS(merged_result,itemsToMerge[0]) #If all of the items in a are considerably less than all of the items in b for example, we will have merged all of those but there will still be some left in b to merge. These are already sorted as they got sorted when merging last time, so we can just add them straight in.
				ARRAY_APPEND_ALL_ITEMS(merged_result,itemsToMerge[1]) #and Vice Versa
			END_IF				
			ARRAY_APPEND(thisMergeLevel,merged_result) #Having finalised the merge of the current pair of lists, add that to the current merge so that once we reach the end of this level, we can add it to the overall merge
		END_FOR
		ARRAY_APPEND(results,thisMergeLevel) #Having reached the end of the current level, we add to the list of merge levels so that next time we can operate on the merged list we just made to do the next set of merges
	END_FOR
	RETURN results[LENGTH(results-1][0] #At the end, we want to return the final sorted list, which can be found at the final position in the merges list.
END_FUNCTION

```


Notice that in both implementations, because we know we are merging sorted lists, we only need to compare the first values in each of these lists when creating a sorted merge. This is from whence Merge Sort derives its efficiency, reducing hence the number of comparisions required to complete the algorithm.

<h3>Tests</h3>
You should, by now, have a working function to read from files. As such, use the list of integers in the Day 1 Linear Search directory to test the function, sorting these values.
There should be enough (I think 1000) in there that you see a real performance benefit from the use of Merge Sort over Bubble Sort, and you may want to take a look at that with a timer function.

<h3>Extensions</h3>
<ul>
<li>The recursive example above uses an ARRAY_DELETE operation for clarity. Many LLLs don't have dynamically allocated array memory, and require arrays to be of a fixed length throughout program execution. Consider how you could implement the same algorithm without the use of a delete operation, either in one of these LLLs or in an HLL of choice.</li>
<li>The pseudocode provided above uses a less than operator, which means it is designed for integer sorting. Can you make it work for the sorting of strings?</li>
<li>Can you manage to work out the *-1 trick to allow this same function to easily do descending and ascending order sorting? Or maybe you could do it with the less_than() function (as below).</li>
<li>Because I usually implement this algorithm recursively, and it is by no means optimised for iteration, I am not all that confident with my iterative pseudocode. It works, as tested via a Python translation (available in the same directory as this problem formulation) but if you think you can do a more efficient implementation, file a PR or simply use this algorithm in your code and I can link to it from this problem formulation page.</li>
<li>If you have used the recursive implementation, find out your language's maximum recursion depth, and try to calculate what length list would be required to exceed this, causing the algorithm to fail.</li>
<li>Compare the time efficiencies of and calculate the time complexities of both Bubble Sort and Merge Sort to compare the two and get a concrete idea of how much benefit you really do get from switching. 
<li>Take a look at: https://stackabuse.com/merge-sort-in-python/, a great explanation of Merge Sort with some Python Examples. Specifically, try the exercies from the optimisation section, namely:<ul>
	<li>At any given point, we might have an already sorted array chunk which we don't want to waste time splittng down and merging back up. Use another algorithm, bubble sort would be a decent candidate, to check at each stage if you have a sorted sub-list, and then don't waste time adjusting these. This will be of considerable effort to implement, however you will be rewarded by the ability to test the time efficiency of the resulting algorithm against the original merge sort to see for lists of which characteristics you can benefit</li>
	<li>If your language supports it, implement each of the branches of the recursive merge sort splitting as a separate thread, allowing them to be run concurrently. Only the original/final function call has to be run as a whole. This should result in a considerable benefit in the time taken to sort long lists, which will have a large number of recursive function calls. At each level you will, however, require a check to make sure that the two sides being merged have finished being sorted, or some kind of return from the thread before the merge.</li>
</ul>
</ul>


<h3>Hints</h3>

This would be a bit more challenging, but certainly doable. You would need to have variables tracking the position in that you have got to in a and b at each point, to make sure that all values from a and b are succesfully merged. You would need a start_a variable and a start_b variable, each tracking the first value which hasn't yet been "deleted". A subset of values could be passed into the function and returned as normal, though. Another option might be to use the linked list data structure, discussed in previous episodes, which has a pointer at the beginning of the list. You could simply move the start pointer to point to the second element in the list when you delete a value, and free() the memory that was originally occupied by the first structure in the linked list, which would to all intents and purposes be equivalent to deletion of the value.

For the second extension I would probably create a function less_than(a,b) which checks if a is less than b. You would have this function check the type of the two variables, and then compare them, returning a boolean result. If the two variables are of different types, you can invoke an error or try to sort them anyway as we did for Bubble Sort. This should allow the same merge_sort() function to work for both string and integers, with only one change to the conditional expressions, having created the new function.</li>

You can check for an example of the -1 trick in my bubble_sort code. All you need to do is to multiply both values that you are comparing by either 1 or -1, and use the greater than operator, because if we have say 3 and 4, 3 > 4 ---> False but -3 > -4 ---> True, so the order in which the values will end up is reversed.

