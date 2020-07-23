TL;DR - Make the Binary Search Algorithm in your chosen language and test it on some arrays. This algorithm searches a sorted list of values by each time finding the middle value in the list, and comparing it to the target. If the target is later in the list, the middle and everything before it is discarded. If it is earlier, the middle and everything after it is discarded.

<h1>Day 4</h1>
<h2>Binary Search Algorithm</h2>
<h3>Problem</h3>
Returning to the GCSE Sorting and Searching algorithms (Yawn! Some new content before the end of this week, I promise.), it's time to tackle the Binary Search Algorithm. This algorithm requires a sorted list to of values, because it uses the inherent ordering of the list in order to search it.

The Binary Search algorithm has logarithmic complexity O(log(n)). This means that for every multiplication of the list size by a fixed constant, another fixed constant is added to the number of iterations of the algorithm required to complete the searching. In this case, doubling (x2) the list size results in adding 1 extra operation, x4 = +2. x8 = +3 and so on. More generally, multiplying the list size by a given number y results in floor(log2(y)) more comparisons.

As a result, the algorithm is both time and space (memory) efficient. This is because it is quick to execute, and we could literally free up the memory holding the deleted halves of the list each time, rather than just point to the new start.

The Binary Search algorithm works as follows: (As ever I have tried not to give away the exact implementation to avoid making the task trivial, given the algorithm's simplicity)

```
WHILE we have more than 0 elements left in the list:
	Take the middle element of the list by DIViding the (length-1) by two (quotient. Add one again at the end if your language indexes from 1)
	Compare the target to the middle element.
	IF the target is greater than the middle element:
		Discard the first half of the array and the middle element as the target cannot be in this range
	ELSE IF the target is less than the middle element:
		Discard the second half of the array and the middle element as the target cannot be in this range
	ELSE   
		The target has been found at the current index. 
		RETURN TRUE or the index that the target was found at.
ENDWHILE
RETURN FALSE or -1 depending on implementation//If the algorithm gets to here, then we have not found the target
```

As you can see, on each iteration of the loop, if the target is not found, there are two possibilities, each involving the halving of the array length. This is why we call the algorithm binary search, as it chooses in each case from two (bi-) possibilities. 

Here are some pros and cons of the Binary Search Algorithm. Refer back to these when we get to the A* Search Algorithm, to see if it will resolve some of Binary Search's issues.
<table>
<tr><th>Benefits</th><th>Disadvantages</th></tr>
<tr><td>More time and space efficient (less complex) than linear search</td><td>Requires list to be sorted in order to be able to act upon it. This makes it difficult to adjust the list later, so in databases for example this is not ideal. In addition, this slows down the search process if you do decide to pre-sort an unsorted list.</td></tr>
<tr><td>More consistent run-time than linear search, shorter for longer lists (max comparisons of log2(n)+1 instead of n for linear search. Average log2(n)+1 compared to n/2</td><td>More complicated to program than Linear Search; possibility of making mistakes with a recursive function, although many standard library functions already implement this algorithm for you.</td></tr>
<tr><td>Unlike some algorithms such as merge sort, the search can be done on the original list</td><td>Some types do not have an inherent less than/greater than relationship, so cannot be sorted and thus cannot be binary searched - this isn't that common as you often wouldn't want to search them if you can't sort them but it can happen.</td></tr>
<tr><td>It is is slower than some faster methods such as hash tables, but equally a less complex data structure (a simple array) is required for the data</td></tr>
</table>


<h3>Task</h3>

Today's task is to produce an implementation of the Binary Search Algorithm, which should work on sorted lists of numeric values (real numbers) and strings (sorted alphabetically).

<h3>Tests</h3>
You can re-use the file of integers and of strings which can both be searched once you have written a program that can read from a file, which are present in the Day 1 Linear Search directory.

Otherwise you can enter any array and search from that, e.g.:

Find 'a' in ['a','b','c','d','e']


<h3>Extensions</h3>
<ul>
<li>Combine your Bubble Sort and Binary Search algorithms (if they are written as functions this should be easy), in order to allow an unsorted list to be entered by the user or read from a file, and to be searched with Binary Search.</li>
<li>Compare the efficiency of this sort and then search with a simple linear search for different sized lists. You could do this by time, but also a count of the number of operations required would be useful. Equally, I recommend considering the different possible list characteristics - that is to say their inherent ordering or lack of order, and see if this makes a difference. As a graphical reminder of the importance of list characteristics, although this is for sorting: https://www.toptal.com/developers/sorting-algorithms</li>
<li>This algorithm can be effectively implemented using both an iterative (loop-based) and recursive (fucntion which calls itself) approach. You will find both of these to be useful in the future for algorithms which are so complicated one way that they lend themselves to the other method. Try both. The benefit of recursion is that your code is easier to understand, although you lose some efficiency and the limited maximum recursion depth can become an issue. Iteration is useful because it is more computationally efficient in most cases, and easier to program if you aren't familiar with recusion, although not suited to some specific tasks.</li>
<li>Having implemented both approaches, compare their efficiencies using a timer or an empirical method (by counting the number of assignment statements for example), thus considering the complexities of the different methods and how well they would scale to larger datasets. It depends on the algorithm and how well each implementation occurs, but you may well find a discrepancy, because the time efficiency or complexity of an algorithm <strong>is</strong> implementation dependent, even though it is machine independent.</li> 
<li>A close cousin of the Binary Search Algorithm is the Binary Search Tree Data Structure. This structure can be more efficient than an array for the addition and deletion of values. This is because we would have to shift all of the values after an added value to the right such that we could keep the array in order, permitting binary search to be carried out on the updated array. A binary search tree does not require this because it has its own internal indexing which is used instead of the indexing of the array that holds the values. This means we can much more cheaply make adjustments to the tree. See the hints section for a link and a more detailed explanation. If you are interested in data strutures and their characteristics and operations, investigate linked lists which are popular in LLL. You will find out why they are not ideal for binary search, despite permitting easy addition of values in a sorted way.</li> 
<li>The Binary Search algorithm requires a sorted list, but this list can be sorted in any way as long as this is consistent with the implementation of the search algorithm. Using an HLL permitting mixed-type lists, program an implementation of the algorithm which allows for a mixture of strings and integers in the same list, defining a convention for how they should be compared and hence sorted. You could expand this to work for your bubble sort algorithm, so that the user can enter these values in any order.</li>
<li>In the same vein, consider all of the possible data types as well as real numbers, integers, strings and chars. Choose one and make an implementation of a sorting algorithm and of Binary Search which effectively defines a convention for how we can sort data of this type, and hence search it with Binary Search.</li>
</ul>



HINTS BELOW

For the first extension task you will want to have a separate function that reads from a file and returns an array of values to search, unless your language already offers this, so that you can re-use this in the future. You will then want to apply the sort to the extracted data, then the search.

For the second extension, you will want to add an extra count variable to your program, then add an update to this variable after every assignment statement to allow these to be counted. This is computationally inefficient and a bit confusing, of course, but you would take these lines out when the algorithm is really being run.

Here is some (detailed) pseudocode for the recursive approach:

```
FUNCTION binary_search(list,start,end,target): //list is the array to search amongst, start is an index from 0 
	IF (start == end):
		RETURN False//We have an empty list to sort, so not found no matter what target equals
	ENDIF
	current_index <-- (start+end) DIV 2 //current_index becomes the middle index in the remaining part of the list
	IF (list[current_index] == target): //We have found it!
		RETURN True //Or return current_index
	ELSE IF (list[current_index] > target)://We are looking to late in the list
		end <-- current_index - 1 //Discard the second half
		RETURN binary_search(list,start,end,target)//Re-run binary search on the remaining list
	ELSE //list[current_index] must be less than target.
		start <-- current_index + 1//Discard the first half
		RETURN binary_search(list,start,end,target)//Re-run binary search on the remaining list
	ENDIF
ENDFUNCTION

arr = ['a','b','c','d','e']//e.g.
targ = 'b'//e.g
binary_search(arr,0,LENGTH(arr)-1,targ)
```

Generally, when trying to decide if a recursive approach to an algorithm would work, you can use the assumption that any algorithm which works iteratively will work recursively, although this doesn't tell us whether or not recursion is a good idea. Ultimately, it works best when you need the answer to a sub-problem before you can get the answer to a given problem, and these problems use the same algorithm. In this case, to find out if the item is in the list, we discard half of the list, but we still need to know if the item is in the remaining half.



For the Binary Search Tree extension:<br />
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/1200px-Binary_search_tree.svg.png" />
In a Binary Search Tree, we store each value from our original array as a "node". This is usually an object or dictionary with three properties, namely: value,left,right.

We then create an array of these structures, which represents a tree. This is done by finding the middle value in the array we want to store, and creating the first structure to represent this value. We leave the left and right values blank for now. Then, we operate on the two sub-arrays either side of the middle element, finding their middle and creating a structure for those (you can see how this relates to Binary Search, and how we might implement this as a recursive function)

Each time a new structure is created, we update the node on the level above to link these two together. If the value we just made is greater than the node on the level above, it is "connected" to the right branch, and if it is less than the node above, it is connected to the left branch. You could use pointers or simply store the left and right values as an array index. We repeat this process until we create a full structure, such as the one below:

```
[{value:8,left:1,right:2},
{value:3,left:3,right:4},
{value:10,left:NULL,right:7},
{value:1,left:NULL,right:NULL},
{value:6,left:5,right:6},
{value:4,left:NULL,right:NULL},
{value:7,left:NULL,right:NULL},
{value:14,left:8,right:NULL},
{value:13,left:NULL,right:NULL}]
```
^ This represents the tree in the image above.

As you can see, because we give the indices of the connected values in the left and right properties, it doesn't matter whether the values are actually in order in the array or not, or even what order we put them in. This means we can very easily add a new value to the end of the array, complete a binary search to locate where it should be added, and then update the relevant L and R positions.

Here is a better explanation of the relationship between these two constructs https://stackoverflow.com/questions/21586085/difference-between-binary-search-and-binary-search-tree



In terms of Linked Lists:
<ul><li>A Linked List is a data structure in which many separate variables are linked together into a list, each one pointing to the next one in the list. Each element is a structure containing the value at this position in the list, and a pointer pointing to the next one of these structures. New values can easily be spliced into these lists by creating a new variable and adjusting the pointer values so that the item before points to this new variable, which points to the item after insertion. The problem is that they can only be accessed sequentially. Without going through the entire list, it is impossible to know how many items are in the list, as you only know at each element whether there is or isn't a next one. In the same way, you cannot access a linked list at any given index without passing through all of the indexes before this one in order to locate the position of the element you want. This requires so much computation that for a linked list, Binary Search is generally no better than Linear Search.</li>
<li>For an explanation of this data structure: https://www.youtube.com/watch?v=t5NszbIerYc</li></ul>

For the penultimate Extension, you could, for example, sort all strings alphabetically and all numbers numerically when they appear ajacently. To decide if a string or a real number should go first when data of two different types are adjacent, convert the first letters of the strings to their positions in the alphabet, or for more compatibility, try ASCII values. If the letter and number match, for example andy and 65, you will need to move onto the second letter. Here we see that andy is longer than 65, which represents just a single a, and so should go after. If two values are logically equivalent in your convention they can go in any order as for numerical or alphabetic sorting. Don't forget that other ways to sort these values exist, so don't be afraid to consider your own interpretation.

In terms of data structures, for a real challenge you will want more complicated abstract structures that don't have an inherent sorting. You could try:
<ul>
<li>Functions - Maybe number of lines - you need to work out a tiebreaker</li>
<li>Graphs - Maybe by number of nodes - you need to work out a tiebreaker</li>
<li>Arrays - within the outer array</li>
<li>Dictionaries</li>
</ul>

