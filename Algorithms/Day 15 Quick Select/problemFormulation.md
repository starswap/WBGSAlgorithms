TL;DR - Based on the Quick Sort algorithm, the Quick Select algorithm is used to choose the kth smallest or kth largest element in an array. It repeatedly partitions the list in two in the same way that Quick Sort does, such that the first partition contains the first n elements and the second partition contains the last m elements. Then, if k < n+1, we repeat the process on the first partition. If k = n+1, we know that we have found the answer and return it. Otherwise we operate on the second partition. The non-interesting partition is discarded. Either Hoare's or Lomuto's partitioning algorithm can be used, with Hoare's requiring some additional adjustments. This algorithm is usually implemented recursively. Quick Select can be implemented to select from an array in place. This should be done to create a memory efficient algorithm. Other selection algorithms include Introselect and the Binary Heap method. Implement the Quick Select algorithm, first using Lomuto's partitioning scheme. Then extend either to select from strings as well as numbers, or to use Hoare's method.
<h1>Day 15</h1>
<h2>Quick Select Algorithm</h2>
Having looked at the Quick Sort algorithm a few days ago, I wanted to take a brief detour into selection algorithms, since one of the most popular and most efficient is based on Quick Sort. This algorithm is called Quick Select. [It is recommended that you take a look at the post on Quick Sort before this one as it may be confusing otherwise.]

First, though, what is a selection algorithm? A selection algorithm is an algorithm used to find the kth largest or the kth smallest element in a list. Hopefully you can see the intrinsic relationship between this and sorting, as we could, for example, sort the whole array and then simply count through until we reach position k. Then we would know we had the desired element.

The only difference between this and the algorithm we will talk about today is that Quick Select seeks to optimise this process, realising that there is no point in sorting the whole array if at a certain point in the sort you can be sure that you know the answer. This makes it quicker than simply sorting the whole list.

Before explaining this algorithm, let me make a comparison to Bubble Sort to illustrate this idea. In Bubble Sort, after i passes over the list, the last i elements of the array are correctly sorted, because the swapping process has the effect of pushing the highest or lowest element to the end of the array. This means that after i iterations, we know which element is the ith largest or ith smallest in the array - it is the one we just sorted into place, at position array[length-1-i]. Sorting the array into ascending or descending order allows us to find either the ith largest or the ith smallest element - we are not bound to find only the ith smallest for example. As you can see, this method is much faster than doing a Bubble Sort over the entire array, then choosing the correctly positioned element because this introduces a great level of redundancy.

The same idea applies to Quick Select.

<h3>Algorithm</h3>
As we saw before, the Quick Sort algorithm works in four fundamental steps, the first two of which are related in efficient implementations:
<ol>
<li>Choose a pivot item out of the elements in the array.</li>
<li>Partition the list so that all elements greater than the pivot are after it in the array, and all elements less than the pivot are before it in the array - the array is in essence sorted with respect to the pivot.</li>
<li>Recursively sort the first and second partitions of the array in the same way.</li>
<li>Having split and sorted the array, we merge the separate elements back together. They have already been sorted so all we need to do is put them back into a single array.</li>
</ol>

With Quick Select the first two stages remain unchanged. We still choose a pivot and partition the list.

However, once we have done this, we only need to focus on one of these two partitions instead of both. This is because we know that the elements on the left of the pivot are all below it and the elements on the right of the pivot are all greater than it. This is different to Quick Sort which performs recursion on both partitions instead of just one of them.

The pivot is the ith smallest element in the array where i-1 is its index. This is because the partition sorts the array as such.

As a result, if we are looking for the kth smallest element there are 3 possibilities:
<ul>
<li>k=i: The pivot that we just used to partition the array is the kth smallest element in the array. Therefore this is the answer.</li>
<li>k<i: All elements earlier in the array than the ith element are less than it (since that is how partioning works), so the element we are looking for will be in the first partition. We can discard the second one and only make a recursive function call on the first half.
<li>k>i: All elements later in the array than the ith element are greater than it, so the element we are looking for will be in the second partition. We can discard the first one and only make a recursive function call on the second partition.</li>
</ul>

