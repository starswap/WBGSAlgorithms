<h1>Day 12</h1>
<h2>Quick Sort Algorithm</h2>
Good Morning folks; today we are continuing our ramble through the sorting sphere, with the Quick Sort Algorithm. After this one we will be looking at Heap Sort, arguably one of the more challenging sorting algorithms, then taking a break from this type of algorithm.

As the name suggests, Quick Sort sorts things quickly. It is one of the best sorting algorithms, with an average complexity of O(nlogn) and a worst case complexity of O(n^2). Being faster than Merge and Heap sort, we can state that it is still hugely popularly implemented today. Both Unix and C use this algorithm as a default standard library routine. 

Like Merge Sort, this algorithm works with a divide and conquer approach. It was developed in 1959 in Russia but by a British Computer Scientist by the name of Tony Hoare.

<h3>Algorithm</h3>
To understand the Quick Sort Algorithm, we first need to introduce the concept of a pivot. This is an element chosen from the array to be sorted, ideally roughly in the middle of the elements in terms of size. 

Having chosen this value, the Quick Sort Algorithm splits the array into two halves:
<ul>
<li>Elements greater than the pivot</li>
<li>Elements less than the pivot</li>
</il>

There are many different ways to do this - please see partitioning schemes below.

Then, having split the array into these two halves, we run the same Quick Sort Algorithm on both. This is where we get the divide and conquer / recursive method, shared by Quick Sort and Merge Sort, from.

Having recursively performed Quick Sort on the different part of the list at every level, we are left with all of the elements from the original list split up in order. We have then to simply combine them to reproduce the orginal list. Unlike in Merge Sort, we don't need to make any comparisons when re-merging; Quick Sort does the sorting in the splitting phase rather than in the merging phase like for Merge Sort. 

We now have a sorted list.

As in the above, the Quick Sort algorithm can be understood to work in three separate steps:<ol>
<li>Pivot Choice</li>
<li>Partitioning (putting elements on the correct sides of the pivot)</li>
<li>Recursively calling the function on both sub-lists / sides of the pivot</li>
</ol>

Here is a brief example:
```
1. ORIGINAL FUNCTION CALL {recursion depth = 1} to sort [90,56,356,1805,35,25,59,09,56,25,167,147,27,46] #Take the final element, 46, to be our pivot.
2. [35,25,09,25,27][46][90,56,356,1805,59,167,147]#Split the list into two halves, preserving the original order. We will go into more detail about how to do this efficiently later, but imagine for now that we iterate over the list, consecutively sending each element either to the less than bucket or to the greater than bucket. We keep the pivot itself separate as we know it goes between the two partitions so we don't need to sort it (we kind of already have). 
3. Call recursively (line 4) to sort [35,25,09,25,27]. Then call recursively (line 16) to sort [90,56,356,1805,59,167,147]. 
4. Return [sorted first half from line 8, pivot = 46, sorted seond half from line 19] to the main loop. This is the entire sorted list. # 

5. NEW FUNCTION CALL {recursion depth = 2} to sort [35,25,09,25,27] #27 is pivot
6. [25,09,25][27][35] #Sublist has been split using 27 as pivot. The second partition of this current split only has one element in so will be returned. We don't need to split it down anymore. 
7. Call recursively (line 9) to sort [25,09,25]. Don't need to call anywhere for the second half as it is only a single element so is inherently sorted.
8. Return [sorted first half from line 12, pivot = 27, second half sorted by default] to line 3. # [09,25,25,27,35]

9. NEW FUNCTION CALL {recursion depth = 3} to sort [25,09,25] #Pivot = 25
10. [25,09][25][-] #Sublist has been split with 25 as pivot. There are no elements bigger than the pivot so we only have one partition to sort. 
11. Call recursively (line 13) to sort [25,09]. Don't need to call anywhere for the empty second half or the pivot as both are inherently sorted. 
12. Return [sorted first half from line 16, pivot = 25, empty second half] to line 7. # [09,25,25]

13. NEW FUNCTION CALL {recursion depth = 4} to sort [25,09] #Pivot equals 9
14. [-][09][25] #There are no elements less than the pivot so we just have the [25] partition that is greater. All partitions are now of 1 length, so we return them. We have reached the recursion base case.
15. Return [empty first half, pivot = 9, second half = 25] to line 11. # = [09,25]

16. NEW FUNCTION CALL {recursion depth = 2} to sort [90,56,356,1805,59,167,147] # Pivot = 147
17. [90,56,59][147][356,1805,167] #List split to two separate partitions using pivot 147.
18. Call recursively (line 20) to sort [90,56,59] and also call recursively (line 23) to sort [356,1805,167].
19. Return [sorted first half from line 22, pivot = 147, sorted second half from line 26] to line 3. # [56,59,90,147,167,356,1805]

20. NEW FUNCTION CALL {recursion depth = 3} to sort [90,56,59] # Pivot = 59
21. [56][59][90] # All elements including pivot are now individual elements, so none of them require further sorting.
22. Return [single first half = 56, pivot = 59, single second half = 90] to line 18. # = [56,59,90]

23. NEW FUNCTION CALL {recursion depth = 3} to sort [356,1805,167] #Pivot = 167
24. [-][167][356,1805] #Lower partition and pivot do not need to be sorted, evidently.
25. Call recursively (line 27) to sort [356,1805].
26. Return [empty first half,pivot = 167, sorted second half from line 29] to line 18. # = [167,356,1805]

27. NEW FUNCTION CALL {recursion depth = 4} to sort [356,1805]. #Pivot = 1805
28. [356][1805][-] # No need to carry out further sorting as we have reached individual elements.
29. Return [single first half = 356, pivot = 1805, empty second half] to line 25. # = [356,1805]
```

