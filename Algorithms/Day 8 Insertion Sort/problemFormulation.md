TL;DR - Both Insertion and Selection Sort can be used to sort lists. They both have Quadratic time complexity, but Insertion Sort beats Selection Sort in all aspects except number of writes to memory, which is important in some applications. It is useful to know both to help with remembering the other one. In Selection Sort we repeatedly put the next lowest element at the beginning of the list, by swapping it into place. We find this minimal element by a single pass through the entire list. In Insertion Sort we don't need to make passes through the list. We repeatedly take the next element that we haven't sorted (using unsorted order not minimum-maximum). We insert this item at the right place in the sorted beginning of the list, shuffling all items along so that this section is always sorted, although does not always contain the lowest elements in the list. After k iterations of Insertion Sort, the first (k+1) elements of the list are sorted but not necessarily the right (k+1) elements until the end. 2 significant advantages of Insertion Sort are the fact that you can add more elements halfway through the sort, its efficiency for small lists, and its limited amount of memory usage as it sorts in situ. Make Insertion Sort (or both of the algorithms), and consider implementing the combination sort described in the first extension. 
<h1>Day 8</h1>
<h2>Insertion Sort</h1>
It's Monday and we are returning to sorting algorithms for today, to investigate the Insertion Sort Algorithm. It isn't mentioned in the A Level or the GCSE Specification, but it is a relatively simple and efficient algorithm, and it has a very interesting use case (see first extension).

This algorithm has quadratic (O(n^2)) time complexity, much like Bubble Sort, but it turns out to be much more efficient when used on shorter lists in practice

