*If you want to time yourself each day to see how long it takes you to produce these programs, by all means email me your times and we can have a daily leaderboard. This will depend on whether you are doing it in an HLL or an LLL and your skill level. 
*Also if you get stuck, send me your code on my school email (external students you can search in school gmail by typing a name) and I will take a look. I can do PHP,JS,Python,C,Octave, among others so I should be able to have a go at fixing any issues. 

<h1>Day 1 of the WBGS Algorithms Project!</h1>
<h2>Linear Search algorithm</h2>
<h3>Problem</h3>
For the first few problems of the WBGS Algorithms project, I am proposing a foray into sorting and searching algorithms. We will attempt to build up from the most basic ones studied at GCSE, for a quick reminder, to some more challenging algorithms which we will be seeing at A Level.

The series starts today with the Linear Search Algorithm: https://en.wikipedia.org/wiki/Linear_search.
As we know, this is probably the most basic searching algorithm in existence. As such, it is very slow, especially for big data sets.
It has linear complexity O(n), which means that in the worst case scenario (you have to go right to the end of the list to find the value), doubling the number of items in the list means doubling the number of comparisons made.
This is different to Binary Search, for example, which we will explore later this week, and which adds only 1 extra comparison for a doubling of the list size.

In the Linear Search Algorithm, we very simply iterate over the list of items to search amongst, comparing each one with the target value.
If the target value is found, we output the index at which the target was found.
If we reach the end of the list, we output that the value was not found. 

<h3>Task</h3>
Produce an program implementing the linear search algorithm, for integers and for strings. If you are using an LLL, you might like to tackle these two separately, but in Python it should be fine to do it all in one go, as you can even have mixed value type lists.

<h3>Extension</h3>
Since this is quite a simple algorithm, there are plenty of ways to extend it. The problem is choosing ones that don't morph the algorithm out of recognition.
I would recommend adjusting the way in which you input into the function.
<ol>
</li>First, create a function which can take inputs from the code, and hard-code in a list and a target value to pass to the function.</li>
<li>Then, look to take user input of the list and of the target. (You will need to ask for the list length then use a loop to take input this many times, or you could have the user space out each item with a space, then split with a string split manipulation command).</li>
<li>However, as we know, these searching algorithms are most useful on large amounts of data, which cannot be searched easily by hand. Create some code that reads in a csv or \n separated file which represents a list of items within which to search. (In PHP you might prefer to serialise). Now get user input of the target item, and then pass these two into your function.</li>
<li>I have provided some sample data in the problem folder, which is a large list of integers separated by new lines, but you could also produce your own as another extension, perhaps taking the two example generation programs in C and Python as examples.</li>
<li>Finally, we want to be able to test the comparitive efficiencies of our sorting and searching algorithms, once we have done all of them. Consider how you would do this, and produce a program which can test them</li>
<li>Additionally, you could try to make the algorithm work to search for single characters or substrings inside strings</li>
</ol>

If you have any other ideas for extensions, send an email, file an issue or create a pull request by editing this file and I will add them in here.

<h3>Tests</h3>
I have included a file of integers and of strings which can both be searched once you have written a program that can read from a file.

Otherwise you can enter any array and search from that, e.g.:


Find 'a' in ['a','b','c','d','e'] 



HINTS BELOW

For the final extension task, you will need to have implemented your searching algorithm as a function, ideally as part of a library or header file.

Then you want to produce some test data or get the data from this folder.

You want to write another program which will serve as an outer shell to the algorithm. This program will start a timer, run the algorithm and then stop the timer.




To start a timer, you can simply get the current time in seconds since the Epoch in 1970, and do the same at the end. Then subtract the difference. You don't actually need to start a timer as a child process.





You want to be able to do this with your other searching and sorting algorithms once we have made them, so I would recommend producing a function which can test other functions.

The way you would do this is by passing a reference to the searching algorithm to the test function. The test function would then do all of the testing, and return a simple time taken value for the execution of the function on the test data, which would also be passed as a parameter:

This would be implemented like this, for example:


FUNCTION tester(input_data,*function_to_test)

	original_time <- GET CURRENT TIME

	function_to_test(input_data)

	GET CURRENT TIME

	end_time <- GET CURRENT TIME

	RETURN end_time - original_time

END FUNCTION

It turns out to be more or less easy to achieve this depending on the language you have chosen.

In a LLL like C, you can pass a function pointer pointing to function_to_test to tester, and have tester call the function passed in as an argument by dereferencing the pointer.

In Javascript, I believe that functions are variables just the same as any other, so it should be possible to pass the function without brackets to tester, then call it as normal inside.

As for other languages, it could be more difficult but hopefully you can adapt these examples to your language of choice. 