Please note the subtle difference in the above compared with Merge Sort. In Merge Sort, when a function receives the return from its two deeper recursive functions, it has to make comparisons to merge the two sorted lists that were received back in the right order. In Quick Sort there is no need for this, as we have a two sorted partitions with the guarantee that all the elements in one are greater than all the elements in the other. This means that as soon as a function received a sorted list from the two functions below it, it simply must concatenate them and then return to the function above it. There is no need for subsequent comparisons. This is demonstrated in the above where the third line in every block of four proceeds straight into the 4th line, without any selection statements being used.

In a sense, this quality of needing only the splitting phase to sort the elements is what makes Quick Sort so quick. 

<h4>Pivot and Partioning Choice</h4>
Although it is useful for understanding roughly how Quick Sort works, the example above leaves out the two most important and customisable parts of the Quick Sort algorithm - these are choosing the pivot, and choosing the (sub-)algorithm we will use to partition the list about the pivot. 

<h5>Pivot</h5>
Although for efficiency reasons we would like to choose the pivot as the exact middle element in the list by value, this would require iterating over the entire array to find the middle element, essentially sorting it in doing so, which would slow down the algorithm very significantly.

There are three other common ways to choose the pivot: choose a random item in the list, choose an item at a fixed position (say first, middle - preferred by the Hoare partitioning scheme - or last - generally used in the Lomuto partitioning method), or use the Sedgewick method (described in the extensions below), which seeks to optimise this choice so that we get an element as close to the middle (by value) of the list as possible. 

<h5>Partitioning Scheme</h5>
A partitioning scheme, almost an algorithm in itself, is a method used to split the list into its two constituent partitions (greater than the pivot and less than the pivot), before these partitions are sorted recursively. We can think of this as sorting the list relative to the pivot element. 

While the definition on the line above is correct, it convenes to point out that good partitioning schemes won't require more memory than the original list - they will be able to partition the list in situ, through the use of swapping. Some basic partitioning methods which do not meet this second constraint would be:
<ul>
<li>Creating two separate arrays, one to hold items less than the pivot and one to hold items greater than the pivot, then iterating over the entire list, appending each item to the correct array.</li>
<li>Choosing the pivot to be the final item in the list, then iterating over the entire list, moving items to after the pivot if they need to be, and leaving items less than the pivot where they are.</li>
</ul>

