<h1>Day 2</h1>
<h2>Bubble Sort algorithm</h2>
<h3>Problem</h3>
Continuing the series on sorting and searching algorithms, we are going to tackle today the Bubble Sort algorithm. There are two reasons behind this:
<ol>
<li>Firstly, it is the next easiest of the 4 sorting and searching algorithms from GCSE, and probably the simplest sorting algorithm.</li>
<li>Secondly, in order to program Binary Search, the next searching algorithm in the schedule, we need a sorting algorithm because Binary Search only works on a sorted list.</li>
<li>Thirdly, we want some variety - we don't want to do all searching then all sorting or vice versa.</li>
</ol>

Before we start the implementation of this algorithm, I'd like to reference a fantastic site which demonstrates the efficiencies of different sorting algorithms for different dataset characteristics:
	https://www.toptal.com/developers/sorting-algorithms

Also, here's a link that may bring back a few memories:
	https://www.youtube.com/watch?v=lyZQPjUT5B4

The bubble sort algorithm (found here: https://en.wikipedia.org/wiki/Bubble_sort) has quadratic time complexity or O(n^2). This means that when the data set size is doubled, the amount of operations required to complete the algorithm is quadrupled.
In this algorithm, we will do the following:
<ol>
<li>Make repeated passes over an unsorted list.</li>
<li>On each pass, we will iterate over the entire list, item by item.</li>
<li>For each item, we will compare it to the next item in the list.</li>
<li>If they are in order, we do nothing.</li>
<li>Otherwise, we will swap them around so that they are in order.</li>
<li>We will repeat this procedure until we reach the end of the list, then start a new pass</li>
<li>Although the maximum number of passes required can be calculated (since every pass guarantees 1 extra item in order at the end of the list, e.g. the first pass puts the highest value in place, for example.), this guarantees a worst case scenario in terms of run-time.</li>
<li>As such, we tend to make a check on every pass of whether a value has been changed on that pass. <ul><li>If yes, keep going as we are still in the process of sorting.</li> <li>If no, then stop as we have sorted the list.</li></ul></li>
</ol>

<h3>Task</h3>
Produce an program implementing the bubble sort algorithm.
Unlike with searching, we can only sort on arrays of a single data type. This means you may need to write separate functions for strings and numbers, although this depends on the language in question.

<h3>Extension</h3>
<ol>
<li>Sorting provides a nice opportunity to use one of my favourite tricks in computing, the multiplying by -1 trick to reverse the action of something. First, see if you can create a function that accepts an argument corresponding to whether the list should be sorted in ascending or descending order, of 1 or -1 respectively.</li>
<li>Now, try to see if you can adapt the algorithm such that you don't need any conditional logic to accomplish this, using the fact that we have chosen 1 and -1 as our parameter values. Maybe you managed it from the beginning. You likely will only be able to do this for real number sorting, but maybe you can find an implementation that works for strings</li>
</ol>

Here are the extensions from yesterday, which could also work for this sorting algorithm:
<ol><li>First, create a function which can take inputs from the code, and hard-code in a list and a target value to pass to the function.</li>
<li>Then, look to take user input of the list to sort (You will need to ask for the list length then use a loop to take input this many times, or you could have the user space out each item with a certain separator</li>
<li>However, as we know, these sorting algorithms are most useful on large amounts of data, which cannot be sorted easily by hand. Create some code that reads in a csv or \n separated file which represents the list to be sorted</li>
<li>You can use the test data files from yesterday to check that your file reading and sorting works, and for a large data set to test the time efficiency of the algorithm</li>
<li>If you created the function yesterday that takes another function as an argument and times its execution, you shouldn't have that much to do up to this point. You could, hence, look to practically (as opposed to empirically), calculate the complexity of this algorithm. You do this by repeatedly running the function with different data set sizes, and finding the average comparitive increase in time when the data set size is (say) doubled. You should find that the time taken quadruples, leading you to the correct conclusion that this algorithm is of quadratic complexity, although the increase could be slightly more depending on the efficiency of your implementation. You will need to start with a large data set to do this computation. You could use your timer function from yesterday, altering it to take a list length as an argument and having it truncate the list to that length before running the sorting algorithm, for example. Then put this timer in a while loop where you double the counter variable each time, passing this as an argument.</li>
</ol>

Again, if you have any other ideas for extensions, send an email, file an issue or create a pull request by editing this file and I will add them in here.

<h3>Tests</h3>
Your program should be able to sort any list of all real numbers or all strings, into numerical or alphabetical order.

As mentioned above, You can test this with any list of values, sorting by hand to check the result, or you can use yesterday's integers or words lists to test this program.

E.g. (With all steps listed for completeness of algorithm test)

```
[7,5,6,3,1] 
[5,7,6,3,1]
[5,6,7,3,1]
[5,6,3,7,1]
[5,6,3,1,7]
NEW PASS
[5,3,6,1,7]
[5,3,1,6,7]
NEW PASS
[3,5,1,6,7]
[3,1,5,6,7]
NEW PASS
[1,3,5,6,7]
BLANK FINAL PASS
END ALGORITHM
```

HINTS BELOW

I can't really think of any constructive hints for today, except one:
	If you are having trouble exiting the loop after a pass which makes no change, use a boolean (or binary int.) flag, "changed",which is set as False at the beginning of every pass. When a change is made, set to True. The while loop's condition should reference this flag.