There is no need to merge the elements in the list back together once they have been split and sorted, because the goal is not to sort the array. This means that the 4th step from Quick Sort is redundant and not used.

As you may imagine, if we wanted to find the kth largest instead of the kth smallest element, all we would need to do is have all of the < signs replaced with > in the algorithm, such that it partitions as if the array was being sorted in descending order instead of ascending order.

Hopefully you can see the link to Binary Search, which uses the same mechanic of repeatedly splitting the array in two and discarding the unwanted half. The difference with Quick Select is that we are searching for an element based on its value compared to the others in the list, rather than searching for an absolute value. This means that we have to include some element of sorting into the algorithm, which is where the link to Quick Sort comes from. There are two other slight differences which is that we don't always split the array in half, and we don't start with a sorted array. These are explored more in the first extension task.

As we discussed in the Quick Sort post, there are many ways to accomplish the partitioning step within each recursive function call. The most popular methods are the Hoare method and the Lomuto method because they work by swapping rather than by insertion which makes them memory efficient, they sort the list in situ, and they only require a complexity equivalent to a single loop over the list and to complete the partitioning. The Lomuto method adapts directly to Quick Select, because we can guarantee that the pivot is sorted into the right place after the partitioning. Lomuto's algorithm returns partitions [start:pivot-1], pivot and [pivot+1:end]. Because we know exactly where the pivot is in the list and that it must be sorted with respect to all of the other elements, we only need to compare it to k in the same way as described above and act accordingly. Then we are done. 

Because of this, Lomuto's method is the one used below in the example. For an explanation of how to adapt Hoare's method to work for Quick Select, first read the <a href="https://github.com/starswap/WBGSAlgorithms/blob/master/Algorithms/Day%2012%20Quick%20Sort/problemFormulation.md">Quick Sort</a> WBGSAlgorithms post, then take a look at the second extension. 

<h3>Example</h3>
Here we will use the Lomuto partitioning method. The goal is to find the 2nd smallest element in the list.

```
[83,190,36,15,748,24,33,22,58,90,800,82] #The pivot is equal to the last element in the list, 82
#Partitioning Step:
	Set i=0, j=0
	list[j] = 83 is greater than the pivot so increment j only. j is now equal to 1 and i is now equal to 0.
	list[j] = 190 is greater than the pivot so increment j only. j is now equal to 2 and i is now equal to 0.
	list[j] = 36 is less than the pivot so swap elements i and j and increment i and j. The list is now [36,190,83,15,748,24,33,22,58,90,800,82]. j is now equal to 3 and i is now equal to 1.
	list[j] = 15 is less than the pivot so swap elements i and j and increment i and j. The list is now [36,15,83,190,748,24,33,22,58,90,800,82]. j is now equal to 4 and i is now equal to 2.
	list[j] = 748 is greater than the pivot so increment j only. j is now equal to 5 and i is now equal to 2.
	list[j] = 24 is less than the pivot so swap elements i and j and increment i and j. The list is now [36,15,24,190,748,83,33,22,58,90,800,82]. j is now equal to 6 and i is now equal to 3.
	list[j] = 33 is less than the pivot so swap elements i and j and increment i and j. The list is now [36,15,24,33,748,83,190,22,58,90,800,82]. j is now equal to 7 and i is now equal to 4.
	list[j] = 22 is less than the pivot so swap elements i and j and increment i and j. The list is now [36,15,24,33,22,83,190,748,58,90,800,82]. j is now equal to 8 and i is now equal to 5.
	list[j] = 58 is less than the pivot so swap elements i and j and increment i and j. The list is now [36,15,24,33,22,58,190,748,83,90,800,82]. j is now equal to 9 and i is now equal to 6.
	list[j] = 90 is greater than the pivot so increment j only. j is now equal to 10 and i is now equal to 6.
	list[j] = 800 is greater than the pivot so increment j only. j is now equal to 11 and i is now equal to 6.
	list[j] = the pivot so swap elements i and j and increment i and j. The list is now [36,15,24,33,22,58,82,748,83,90,800,190]. j is now equal to 12 and i is now equal to 7.
	The pivot is now at element i-1 (6). The first partition is list[0:i-2] inclusive (0 to 5) and the second partion is list[i:end] (7 to end)
Since we are looking for the 2nd smallest element and the pivot is the 7th smallest (0 indexing, sorry), we discard the second partition as the answer cannot be there. It must be in the first partition.
Our new list is [36,15,24,33,22,58]. The pivot element is 58. From now on I will skip the actual partitioning method for brevity. Note that the way we find out k where k satisfies "the pivot is the kth smallest element" is that k=i after the partitioning step.
The partitioned list is [36,15,24,33,22] and 58 is the pivot (a worst case partition). Since the pivot is the 6th smallest element, the answer must be in the first partition as 2 < 6.
Our new list is [36,15,24,33,22]. The pivot element is 22.
The partitioned list is [15] [36,24,33] and the pivot is 22. Since the pivot is the 2nd smallest element, we have found the answer. Return 22.
```
Note that although we choose the pivot at the beginning of each recursive step, before the partitioning, the partitioning is necessary in order to allow us to know at which position in the list the pivot goes. It is this that allows us to know whether or not we have found the element that we are selecting for.