Instead of these methods, which are relatively memory and time inefficient, although maybe easier to understand, we generally use one of two efficient partitioning schemes:<ul>
<li>Hoare Method</li>
<li>Lomuto Method</li>
</ul>

<h6>Lomuto Method</h6>
This method, considered simple but inefficient in real use, is attributed to Nico Lomuto.

We use an index i which tracks the last element in the list which is guaranteed to be below the pivot (this is i-1), and an index j which is used to iterate over the whole list.

When j encounters an element less than the pivot, we swap this element with the element at position i, so the element at position i is now also in the right place. We then increment i such that the rule that all elements up to and including i-1 are below the pivot is preserved.
```
Taking the example from before, [90,56,356,1805,35,25,59,09,56,25,167,147,27,46] with a pivot of 46, the final element in the list, i and j both start as 0.
1. Array[j] is 90, which is greater than the pivot so nothing happens. Increment j only.
2. Array[j] is 56, which is greater than the pivot so nothing happens. Increment j only.
3. Array[j] is 356, which is greater than the pivot so nothing happens. Increment j only.
4. Array[j] is 1805, which is greater than the pivot so nothing happens. Increment j only.
5. Array[j] is 35, which is less than the pivot. Swap it with Array[i], which is Array[0] and add one to i. This means the array is now [35,56,356,1805,90,25,59,09,56,25,167,147,27,46] and i is now 1. The next swap will be made into Array[i] which is Array[1], which makes sense as it will keep the smaller elements together. i-1 is 0, so all elements in the array up to and including 0 are less than the pivot and in the right place. Increment j.
6. Array[j] is 25, which is less than the pivot. Swap it with Array[i], which is Array[1] and add one to i. This means the array is now [35,25,356,1805,90,56,59,09,56,25,167,147,27,46] and i is now 2. The next swap will be made into Array[i] which is Array[2], which makes sense as it will keep the smaller elements together. i-1 is 1, so all elements in the array up to and including 1 are less than the pivot and in the right place. Increment j.
7. Array[j] is 59, which is greater than the pivot so nothing happens. Increment j only.
8. Array[j] is 09, which is less than the pivot. Swap it with Array[i], which is Array[2] and add one to i. This means the array is now [35,25,09,1805,90,56,59,356,56,25,167,147,27,46] and i is now 3. The next swap will be made into Array[i] which is Array[3], which makes sense as it will keep the smaller elements together. i-1 is 2, so all elements in the array up to and including 2 are less than the pivot and in the right place. Increment j.
9. Array[j] is 56, which is greater than the pivot so nothing happens. Increment j only.
10. Array[j] is 25, which is less than the pivot. Swap it with Array[i], which is Array[3] and add one to i. This means the array is now [35,25,09,25,90,56,59,356,56,1805,167,147,27,46] and i is now 4. The next swap will be made into Array[i] which is Array[4], which makes sense as it will keep the smaller elements together. i-1 is 3, so all elements in the array up to and including 3 are less than the pivot and in the right place. Increment j.
11. Array[j] is 167, which is greater than the pivot so nothing happens. Increment j only.
12. Array[j] is 147, which is greater than the pivot so nothing happens. Increment j only.
13. Array[j] is 27, which is less than the pivot. Swap it with Array[i], which is Array[4] and add one to i. This means the array is now [35,25,09,25,27,56,59,356,56,1805,167,147,90,46] and i is now 5. The next swap will be made into Array[i] which is Array[5], which makes sense as it will keep the smaller elements together. i-1 is 4, so all elements in the array up to and including 4 are less than the pivot and in the right place. Increment j.
14. j is the final value in the list. Since we set the pivot to the final value at the beginning, we know that this value is the pivot, which doesn't need to be sorted. i is now the first item in the second partition, with i-1 the last item in the first partition as it always has been. This means we have: firstPartion = Array[0:i-1] inclusive, secondPartition = Array[i:j-1] inclusive, and pivot = Array[j]. Now we can do the recursive function calls on each of the partitions as explained above, then return [sortedFirstPartition,pivot,sortedSecondPartition] again as above.
```
In order to reap the benefits of the fact that Quick Sort can sort an array in place, you would likely use pointers, passing the partition to sort to the deeper recursive function by reference rather than by value, however for a first implementation and for understanding, creating separate variables firstPartition and secondPartition, passing those to create sortedFirstPartition and sortedSecondPartition, is fine.

