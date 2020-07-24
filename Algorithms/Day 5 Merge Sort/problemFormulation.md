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
		ARRAY_APPEND_ALL(result,sorted_b)                  #Do the appending.
		BREAK                                          #There are now no elements left to sort in the sorted_a and sorted_b variables, so we can stop this step.
	    ENDIF
	    ELSE IF (LENGTH(sorted_b) == 0):                   #If there are no items left in b, we can add the rest of a to the sorted list as above.
		ARRAY_APPEND_ALL(result,sorted_a)
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

```
#Iterative code will appear here when I have time.
```


<h3>Tests</h3>
You should, by now, have a working function to read from files. As such, use the list of integers in the Day 1 Linear Search directory to test the function, sorting these values.
There should be enough (I think 1000) in there that you see a real performance benefit from the use of Merge Sort over Bubble Sort, and you may want to take a look at that with a timer function.

<h3>Extensions</h3>
<ul>
<li>The recursive example above uses an ARRAY_DELETE operation for clarity. Many LLLs don't have dynamically allocated array memory, and require arrays to be of a fixed length throughout program execution. Consider how you could implement the same algorithm without the use of a delete operation, either in one of these LLLs or in an HLL of choice.</li>
<li>The pseudocode provided above uses a less than operator, which means it is designed for integer sorting. Can you make it work for the sorting of strings?</li>
<li>Can you manage to work out the *-1 trick to allow this same function to easily do descending and ascending order sorting? Or maybe you could do it with the less_than() function (as below).</li>
</ul>


<h3>Hints</h3>

This would be a bit more challenging, but certainly doable. You would need to have variables tracking the position in that you have got to in a and b at each point, to make sure that all values from a and b are succesfully merged. You would need a start_a variable and a start_b variable, each tracking the first value which hasn't yet been "deleted". A subset of values could be passed into the function and returned as normal, though. Another option might be to use the linked list data structure, discussed in previous episodes, which has a pointer at the beginning of the list. You could simply move the start pointer to point to the second element in the list when you delete a value, and free() the memory that was originally occupied by the first structure in the linked list, which would to all intents and purposes be equivalent to deletion of the value.

For the second extension I would probably create a function less_than(a,b) which checks if a is less than b. You would have this function check the type of the two variables, and then compare them, returning a boolean result. If the two variables are of different types, you can invoke an error or try to sort them anyway as we did for Bubble Sort. This should allow the same merge_sort() function to work for both string and integers, with only one change to the conditional expressions, having created the new function.</li>

You can check for an example of the -1 trick in my bubble_sort code. All you need to do is to multiply both values that you are comparing by either 1 or -1, and use the greater than operator, because if we have say 3 and 4, 3 > 4 ---> False but -3 > -4 ---> True, so the order in which the values will end up is reversed.