<h3>Pseudocode</h3>

```
FUNCTION lomuto_partition(array):
	pivot <- array[LENGTH(array)-1]
	i <- 0
	FOR j <- 0 TO LENGTH(array)-1:
		IF (array[j] <= pivot):          #In the Wikipedia implementation and many others, only elements less than the pivot are swapped here. This leads to a reduced number of unnecessary swaps which is more efficient although the code is less tidy because you have to make an explicit swap of the last element to put it into place at the end of the algorithm.
			swap <- array[j]
			array[j] <- array[i]
			array[i] <- swap
			i++
		END_IF
	END_IF
	RETURN i-1
END_FUNCTION

FUNCTION quick_select(array,k,left,right):
	pivotIndex <- lomuto_partion(array[left:right]) #Inclusive ranging
	IF (left+pivotIndex == k):
		RETURN array[left+i]
	ELSE IF (left+pivotIndex < k):
		RETURN quick_select(array,k,left,left+pivotIndex-1)
	ELSE: #i must be greater than k
		RETURN quick_select(array,k,left+pivotIndex+1,right)
	END_IF
END_FUNCTION

Get the array as userinput
Get the index k of the element that we want (e.g. k = 1 for the smallest element, 2 for the second smallest element, 3 for the 3rd smallest element) #If you want to be able to do the largest, 2nd largest, 3rd largest etc. you can convert an inputted ath largest value to the equivalent kth smallest value by doing k <- LENGTH(array) + 1 - a. It may also be possible to have the array "sorted" in descending order and then use the original input value, such as by adjusting the less than and greater than signs in the quick_sort function or swapping the partitions over, but clearly the first way is much easier.
k <- k-1 # Convert the userinputted value from 1 indexing to 0 indexing.
IF (k <= LENGTH(array) AND k >= 0 AND LENGTH(ARRAY) != 0):   #Make sure to validate inputs before calling the function.
	OUTPUT quick_select(array,k,0,LENGTH(ARRAY)-1)
END_IF
```
In a memory efficient implementation of Quick Select, we want to make sure to do all of the partitioning in situ (on the original array). I have tried to demonstrate this above, using two extra arguments (left and right) to the quick select function, representing the bounds of the current partition to operate on. The whole array is passed on every function call but each function call only operates within its bounds. In order to avoid copying the array needlessly there is one additional step. In a real implementation you would pass the array by referensortce between the functions rather than copying the actual data, such as with a pointer. You would also not want to pass the array in its entirety out to a partitioning function. The easiest way to reduce this problem is to have the partitioning algorithm within the original Quick Select function, although more passing by reference and returning of indices could instead be used.