<h6>Hoare Method</h6>
Hoare himself, the inventor of Quick Sort, used a different method to partition the array. 

The pivot was chosen as the middle element of the list. 

He then took two indices, one at the beginning and one at the end of the list, and moved each one towards the other until it pointed to an element that was on the wrong side of the pivot or equal to the pivot (as in it could go on either side). The indices would be moved independently.

Once the two elements pointed to were one greater than, one less than the pivot element, and they were in the wrong relative order (on the wrong sides of the pivot), he would swap them.

This would be repeated until the pointers collided without any swaps.

```
Here is an example with the same array as in the two previous ones: [90,56,356,1805,35,25,59,09,56,25,167,147,27,46]. The pivot is 59, the middle element.
1. i is 0
2. Move i from 0 towards the end of the list until we find an element on the wrong side of, or equal to, the pivot. The first element, 90 meets this description. 
3. j is 13
4. Move j from 13 towards the beginning of the list until we find an element on the wrong side of, or equal to, the pivot. The last element, 46, meets this description.
5. Swap elements at index i (0) and index j (13) in the list, to get [46,56,356,1805,35,25,59,09,56,25,167,147,27,90]
6. i is still 0. Move it towards the end of the list until we find an element on the wrong side of, or equal to, the pivot. The element at index 2 (365) meets this description.
7. j is still 13. Move it towards the beginning of the list until we find an element on the wrong side of, or equal to, the pivot. The element at index 12 (27), meets this description.
8. Swap elements at index i (2) and at index j (12) to get [46,56,27,1805,35,25,59,09,56,25,167,147,356,90]
9. i is still 2. Move it towards the end of the list until we find an element on the wrong side of, or equal to, the pivot. The element at index 3 (1805) meets this description.
10. j is still 12. Move it towards the beginning of the list until we find an element on the wrong side of, or equal to, the pivot. 25 at index 9 meets this description.
11. Swap elements at index i (3) and at index j (9), to get [46,56,27,25,35,25,59,09,56,1805,167,147,356,90]
12. i is still 3. Move it towards the end of the list until we find an element on the wrong side of, or equal to, the pivot. The element at index 6 (59) meets this description.
13. j is still 9. Move it towards the beginning of the list until we find an element on the wrong side of, or equal to, the pivot. The element at index 8 (56), meets this description.
14. Swap elements at index i (6), and at index j (8), to get [46,56,27,25,35,25,56,09,59,1805,167,147,356,90]
15. i is still 6. Move it towards the end of the list until we find an element on the wrong side of, or equal to, the pivot. Element 8 meets this description.
16. j is still 8. Move j towards the beginning of the list until we find an element less than the pivot. Element 7 meets this description.
17. i > j so we know we have searched and partitioned the whole list. 
18. The algorithm is split into a lower partition Array[0:j] and an upper partition Array[j+1:LENGTH(Array-1)]

As above, we now perform the same sorting process on the partitions. 
```

Be aware of the need to move both pivots separately and check individually whether they have encountered a wrongly partitioned element, not simply to check 0 and 13, then 1 and 12, then 2 and 11 together, for example, as some swappable pairs may be missed. We need to include elements equal to the pivot so that the pivot itself can be moved in case it is physically but not numerically in the middle of the list at the beginning.

