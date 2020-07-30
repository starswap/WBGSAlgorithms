<h1>Day 11</h1>
<h2>Shell Sort</h2>
Today we are going back to sorting, but don't worry as we are nearly done. We are investigating the Shell Sort Algorithm, which turns out not to be related to sea shells, naval shells, or bash shells, but rather to have been conceived by Donald Shell in 1959. It makes some substantial improvements to the Insertion Sort algorithm, being in a way a cross between this and bubble sort. It turns out that determining the time complexity of this algorithm and its variants is quite a challenge, but we can say that the basic algorithm has quadratic time complexity in the worst case, meaning it is worse than Merge Sort, but comes out on top of Insertion Sort, Bubble Sort and Selection Sort even though they all have the same complexity O(n^2)

<h3>Algorithm</h3>
Shell sort can be considered a generalisation of Insertion Sort to work for any list size, by taking elements of Bubble Sort. This means that you will need a functioning Insertion Sort Function in order to implement Shell Sort.

The way it works is by repeatedly performing Insertion Sort on sublists taken out of the main list at regular intervals, before finally performing an Insertion Sort on the whole list.

For example:
```
If we have the list [5,7,9,10,3,2,4,6] and we are using 3 as our first interval, we sort (5,10,4),(7,3,6) and (9,2). We then put these back into the list so that elements only occupy positions formerly occupied by elements from the same sublist:

Insertion Sort gives (4,5,10) for the first sublist, so putting that back into the original list we get: [4,7,9,5,3,2,10,6] (Hopefully you can see that elements 0, 3 and 6 have changed)
Insertion Sort gives (3,6,7) for the second interval, so when putting the elements back into the list we get:  [4,3,9,5,6,2,10,7] (Elements 1, 4, and 7 have been reordered)
Insertion Sort gives (2,9) for the final sublist, so when we put that back into the original list, we get: [4,3,2,5,6,9,10,7] (Elements 2 and 5 (8 not in list) have been reordered).

As you can see, by the end of this process the list is much closer to being sorted, because all of the big elements are near the beginning of the list and all of the small elements are near the beginning of the list.

We now finish the algorithm with a standard Insertion Sort at intervals of 1 element, but because of this presorting, Insertion Sort can finish much more quickly. This is because the elements don't have to move as far in the final Insertion Sort to get to their goal position.
```
In the above, we can say that we used a sequence of intervals of 3,1.

There are two things to note about this sequence:<ol>
<li>We do not always have to use these same intervals - Shell Sort is very customisable. The problem with this is choosing a variation that uses a set of intervals that provides the most efficiency.</li>
<li>We can have as many intervals as we like, but note that too many may waste time as you are likely to find increasing numbers of elements that are already sorted, while too few will mean that you are closer to just running a basic Insertion Sort on the list, meaning it will run too slowly as well.</li>
</ol>

Note that by doing these larger interval sorts before a single 1 interval sort, we permit elements to jump more places in the list, which means that even for large lists, Shell Sort can sort efficiently, which is why we often consider it an extension of Insertion Sort. The final 1 interval sort guarantees a sorted result.

Because we can have different list lengths and the right number of intervals depends on the list length, we are advised to calculate the right intervals for each given list, rather than simply to say that we will always use 7 then 4 then 1 for example.

The problem then becomes deciding what method we should use to generate these intervals. There are many possibilities, some of which are documented <a href="https://en.wikipedia.org/wiki/Shellsort#Gap_sequences">here</a> by Wikipedia, but the fun thing about Shell Sort is that you can make your own interval sequence and test it yourself - there isn't a prescribed way to write the algorithm like many of the other ones we have discussed.

For this reason, note that I have moved the interval generation into a separate function. This means that you can start by hard-coding in some values, then produce one interval generation function, then another one, and then another and keep testing them without much change to the code.

Pseudocode:

```
FUNCTION generate_intervals(n): #Try many different ones to see which is the best - but make copies though, don't edit them and lose the ones you had before as you will want to be able to test them against each other.
	intervals <- []
	WHILE (n > 1) #As soon as we get 1 we will stop.
		n <- n/2 #For example, in this case we divide by 2 every time.
		ARRAY_APPEND(intervals,FLOOR(n)) # We need to make sure that we only have integer intervals. You need to make sure that this will give you 1 at the end for every possible n otherwise the final list won't be sorted.
	END_WHILE
	RETURN intervals
END_FUNCTION

FUNCTION shell_sort(list):
	#intervals <- [23,5,2,1] #Just some random values which can be hardcoded - obviously don't choose 23 if you have a short list - this is why we would in reality generate them based on the list length as we can make sure that they are guaranteed to be less than that.
	intervals <- generate_intervals(LENGTH(list)) #Or do it like this - this is a better method but not great for a first try - make a functioning shell sort algorithm with hard coded values first.
	FOR i<- 0 TO LENGTH(intervals): #For every interval in the list.
		currentInterval <- intervals[i]
		FOR k <- 0 TO currentInterval: #Because we need to do the 0,3,6 interval, then the 1,4,7 interval, then the 2,5,8 interval as above.
			currentList <- []
			j <- k
			WHILE (j<LENGTH(list)): #Take the items out of the list in the right places
				ARRAY_APPEND(currentList,list[j])
				j <- j + currentInterval
			END_WHILE
			currentList <- insertion_sort(currentList) #Sort them using insertion sort
			j <- k
			count <- 0
			WHILE (j<LENGTH(list)): #Put the items back into the list in the right places.
				list[j] <- currentList[count]
				count++
				j <- j + currentInterval
			END_WHILE
		END_FOR
	END_FOR
	RETURN list
END_FUNCTION
```

