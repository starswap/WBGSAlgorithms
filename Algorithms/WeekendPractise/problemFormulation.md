NB - Hints are published at the bottom of the page so if you want to avoid them, don't scroll down!
Having completed this algorithm, don't forget to submit your solution to me to have it featured.

<h1>Getting Started</h1>
<h2>A Divisibility Test for the number 7</h2>

<h3>Problem</h3>

<h4>1. Basic Introduction (~5 mins depending on the language)</h4>
 Using the MOD operator (% in Python), program a function which takes as input an integer and returns True or False depending on whether the integer is divisible by 7. This should be very quick to do, but you will want the resulting function to test your answer to part 2. 

<h4>2. What if we didn't have the % operator? (~20 mins)</h4> 

This version is taken from Introduction to Number Theory by CJ Bradley, published by the UKMT.

We can take any integer and express it in the form:
	10M + R
Where R is the units digit and M is the number of tens.
For example, 342 = 10*34 + 2. Therefore, in this case, M = 34 and R = 2.

Using Modular Arithmetic, (relatively easy to prove, but we will omit here for brevity) we can deduce that any number divisible by 7 will have the property:
	M-2R is divisible by 7 or M-2R MOD(%) 7 = 0.

Without using the Modulo(%) operator which automatically tells you whether the integer is divisible by 7 (as you found out in part 1), but using this new fact, try to program an algorithm which will tell you if a given integer is divisible by 7.

<h3>Tests</h3>
You can test both of these algorithms by checking their results against each other. They should produce the same result. Start by checking the first algorithm by passing in some simple tests:
1. 7 --> True
2. 91 --> True
3. 94 --> False
4. 7777 --> True
5. 77892 --> False

<h3>Extension</h3>
There are in fact many ways to accomplish the task of checking for divisibility. The 1st one is most suited to a computer, and the second to mental calculation. I can think of at least one other way. How many can you think of?


HINTS BELOW














Hint 1: You will need to use either a while loop or a recursive function for this challenge, as you need to continually reduce the number that you are testing. For example, if you get 683 as input, you would do M-2R to get 62, but then you would need to run the same divisibility test on this. Try to work out how you will know when you can stop without using %.





Hint 2: In order to stop the Algorithm, you will need to check how many digits are present in the result of each divisibility test. If there is only 1 digit, then it will either be -7,0,or 7 - hence the number you just checked was divisible by 7, so the original number must have been (we can follow the chain of reasoning back up). Otherwise, you will know that the number was not divisible by 7.






Hint 3: You can make the above check in the condition of your while loop, or as the exit/return test for a recursive function. 