Although it seems as though we are doing lots of nested loops, Hoare's method actually confers speed advantages when all values are equal, when the values are already sorted (if the middle element is chosen to be the pivot), and on average (3 times fewer swaps according to Wikipedia) because we never reset i and j, so we are actually simply looping through half of the list in one direction and half in the other direction, which equates to looping over the whole list once only.

The choice of pivot is both separate from and linked to the choice of partitioning algorithm. For efficiency, it is illogical to choose the beginning or the end of the list as the pivot for Hoare's method, as this worsens the algorithm's time complexity when all elements are equal or when the list is already sorted, producing a worst cae of O(n^2). However, there is some choice. We can choose the middle element by index, or we could use Sedgewick's method, described in the third extension below. 

<a href="https://en.wikipedia.org/wiki/Quicksort">Wikipedia</a> reminds us that with very long lists of elements, by the end of the splitting stage, it is very likely that we will start to get lists that are already sorted or which contain few unique elements. For this reason, Sedgewick's pivot choice or using the middle value is well worth doing - it doesn't just apply to contrived situations.

Please note that unlike the with the Lomuto partitioning scheme, in Hoare's method we cannot guarantee that the pivot is in the right place until the end of the sort. This means that where we did a recursive sort on the elements [0 to p-1] and [p+1 to end], and then added in [p] when returning on the 4th line of every block above, we must instead do [0 to p] and [p+1 to end], joining only two blocks together for the return.

Final note to make - regardless of the partitioning scheme we must avoid creating an infinite recursion by creating a zero-length partition. This can be fixed when the partitioning is created through skillful rounding, or by adjusting the base case of recursion to count both zero and one. 


<h4>Pseudocode</h4>

FUNCTION quick_sort_lomuto(list): #Please note that this code was created with help from the Wikipedia page on Quick Sort.
	IF (LENGTH(list) <= 1):
		RETURN list
	ELSE:
		pivotIndex = LENGTH(list)-1
		i = 0
		FOR j = 0 TO pivotIndex:
			IF (list[j] < list[pivotIndex] AND i != j): #At the beginning we would get some occasions where we would be trying to swap an element with itself, which is non-sensical. This is why I use AND.
				swap = list[j]
				list[j] = list[i]
				list[i] = swap
				i++ #i in essence is holding statically onto the first element that is greater than the pivot, so we can replace it with an element less than the pivot, and fire it towards the end of the list. Th 
			END_IF
		END_WHILE 
		firstHalf = list[0,i-1] #Inclusive ranging as always
		secondHalf = list[i,LENGTH(list)-2]		
		RETURN ARRAY_CONCAT(quick_sort_lomuto(firstHalf),list[LENGTH(list)-1],quick_sort_lomuto(secondHalf))
	END_IF
END_FUNCTION

FUNCTION quick_sort_hoare(list): #Please note that this code was created with help from the Wikipedia page on Quick Sort.
	IF (LENGTH(list) <= 1):
		RETURN list
	ELSE:
		pivotIndex = LENGTH(list)-1 MOD 2
		WHILE (1 == 1):
			DO 
				i++
			WHILE list[i] < list[pivotIndex] #Find an element in the first half that belongs in the second half
		
			DO 
				j++
			WHILE list[j] > list[pivotIndex] #Find an element in the second half that belongs in the first half
			IF (NOT(i<j)):
				firstHalf = list[0,j] #Inclusive ranging as always
				secondHalf = list[j+1,LENGTH(list)-1)]
				RETURN ARRAY_CONCAT(quick_sort_hoare(firstHalf),quick_sort_hoare(secondHalf))
			ELSE
				swap = list[i]
				list[i] = list[j]
				list[j] = swap
			END_IF
		END_WHILE
	END_IF
END_FUNCTION