<h3>Pros and Cons</h3>
Selection is not a particularly popular open problem, meaning there aren't many algorithms to compare with each other, so it is difficult to categorically state the advantages and disadvantages (which tend always to be comparitive) of one algortihm. These are also not particularly well documented online. Here is what I found:
<table>
<tr><th>+s</th><th>-s</th></tr>
<tr><td>Easy to convert Quick Select to selecting the n smallest elements instead of the nth smallest element or to do largest instead of smallest. This makes it very versatile.</td><td>Unlike Quick Sort, Quick Select does not do multiple simultaneous recursive function calls, because it repeatedly discards half of the array. This makes it unsuitable for processor threading to improve performance</td></tr>
<tr><td>More time efficient than simply sorting the whole array and then choosing the kth element.</td><td>More complicated to program than this approach.</td></tr>
<tr><td>Memory efficient as it can select from the array in place without needing to take up lots of memory. Equally suitable for EEPROM ram for example, where the number of writes is limited, since swapping is used intead of insertion with the Lomuto and Hoare methods.</td><td>While the number of assignment steps might be reduced, the number of iterations for an already sorted list will not be. This means that Quick Select works worst when compared to other selection methods when the list is already sorted.</td></tr>
<tr><td>Compared to a Binary Heap approach, the Quick Select algorithm has a better average case complexity of O(n) compared to O(nlogk). It is also better when we look for a large number of elements such as the lowest 128 elements.</td><td>Binary Heap wins on space complexity, having O(k) compared to O(n) for Quick Select. Equally Quick Select's worst case complexity of O(n^2) makes it unattractive. Binary Heap can make use of a computer's cache in order to allow it to be much faster when looking for the 5 lowest values, for example (source:https://lemire.me/blog/2017/06/14/quickselect-versus-binary-heap-for-top-k-queries/)</td></tr>
<tr><td>Consistent runtime compared to many other algorithms, which is much shorter for longer lists.</td><td>Efficiency declines when a bad pivot is chosen. If the Lomuto method is used we get a worst case when the array is already sorted or reverse sorted as each time we only remove one element - the pivot element - from the list that we are selecting from. </td></tr>
<tr><td>Can be adapted and combined in a variety of ways to produce better algorithms such as Introselect and more: https://en.wikipedia.org/wiki/Quickselect#Variants </td><td>Because the algorithm works on the assumption that it is able to rule out blocks of values, it is not "online" - we cannot add more values halfway through the execution and expect the right answer to be found. This is different to a simple sort and take the first k elements approach.</td></tr>
</table>


<h3>Task</h3>
Adapt your Quick Sort algorithm to produce Quick Select, using Lomuto's partitioning method as it is simple - you may want to shift the partitioning to a separate function which can be called by both Quick Sort and Quick Select. Then test the algorithm (as below). You may want to use file reading to allow your algorithm to operate on large lists, as this is one of the better cases for recursive algorithms like Quick Select by comparison to non-recursive ones.

You may also want to write your implementation of Quick Select such that it works with real numbers and with strings. 
<h3>Tests</h3>
Any array can be used to test your algorithm as long as the k value is less than or equal to the length of the array. Try the files in the linear search directory of the WBGS Algorithms repository or some of these:

[9,4,2,7,1,3,5,8,6] - qs(a) -> a #What other interesting arrays can you find that have a similar property? It turns out that any array containing a reordering of the first x elements of a sequence where the nth term can be wrtten algebraically has the property qs(n) -> nth term of the sequence. This is, perhaps, unsurprising.

[25,45,10,18,19] - qs(1) -> 10, qs(2) -> 18, qs(3) -> 19, qs(4) -> 25, qs(5) -> 45

<h3>Extensions</h3>
<ul>
<li>Adapt the Quick Select algorithm to produce Quick Search. This algorithm will work like binary search, in that it will repeatedly cut the list in two and only search in one of the two partitions. This algorithm presents a linked advantage and disadvantage. + Quick Search can efficiently search a list that is not already sorted. - It isn't as efficient as binary search because the list is not always split exactly in two; it depends on the quality of the pivot choice, which is ultimately random. Work out the complexity of this new search algorithm and compare its performance to Linear Search and Binary Search on a large amount of test data, such as the files in the linear search directory. Assuming an unsorted input list, Quick Search should be faster than sorting and then using binary search as these two steps are sort of combined. Test this hypothesis.</li>
<li>As mentioned above it is possible to use Hoare's original partitioning scheme for Quick Sort with Quick Select, which produces a more efficient, although more confusing, result. Because Hoare's method has the disadvantage that he pivot element and any elements equal to the pivot can end up anywhere in the array at the end of a partitioning step, we don't have the index of the pivot to compare to our goal value k. The pivot can be found in the first or second partition as well, as the partitions are only defined as including elements less than or equal to the pivot and greater than or equal to the pivot respectively. However, this does not matter because we can guarantee that the elements in the first partition are still the n lowest elements in the array where n is the length of the first partition, and the elements in the second partition are still the m highest elements in the array, where m is the length of the second partition. (the only difference is that the pivot could be anywhere within these). As such, we can still split the list and only do recursion on one half of the list, based this time on the length of the first partition rather than the pivot location. At each step, we will only do recursion on one half of the array from the step above because we are still able to determine which half of the partitioned array contains the target value. The problem, however, becomes knowing when to stop the recursion. Because we keep splitting the array, choosing the half of it that contains the target, eventually we will get to an array containing only a single element. Since this array contains the answer only this element can be the answer so we just return this value. (note that this will work even if we get something like [56,56] because, while Lomuto would give us FP:[56], P:56, SP:[], Hoare gives us FP:[56],SP:[56], not FP:[56,56],SP:[]). In summary, to use Hoare's method, two changes are required to the quick_sort() function. Instead of comparing k to the pivotIndex, compare it to the length of the first partition, and convert the base case of the recursion to be when there is only a single element left. I am sure that is exceedingly clear! </li>
<li>Find out about some of the uses of Quick Select and other Selection algorithms in the real world.</li>
<li>We didn't cover any Selection algorithms at GCSE for Computing, as we only looked at Sorting and Searching. Find out about some other Selection algorithms and their advantages and disadvantages.</li>
<li>Use the *-1 trick to allow Quick Sort to sort in descending order and then extend this to Quick Select so that you can find the kth largest element in the array.</li>
<li>Adapt the Quick Select algorithm so that it returns the k smallest or k largest elements in the array rather than the kth smallest or kth largest element. I shan't give a hint for this as it should be very simple.</li>
</ul>

<h3>Hints & Solutions</h3>
<ol>
<li>This should only require a few minimal adjustments. The comparison between k and i should be replaced with a comparison between the value we are searching for and the actual value of the pivot like in Binary Search. The base case of the recursion will also need to be changed such that the algorithm stops if it finds the answer and returns its index (which will need to be tracked, although we are in essence already doing that by tracking the pivot index in Quick Select) and also stops if it doesn't find the answer (the length of the array to be searched is 0) and returns -1.</li>
<li>For some pseudocode check <a href="https://stackoverflow.com/questions/58331986/quickselect-with-hoare-partition-scheme">here</a></li>
<li>Price selection algorithms for eCommerce which have a list of possible prices and need to display the lowest few prices on a website such as Amazon. Combined genetic heuristic algorithms where some heuristic is used to assess the performance of several certain algorithms. The best few are chosen and allowed to "breed" to produce the next generation of algorithms such that the program learns to produce the best algorithm possible. A Selection algorithm would be used to pick the best few to breed. Any use case where you can only make a certain number of choices, say 5, and you want to quickly make sure that your 5 choices are the best (e.g. Drafting of players for sports teams, stock investment...)And many others which I have not mentioned as well. </li>
<li>Introselect,Binary Heap,<a href="https://lemire.me/blog/2017/06/14/quickselect-versus-binary-heap-for-top-k-queries/">and others</a>, <a href="https://en.wikipedia.org/wiki/Selection_algorithm">Wikipedia</a></li>
<li>This works well for algorithms based on sorting. You have an additional argument which is like a boolean representing ascending or descending sorting, but instead of 0 and 1 values you have -1 and 1. When two values are compared, instead of directly comparing them, compare descendFlag*a and descendFlag*b. If the descendFlag is 1 you are comparing a and b as normal, however if it is -1, you compare -a and -b. If a > b, -a < -b and if a < b, -a > -b. If a = b, -a = -b. Hopefully you can see how this works.</li>
<li>No hint, as mentioned above.</li>
</ol>


<h3>Sources</h3>
https://www.youtube.com/watch?v=BP7GCALO2v8
https://stackoverflow.com/questions/58331986/quickselect-with-hoare-partition-scheme
https://en.wikipedia.org/wiki/Quickselect