Here are some other advantages and disadvantages of Insertion Sort, taken in part from the <a href="https://en.wikipedia.org/wiki/Insertion_sort">Wikipedia</a> page on this algorithm.
<table>
<tr><th>Pros</th><th>Cons</th></tr>
<tr>Very simple to implement.<td></td><td>{}{}{}</td></tr>
<tr><td>Efficient for small data sets, compared to Merge Sort and Heap Sort but also to Bubble Sort and other quadratic algorithms.</td><td>Slow for large data sets as the result is built one item at a time.</td></tr>
<tr><td>Like Bubble Sort, very efficient for data that is nearly sorted (I refer you back to https://www.toptal.com/developers/sorting-algorithms)</td><td>{}{}{}</td></tr>
<tr><td>Like Bubble Sort, the relative order of equivalent elements is not changed, which could be significant for some applications.</td><td>{}{}{}</td></tr>
<tr><td>Again like Bubble Sort, we don't need much extra memory other than that of the original list (space for 1 item) which is a significant advantage when compared to Merge Sort.</td><td>{}{}{}</td></tr>
<tr><td>We can, halfway through sorting, give the algorithm a load more data and it will be able to sort it at the same speed as if it had had it all from the beginning. This is not the same as Merge Sort, for example, which in a classic implementation could not deal with extra values that were not split and merged with the original list. This property is known as "online" - the algorithm works in the "online" setting.</td><td>{}{}{}</td></tr>

It is useful to note that manual sorting of items by a human who can see all of them, such as for playing cards, often uses a method similar to Insertion Sort.
</table>

<h3>Algorithm</h3>
It turns out that a good way to understand and remember Insertion Sort is to compare it to the inferior Selection Sort. These algorithms are both very simple so you shouldn't have any trouble understanding them.

<h4>Selection Sort</h4>
Very simply, selection sort makes repeated passes through the entire list of values, checking for the minimum (by whatever mesure is being used to sort) value that has not yet been sorted. Having passed over the entire list, it swaps the minimum value that was just located into the position that it should go into, with the original value in that position going to where the minimum was. For example:

```
[4,2,6,3,4,5,9,10,3] -> Pass through list to find that 2 at position 1 is the lowest value
[2,4,6,3,4,5,9,10,3] -> Swap 4 and 2 around so that 2 is in the correct place at position 0. Pass through the list to find that 3 at position 3 is the lowest value.
[2,3,6,4,4,5,9,10,3] -> Swap this 3 into position 1 by swapping with the 4 formerly in that position. Pass through the list to find that 3 at position 8 is the lowest value.
[2,3,3,4,4,5,9,10,6] -> Swap this 3 into position 2 by swapping with the 6 formerly in that position. Pass through the list to find that 4 at position 3 is the lowest value. 
[2,3,3,4,4,5,9,10,6] -> Find that this 4 is already in the right place. Pass through the list to find that 4 at position 4 is the lowest value.
[2,3,3,4,4,5,9,10,6] -> Find that this 4 is already in the right place. Pass through the list to find that 5 at position 5 is the lowest value.
[2,3,3,4,4,5,9,10,6] -> Find that this 5 is already in the right place. Pass through the list to find that 6 at position 8 is the lowest value.
[2,3,3,4,4,5,6,10,9] -> Swap this 6 into position 6 by putting the 9 that was there into position 8. Pass through the list to find that 9 at position 8 is now the lowest value.
[2,3,3,4,4,5,6,9,10] -> Swap this into position 7, sorting the array by putting 10 into the last position. Because there are 9 elements and we just sorted the 8 lowest, we know that the last one must be greater than all of these, and so in the right place so we can stop. 
```
(<a href="https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif">Here</a> you can see an animation which demonstrates the same idea).

In the same way that Bubble Sort guarantees that the last k elements are sorted after k iterations, Selection Sort guarantees the sorting of the first k elements after k iterations. This means you can optimise the algorithm a bit by looping from one position later in the list each time.

Unlike Bubble Sort, however, on every pass selection sort makes only one swap and these swaps do not have to be of consecutive items.

I shan't give code for Selection Sort as it is very simple and should be clear, and I don't want to spoil it in case you want to implement it for comparison.

I will, however, give the hint that it is primarily an iterative algorithm. 

<h4>Insertion sort</h4>
Insertion sort is essentially an improved version of Selection Sort, which works in the opposite direction. Although it has the same average-case complexity, it is more efficient than Bubble Sort for small lists, and Selection Sort for all lists.

In the Insertion Sort algorithm, we move from the beginning to the end of the list, one item at a time, making in essence only one pass through the list.

For each item we encounter, we insert it into the first part of the list so that it is sorted relative to the items before it in the list, so that we build up a sub-list in which all of the values are sorted relative to one another of first 1 then 2 then 3 then 4 ... values at the beginning of the list. 

When an insertion is made, all elements between the position that the new element came from and the position that it went to are shifted one space to the right. These are always all of and exclusively all of the elements that have already been sorted but which are greater than the value being inserted. 

What distinguishes this from other sorting algorithms is that these values are not necessarily the first k values in the whole list - all we know about them is that they are relatively in order.

Here is an example of Insertion Sort, using the same numbers as for Selection Sort so you can compare: - Please remark that the first k items are always in order, where k is the number of iterations we have made.  

```
[4,2,6,3,4,5,9,10,3] -> First, we look at the first item and insert it at the beginning of the list so that it is sorted relative to all of the items we have seen already (itself only), starting from the beginning. This means that we do nothing to the list
   |
   2                 -> Next, we look at the second item, which is two. We compare it to all of the items we have seen already, going <strong>backwards</strong>(implementation note) from its position. So we check it against 4, finding that it is less than 4, so it needs to be inserted before 4. Because there are no other elements before 4, it is inserted at the beginning of the list.
 |<-
[2,4,6,3,4,5,9,10,3] -> The result after inserting 2.
     |
     6               -> Then, we look at the third item in the list, which is six. We compare it, going backwards to 4, and then we would compare it to 2. However, we do not need to do both of these comparisons, because, having compared it to 4, we know it is greater than the largest element in our "sorted beginning", so it goes at the end of this section, becoming the new final element - hence we leave it where it is. 
     |
[2,4,6,3,4,5,9,10,3] -> The result after inserting six.
       |
       3             -> We look at the fourth item in the list, 3. We compare it successively with 6 and 4, finding both times that 3 is lower. Hence, we check it with 2, which it is greater than. Thus, we insert it into the list between 2 and 4, keeping the beginning sorted. 4 and 6 are shifted right
   |<--|
[2,3,4,6,4,5,9,10,3] -> As you can see, multiple elements can all be moved in one go (difference when compared to Selection Sort, which uses swapping), and one element can move more than 1 place in one go (difference when compared to Bubble Sort) 
         |
         4           -> Now, we check the fifth item in the list, 4. We compare it with 6 and find that 6 is greater, so we can't insert yet. We compare with the next value,4 and find that they are equal, hence the test is not greater than the item to be inserted, so we can insert just after. This is important to maintain the property of the algorithm that it keeps equal values in order, as if you used a wrong greater than or equal sign instead of greater than for example, you would lose this benefit of this particular algorithm.
       |<-
[2,3,4,4,6,5,9,10,3] -> You can see that after 5 steps, the first 5 values are correctly ordered with respect to each other, although we don't have the first 5 elements in the final list (which would include 3 and 5)
           |
           5         -> Next, we check the sixth item in the list. It is less than 6, so can't be inserted at the end of the sorted section. We compare it to 4 and find it to be greater, so correctly insert it between 4 and 6
         |<-
[2,3,4,4,5,6,9,10,3] -> The result after inserting 5 - we have shifted six along to make space for 5. (Try not to think of these short moves as swaps - they are removals and reinsertions - this will help with understanding larger jumps like the final one shown here.)
             |
             9       -> Now, we check the seventh item in the list. We compare it to 6, and find that it is greater. Hence, we can insert it straight away at the end of the sorted section (which is equivalent to leaving it where it was)
             |
[2,3,4,4,5,6,9,10,3] -> No change has been made, as you can see, because 9 was already sorted with respect to the beginning of the list.
               ||
               10    -> Then, we check the eighth item in the list, which is 10. We compare it to 9, finding that it is greater. We thus can insert it straight away at the end of the sorted section, leaving it where it is.
               ||
[2,3,4,4,5,6,9,10,3] -> There has been no change to the array after this insertion.
                  |
                  3  -> We check the ninth item in the list, which is 3. We compare it to 10, then to 9, then to 6, then to 5, then to 4, and then to then to 4, keeping going each time because these numbers are greater than 3, the number to be inserted. Then, we compare to the 3 that is already in the list, finding that this is not greater than the 3 we are inserting, so we can insert this value between the 3 and the 4 already in the list.
   |<-------------|
[2,3,4,4,5,6,9,10,3] -> We have iterated over every element in the list (k=LENGTH(list)-1 using zero-indexing), so we would know that we had finished and if we were using a loop, we would have reached the end - there would be no more iterations.
```


Notice that finding an already sorted element that is less than the value we are inserting is the key trigger to do the actual insertion. while the test is greater than the value being inserted, we need to check the next value before we insert, unless we reach the beginning of the list.


*Implementation Note - in a real implementation you would skip the first step here as the first item is always sorted to itself. Hence, you would actually have the first k items in order after k-1 steps, as the first step was skipped.

Here is some pseudocode for the Insertion Sort algorithm:

Here is a graphical example for Insertion Sort https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif


<h3>Task</h3>
Implement Insertion Sort in your chosen language, and test it on some input data. You can make selection sort as well if you like, but it is generally considered to be inferior in all aspects but one, so wouldn't generally be worth using in reality. The one exception given by Wikipedia is that of a system (such as an embedded system) which uses memory that is damaged by writing / has a very short write life. This is because Insertion Sort makes more writes to the memory than Selection Sort as each time an insertion is performed, we slide every greater element one space to the right to accommodate the added element. In Selection Sort you only have to make 1 swap for each insertion.

<h3>Tests</h3>


<h3>Extensions</h3>
<ul>
<li>This extension is thanks to https://stackabuse.com/merge-sort-in-python/ - In the Optimisation section at the bottom, you will see the suggestion to combine both Merge Sort and Insertion Sort to create a very efficient sorting algorithm for both long and short lists, as Merge Sort is most efficient for long lists, while Insertion Sort is optimised for short ones. Implement this and try a variety of different thresholds for when we should switch to insertion sort, testing these against each other and against basic Merge and Insertion sort for lists of different lengths. You will want to use a timer function to test these; you could average the times returned across the different lengths to get a single real number evaluation metric to compare the algorithms with. Make sure not to just switch to insertion when the orginal list is short, but to do it to sort short lists that we have got from splitting, so you don't split down all the way to individual elements before merging. I recommend editing the base case of your recursive Merge Sort function to make this happen.</</li>
<li>Calculate - Empircally or using the times returned, the complexity of this combined funtion. Find out the threshold for when sole Insertion Sort becomes slower than sole Merge Sort in terms of list length. </li>
<li>Compare the efficiency of Bubble Sort and Insertion Sort by comparison of time of execution, then swap out the calls to insertion_sort() in your combined function for calls to bubble_sort(). Check the time efficiency of the resulting function, especially with comparison to the Merge/Insertion combination. Notice the power of this functional approach - you can easily swap in and out different base sorting algorithms to use within Merge Sort in order to find the best.</li>
<li>Can you implement Insertion Sort recursively? It won't be useful or efficient, but it could be a fun challenge. You can then compare the efficiency loss with the original one. Wikipedia offers a solution if you get stuck.</li>
<li>Implement the ability to interrupt the insertion sort halfway through to add more values to be sorted, simulating a website, for example, that receives more input on the server side from the client.</li>
<li>Try to understand why the time complexity of the Insertion Sort algorithm is quadratic - it is quite an easy one to understand.</li>
<li>It is widely commented on the Internet that a linked list data structure is 
</ul>

<h3>Hints & Solutions</h3>

1:
```

FUNCTION MergeInsertion(list,threshold):
	IF (LENGTH(list) < threshold):
		RETURN insertion_sort(list)
	ELSE
		#Insert your previous merge sort code here, making sure that the recursive function call is made to the same MergeInsertion function, not the original merge_sort function so as to benefit even when the original list is larger than the threshold as we will sort the littler lists produced by the splitting process by Insertion Sort.
ENDFUNCTION
```
Wikipedia predicts the resulting threshold at around 7-50 elements, depending on the language and environment. The reason Insertion sort is quicker than Merge Sort is partly because it is non-recursive and so requires fewer function calls than Merge Sort, each of these costing time. We can see this by thinking about the fact that Merge Sort has to split down the array then build it back up again regardless of its size, wheras insertion sort can just do a couple of swaps in a short array. More comparisons are made by Insertion Sort for a large list, but for a short list the number of comparisons is similar and the overhead cost is worse for Merge Sort.


4:You could do this by threading, or by two separate programs which both edit the same file. Have the insertion sort read in from the file on every iteration to update its variable if changes have been made. You would want to turn off this feature unless it was necessary for the setting in which Insertion Sort was being used, as it will slow it down. You could use a boolean parameter flag which defines whether or not this code should be executed. You could then have only 1 function that works in either setting.

5:It is because we have a nested loop - we loop through all values in the list to find the values to insert, then loop over them again to work out where to insert. If we just had one nested loop, we would only add one extra iteration for every extra value added to the list - this would be linear complexity, but because we have both loops, we add an extra number of comparisons which is in the order of n (worst case) throughout the whole of the inner loop by the addition of one extra element to the end of the list. This is why the complexity is n^2. If we double the list length, instead of having double the number of iterations to make like for a single loop, for each of these we have double the number of iterations as well because of the inner loop - so we quadruple the total number of iterations, which is equivalent to quadratic complexity. 

#Need to finish tests and pseudocodde. 