<h4>Summary of the Pros and Cons of Quick Sort</h4>
<table>
<tr><th>+s</th><th>-s</th>
<tr><td>In practice 2 to 3 times faster than Merge Sort and Heap Sort, despite having the same complexity. This makes the algorithm popular and often pre-implemented.</td><td>Efficient implementations are unstable which means that equal elements do not remain in the same order after sorting, although by sacrificing space efficiency, it is relatively easy to achieve a stable sort.</td></tr>
<tr><td>Does not require much auxiliary memory usage - array can be sorted in place, reducing the algorithm's space complexity.</td><td>Relying on recursion of list halves, it does not work well in an online setting - you cannot add extra values halfway through sorting.</td></tr>
<tr><td>Can be run "externally", that is to say to sort disk files efficiently, as well as sorting lists in memory. This is more space efficient than external Merge Sort, and more time efficient than most other external algorithms.</td><td>Unlike Merge Sort and most of the other sorts we have talked about, Quick Sort is not efficient when run against data to be sorted stored in a linked list data structure, because elements cannot be accessed without first passing through all of the elements before. Choosing a good pivot becomes inefficient and so we have to settle for a poor pivot. We also have difficulty with reverse iteration as in Hoare's method unless we have a doubly linked lists.</td></tr>
<tr><td>Elegant recursive implementation makes it relatively simple to code.</td><td>On the other hand, getting to grips with the algorithm is challenging, especially with the different partitioning schemes.</td></tr>
<tr><td>More consistent runtime than most quadratic sort algorithms, which is much shorter for longer lists, although generally worse for shorter ones.</td><td>When the pivot chosen (regardless of the method) turns out to be a bad choice, the efficiency of the algorithm rapidly diminishes. This does diminish the stability of the algorithm to some extent. The worst case complexity is worse than most other competitive sorting algorithms.</td></tr>
<tr><td>Works well with threading, caching and other efficiency improvement techniques</td><td>Not "adaptive" - if a list is nearly sorted, there is no performance benefit when compared to a random list.</td></tr>
<tr><td>Highly extenisble and combinable, allowing for the production of more efficient algorithms like Samplesort, Introsort, Quick-Insertion Sort, Quick Select (which we will investigate in the coming days), external quick sort and many others, to accomplish the same task more quickly or other similar tasks.</td><td></td></tr>
<tr><td>Better than insertion sort because it uses swaps so limits the number of writes to memory, and the possibility of an external sort reduces the risk of long-term damage to short write life memory. Generally, swapping > inserting. </td><td>Because of its consistent run-time, it is nowhere near as good as Bubble Sort for verifying that a list is sorted.</td></tr>
</table>

<h3>Task</h3>
Implement the Quick Sort Algorithm using the Lomuto scheme, then implement the Hoare one. You may like to implement the partitioning step as a separate function to allow for easy code switching. 

<h3>Tests</h3>
Test the algorithm using a list of integers and strings, such as the ones published in the Linear Search directory, as usual. You can split this up into smaller blocks if you want to test different size inputs (build a wrapper function that splits the input up.)

You will want to test the algorithm using a variety of different data characteristics: Random (the integer files are already random, for the strings file input them then randomly reorder the words), Nearly Sorted (sort using this or another algorithm then randomly swap some elements), Many Identical Elements (take the first few elements of one of the files and for each word add it to the list to be sorted a random number of times from 1 to 4.), Reverse Sorted (sort the list to be sorted using any sorting algorithm, then reverse it) among others. 