You may be able to improve on the efficiency of this pseudocode, for example by building the insertion sort into the loop rather than using a separate function, which allows for only a loop inside 2 others rather than 3 loops at the centre. If so you can send it in and I will add it, but I will keep this one for clarity.
<h3>Advantages and Disadvantages of Shell Sort</h3>
<table>
<tr><th>+s</th><th>-s</th></tr>
<tr><td>Fastest of the quadratic sorting algorithms, and one of the most efficient sorting algorithms for medium-sized lists. 5 times faster than Bubble Sort, twice faster than Insertion Sort.</td><td>Quadratic complexity makes it worse than Heap Sort, Quick Sort and Merge Sort for most cases, especially long lists, while Insertion Sort is better for short lists.</td></tr>
<tr><td>Relatively simple to understand and to implement.</td><td>Does not have the property of being "stable" like Insertion Sort, meaning it may change the order of equivalent values. This makes it unsuitable for some problems.</td</tr>
<tr><td>Has the property of being "adaptive", meaning it sorts faster when a list is closer to being sorted.</td><td>Not as good as Bubble Sort for verifying whether or not a list is already sorted.</td</tr>
<tr><td>Inherits the property of being "online" from its use of a final Insertion Sort as any items added to the list halfway through can be sorted if necessary just through the final Insertion Sort, or by any of the other sorts before that one. However, unlike for Insertion Sort, we take a performance hit if we don't receive some data until later because this data doesn't have time to undergo as many preliminary sorting steps.</td><td></td</tr>
<tr><td>Like Insertion Sort, it can sort the list in place if implemented efficiently, which means the space complexity is only O(n) + O(1) additional constant space, so the algorithm's memory usage is good.</td><td>However, like Insertion Sort it is not well adapted to embedded systems using memory with a limited write life, because lots of changes are made to the memory when insertions are made.</td</tr>
</table>



<h3>Task</h3>
Implement the Shell Sort Algorithm as a subroutine, and test it using some data we have mentioned in previous editions, e.g. from the Linear Search directory. We haven't mentioned this recently, but it is worth being able to sort both real numbers and strings, so using the lessThan() function idea mentioned previously, try to write a subroutine that allows the sorting of lists of real numbers and of strings. 

<h3>Extensions</h3>
<li>Go onto the Online Encyclopedia of Integer Sequences (<a href="https://oeis.org/">OEIS</a>) and choose some sequence generation functions, or create your own, and test them for a variety of different lengths of list to be sorted. You can use the data and the generation program provided in the Linear Search directory for this test data.</li>
<li>Like we combined Merge Sort and Insertion Sort to produce an exceedingly efficient compound sorting algorithm, could you combine Merge Sort and Shell Sort, using Shell Sort to sort slightly larger lists than were sorted with Insertion Sort? Do you think you will get a performance benefit? Test with time taken or number of iterations required.</li>
<li>We could, in theory, replace all of the calls to Insertion Sort with calls to Merge Sort in the Shell Sort function above. Why would this be a bad idea?</li>
<li>Think about the best,worst and average cases for Shell Sort, and also some applications of it.</li>
<li>Find out about Marcin Ciura and his gap sequence used for Shell Sort.</li>

<h3>Hints & Solutions</h3>
You could try Fibonnaci numbers, powers of any number, prime numbers, odd numbers, 2^k + 1  (as long as you put 1 at the beginning), and many more.

I imagine you will not get a performance benefit but it might be fun to try.

The whole idea behind Shell Sort is that it sorts smaller sub-lists first, then the whole list. Merge sort is inefficient for smaller lists, because it has to undergo a whole split and merge process regardless of list length, so would not sort these efficiently. Secondly, on the final iteration, when we sort with 1 as the interval, Merge Sort would sort the entire list, making the same number of comparisons, even if we hadn't done all of the preliminary sorting, because it is irrelevant for Merge Sort whether or not the list is nearly sorted - it has a very consistent run-time because the same process happens regardless. This means it would be a massive waste of time to do all of the preliminary sorting, which would take ages, and which would make no difference in the end either.

Ciura's gap sequence was derived experimentally to be the most efficient set of intervals for the Shell Sort Algorithm, but it doesn't have a known algebraic generation function.

<h3>Sources</h3>
https://en.wikipedia.org/wiki/Shellsort

https://unacademy.com/lesson/shell-sorting-algorithm-advantages-and-disadvantages/CQSB6V60