<h3>Extensions</h3>
<ul>
<li>Test the efficiency of the Lomuto and Hoare partitioning schemes with a large list, using your timer function from a previous edition of the project. Investigate which one should be faster by running the algorithm through yourself by hand, and seeing how many steps are executed for each of the two algorithms.</li>
<li>Find out about another possible partitioning scheme for the algorithm and implement it. Maybe you could even invent your own and test it against the standard ones used.</li>
<li>When Quick Sort was first implemented, we used to use the first or the last elements as the pivot, with Hoare's partitioning scheme. This gave a particularly inefficient algorithm when the array in question was sorted or reverse sorted. As such, we switched to using the value at the middle index in the array as the pivot. However, a better solution is to use the median of the first, last and middle elements in the array. This was proposed by Robert Sedgewick in 1975 in his thesis about the algorithm. Try all of these different options and collect some evidence to demonstrate that Sedgewick's method is the best.</li>
<li>Find out about the Sample Sort algorithm, which can be thought of as an extension of Quick Sort, and try to implement it.</li>
<li>Use processor threading to allow your algorithm to simulataneously sort both partitions, rather than doing one and then the other. If you have already implemented Sample Sort, extend that as well to ue multithreading. Now test the threaded and non-threaded versions of Quick Sort against each other in terms of time efficiency and see which one works the best. </li>
<li>Try using a combination of Insertion Sort and Quick Sort, like we did with Merge Sort. Insertion Sort is very fast for short arrays, so have it sort the arrays once they get to below a certain length threshold, rather than going through the whole splitting and merging process, which is quite slow. That way you should be able to produce a hybrid algorithm which works well regardless of list length. Experiment to find a good threshold value choice. 
<li>Why is Quick Sort's complexity O(n log n), that is to say log linear?It turns out to be very simple.</li>
</ul>

<h3>Hints & Solutions</h3>
For the third extension, you should find that Sedgewick's method produces a pivot much closer to the numeric middle of the list, which means that the partitions should be closer in size to each other, which improves the efficiency of the recursion. Note that the pivot can actually be an element that isn't in the list with this pivot choice - it doesn't really matter as long as all of the elements progress to the next recursive step.  

4. https://en.wikipedia.org/wiki/Samplesort
This algorithm is optimised for multi-core processing systems. The basic idea is to use Quick Sort with more than two separate partitions. If we are to have p partitions that include an entire array, we must define them by their edges. For example, partition one might contain elements from 1 to 5, partition 2 from 5 to 10, partition 3 from 10 to 18, partition 4 from 18 to 23 and so on. In Sample Sort we pick p-1 elements at random from the list and sort them. Then, these elements are interpreted to represent the edges that define our partitions (like the pivot in Quick Sort except because we have more than two partitions, each partition needs two dividers). We put the elements into the requisite partitions like we did in Quick Sort, then repeat the process.

For example if we had [78,34,15,80,99,4,6,72,3] and we had 4 cores on our  system, we might use four partitions. We would choose 3 random elements, say 34, 99, and 6. The first partition is for elements less than or equal to 6 [4,6,3]. The second partition is for elements that are between 6 and 34 [34,15], and the final partition is for elements from 34 to 99 [78,80,99,72]. As you can see we might have done better to choose 72 instead of 34 to equalise the size of the partitions, but that is the nature of random choices. We have the partitions but they now need to be sorted. We will sort them recursively as in Quick Sort. Once a small number of elements is reached it is common to switch to Insertion Sort for example to speed up the process a it is optimised for short lists.

5. Check these links for more information:

https://www.youtube.com/watch?v=pMK-jcOAYI8

https://www.w3schools.com/HTML/html5_webworkers.asp


https://www.youtube.com/watch?v=SnU9m0uDG8M

https://realpython.com/intro-to-python-threading/


https://www.tutorialspoint.com/multithreading-in-c

https://www.youtube.com/watch?v=nVESQQg-Oiw

You will need to work out how to return values from the threads so that the sorted subarrays can be re-combined to produce a sorted final array. This will be the main challenge. Also note that if you are using Repl.it you cannot be certain of the specs of the processor you are being virtualised - you might only get one core so using threading will just provide an additional overhead, and the threads will be executed through context switching, never at the same time, which won't help. Instead, make sure to test this on a device which you know has multiprocessing capabilities.

7. It turns out that regardless of the partitioning scheme in use, it takes 1 iteration over the entire list to do this, plus about 1 extra iteration in Hoare's method. This is a complexity of O(n). The splitting happens until we get to single elements, halving each time. This means that if we have four elements, in the best case we will split to 2 and 2, then to four individual elements - this is 2 steps, which is log2(4). Putting that together, we "do" n iterations log n times, which leads to a complexity of the two multiplied together, that is to say O(n log n) 



