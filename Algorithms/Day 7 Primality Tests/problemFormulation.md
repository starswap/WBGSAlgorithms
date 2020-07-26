TL;DR
<h1>Day 7</h1>
<h2>Primality Tests</h2>

Rather than a single complex algorithm, for the WBGS Algorithm puzzle this Sunday, we are going to launch into an exploration of two simple algorithms, both of these being of the same type - primality tests.
That way you can implement as many as you have time for, and still have an implementation of something to show for it even with little time.

To begin with, what is a primality test? Well put simply and logically it is a test to determine whether or not a given integer is a prime number, returning a boolean result after applying some mathematical process to the integer. The most simple test for primality is repeated division (often attributed to the Greek mathematician Eratosthenes, especially when used to bulk-test lots of values by ruling out those that feature in multiplication tables, instead of by division). We simply divide by all prime numbers up to the square root of a given integer, essentially discovering factors of the integer. If no prime below its square root wholly divides the integer, we know that it is a prime number, and can thus use it in a test of greater integers.

It turns out that there exists a real plethora of primality tests, but which fall into two main categories, those being determistic tests and probabilistic tests. A determistic test applies a (usually more complex) algorithm to determine categorically whether or not an integer is prime. On the other hand, probabilistic tests are usually simpler and faster algorithms, that are run many times with different inputs (often these involve an integer which either does or doesn't divide a given value which relates to the integer to be tested). With each passed test, the probability of the number being prime increases, and we often know this exact value, although it depends on the algorithm as to whether or not we can reach certainty. In many algorithms, we name the test cases passed 'witnesses' - The more witnesses to the primality of the number, the more likely it is prime.

The challenge in implementation is balancing the computational load of many, many iterations of a probabilistic algorithm/a very long and complex deterministic algorithm and the probability that the number is prime. In some applications, it is absolutely critical that a chosen number is prime, whereas in others we can sacrifice this certainty in order to improve the speed of returning a result. We call composite numbers that pass primality tests pseudoprimes.

We might solve this by using <strong>both</strong> types of test in one implementation. Imagine we have a lot of calculations to do involving a certain number, but we only want to do them if it is prime. We can optimise the speed of the algorithm by using a probabilistic test at the beginning, to make sure we aren't wasting our time, then start the calculation. At the same time we run a slower determistic test, so by the end we have the answer to the calculations and certainty that the original number was prime.

Wolfram MathWorld (see sources) helpfully and astutely points out that probabilistic tests never falsely identify prime numbers as non-prime, as they couldn't otherwise be considered a primality test. They are proved to always work for prime numbers but not always for composites in most cases. For this reason we sometimes say that they can test a number for "composite-ness" as we know for sure that a number is composite if the correct result is returned, but if the result for primality is returned, we can't be sure.

Some primality tests use numbers (Rabin-Miller, repeated division) already known to be prime to check if the number to be tested is prime. These primes are called the bases used in the tests in many cases.


These are the two algorithms we will investigate today for primality testing:
<ol>
<li>The Fermat Test, based on his Little Theorem (probabilistic). One of the simplest primality tests aside from the Sieve of Eratosthenes</li>
<li>Rabin-Miller test. This test is deterministic up to 3.4*10^14 using the first seven primes as its "bases" (thanks go to StackOverflow - see sources), but otherwise probabilistic.</li>
</ol>

I encourage you to implement as many of them as you can, then compare their accuracies and efficiencies.

<h3>Algorithms</h3>
<h4>Fermat Test</h4>
Fermat's Little Theorem states that for any prime number p and any number a that is not a multiple of the prime number:

a^p-1 &#8801; 1 mod p

We can deduce from this a test for primality by putting the number to test into the equation as p.

For example, to test 9:

We ask the question Is a^8 mod 9 &#8801; 1?

There remain two questions to answer. How do we choose a? Does this test guarantee primality? The answer to the second question is no - it is a probabilistic test. In order to increase the likelihood that the result returned by the test is correct, we repeatedly try a values, building up a list of "witnesses" to the primality of the number.

As soon as any of these witnesses tells us that p is not prime, we can stop and return this result.

Otherwise, we set a certain threshold for when we will stop trying (as we need to think about speed here) and return true (or technically "probably prime") if all of the results up to this point attest the primality of the number.

There isn't really a set threshold to use in this case, so we would often implement the test as a function with a parameter k. This parameter represents how many times we should try before giving up. The higher the value chosen, the more likely the result returned is correct.

We should make sure to pick the a values randomly in the range 2 to n-2 inclusive, as 1 and n-1 are not useful in this context, because it is proved that all integers, and then all odd integers will satisfy these equations (source:Wikipedia)


Quick Note - you can only test values greater than three for primality using this test.


There are, unfortunately, some composite numbers which will pass the test no matter how many different a values are tested. These are called Carmichael Numbers or Fermat Pseudoprimes. They satisfy the property that:

a^m &#8801; a (mod m) for all a values up to m, where m is the Carmichael number These are some examples: 561, 1105, 1729.

These numbers satisfy Fermat's Corollary Equation which is equivalent to the first equation, but in a different form: k^p &#8801; k (mod p) for any integer k, and so they satisfy the original equation, which is why they end up being pseudoprimes.

As a result of this problem, the Fermat Test is flawed and has a lower accuracy than other tests. We should now examine a better test, the Rabin-Miller Test.

<h4>Rabin-Miller Strong Pseudoprime Test</h4>
This test is very similar to the above, being in fact based on the Fermat Test, as it uses his Little Theorem. However, it is much more accurate than the Fermat Test, and as mentioned above has been proven to be determistic and correct up to 341,550,071,728,321, using the first seven primes as its "bases". <a href="https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases">Wikipedia</a> provides a list of sets of bases for which the accuracy of this test is verified.

Here is the process: 
```
FUNCTION rabin_miller():
	We name the integer we are trying to test n.
	We express n as (2^s)*d, where d is odd. Both d and s are positive integers
	For many a values: #These are the bases of the test, chosen as below
		possibilityOfCompositeOnThisRound = True
		For all r values from 0 to s-1 inclusive:
			testValue <-- a^(d*(2^r)) mod n
			IF r == 0 AND testValue == 1: #We have found a witness for the primality of n
				possibilityOfCompositeOmThisRound <-- False #We cannot be certain with this a value that n is composite
				break #So we need to try another a value
			ELSE IF r != 0 AND testValue == -1: #This is the equivalent of the first test but just for when r is greater than 0
				possibilityOfCompositeOnThisRound <-- False # We cannot be certain with this a value that n is composite
				break #So we will try another a value
		IF possibilityOfCompositeOnThisRound == True: #For all r values and for the current a, the tests returned a result that was not 1 or -1. As such, we can be certain that n is composite
			RETURN "composite"
	#If we get here and we still haven't returned composite, all of the values of a that we tested are witnesses to the primality of n, so we assume it is prime:	
	RETURN "prime"
ENDFUNCTION	
				
```
When performing the test, we are validating the assertions that:
a^d &#8802; 1 (mod n)
a^(d*(2^r)) &#8802; -1 (mod n)

For all values of r from 0 to s-1 inclusive. 

If all of these assertions are found to be true, it is certain that n is composite.

Otherwise, we must try more a values until we are satisfied either way.

Like with Fermat's test, we can have a values that attest the primality of n, even though it is composite. These are called "strong liars"

<h5>Choosing a values:</h5>
a should be in the range 1 l&#8804; a &#8804; n-1

This test can be implemented either probabilistically or deterministically. 

If we are testing relatively small values of n, we must simply try with a as the first few prime numbers. The number of primes required depends on the size of the number being tested.  (detailled at the above Wikipedia link)

Once enough of these primes have been tested as a values, it is guaranteed that n is prime.

If we are testing a much larger number, the test becomes probabilistic. We would usually choose a using the same method as the Fermat Test, that is to say randomly.

However, Monier and Rabin proved in 1980 (source: Wolfram Math World) that no composite number will pass more than 1/4 of the possible a values. This means there are no numbers that are composite but pass this test in its entirety like the Carmichael numbers for Fermat's test.

This means that we could simply try and try and try until we reach 1/4 of the possible a values, then we will have a definite result for any n, although of course the efficiency of this algorithm is not fantastic.

Another option is to calculate the probabilities. We know that for two independent events, we multiply the probabilities together to find the probability of them both happening. Hence, for every base a that gives the result that a is prime, the probability that the number is composite is multiplied by 1/4:

1 test passed: chance = 1/4
2 tests passed: chance = 1/16
3 tests passed: chance = 1/64 and so on.

I believe that this ^ works because the chance of the number being composite and the tests being passed is 1/4. Once the tests have been passed, then that just leaves the probability of being composite.

Remember that it is impossible for a prime number to come out as composite using these tests - there is as such only one type of error.


<h3>Task</h3>
Implement both of the primality tests above and compare them.


<h3>Tests</h3>
You should be able to give these algorithms any number you know to be prime or composite, and receive the correct result returned from the functions. If you want to do bulk testing of your algorithm up to 100,000, use the information in the first extension task.
E.g.
fermat_primality(80) => False
miller_rabin(97) => False

You can actually use your calculator to easily check the result of these tests if you have a Casio fx-83GT Plus or fx-85GT Plus (or better) calculator. These calculators have a FACT function above the key with the degrees, minutes (apostrophe), seconds (double quote) symbols on it. Use SHIFT to access this function. You simply need to input a number and press equals, then press SHIFT then FACT, and you will get a prime factorisation of the number entered. If the prime factorisation is the number itself, it must be indivisible and hence prime.
I explain this in such detail because although it is such a useful and simple function, many people are unaware of the capacity of their calculators to perform this operation.


<h3>Extensions</h3>
<ul>
<li>Iterate through all integers from 1 to 100,000 (or similar), and run them through each of the primality tests. Take a total time for each of the tests, and a number of correctly identified examples, which you can then convert to an accuracy percentage. You can use these pre-calculated primes (found with the infallible Eratosthenes' Sieve Algorithm) to check the accuracy of each of the tests. https://www.mathsisfun.com/numbers/prime-number-lists.html However, be warned of the speed listed on the page - this may mean that timing each of the algorithms and comparing them is challenging as the numbers involved could be quite small.
<li>Implement repeated division (shouldn't take that long) with a list of given primes to start with for division (make sure to use the square root rule to improve efficiency) and see how that fares in comparison to the other tests. You will need the primes up to root 100,000 which is between 316 and 317. One of the advantages of this method is that instead of dividing, we can multply each prime to create multiple lists, ruling out numbers in a given range that feature on these multiple lists/times tables. As a result, we can bulk test a large set of numbers instead of testing each one individually. If you have time, try both the Sieve (multiplication) and simple repeated division methods, and compare both to the other two algorithms for efficiency and accuracy. These algorithms should be 100% accurate, but they may be slower than the other ones. The sieve method should be faster than the division version. Check Wikipedia (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) for a refresher and nice graphic of the sieve version.
<li>Because repeated division requires division by all primes up to the square root of a number to confirm primality, we can grow our list of primes from just a single value very quickly up to having a list of all primes below a given value. We can use the square root fact to optimise the algorithm by only starting dividing by a certain prime once the number we are testing exceeds that prime's square. For example, we can actually start with just the prime number 2 and each time find more primes by division. We check 3 and 4, finding that 3 is prime. [although the optimisation previously mentioned allows us to know instantly that 3 is prime once we know that 1 is composite]. Then we can check 5,6,7,8, [still only using 2 to test] finding 5 and 7. We can now check all the way up to 49 before needing to use 7 etc. This offers a nice chance to implement either iteratively (bottom up) or recursively (top down) repeated division. For recursion, we can give a certain number to test, and work out the square root of this number. We call the same function to test all values up to this square root, then we do the same until we reach the exit condition/base case which is that the number supplied is 1 or 2, which we take as axiomatic to be non-prime and prime respectively. Then you build back up from this point by division, as illustrated with the previous examples. We could do this iteratively as well by simply looping while the integer being tested is not greater than or equal to the target. On each iteration, test the next natural number in sequence, dividing by all of the numbers in your primes list in sequence to check if the current value is prime. If so, add it to the primes list. Otherwise, don't. Either way increment the current value you are checking. This method has the happy consequence of generating a list of all primes up to the target value, which as mentioned can make it efficient for bulk testing. This the Sieve of Eratosthenes, but we don't often realise this, as we often start with a list of primes that we take as known (as in the list above), although it is important to realise that starting from one prime we can build a complete list of primes upto a given integer. This is why I particularly like the Wikipedia graphic I have linked, because it seems to correctly illustrate this, as well as listing the sqroot optimisation technique which I hadn't noticed before today!.</li>
<li>Primality tests have hundreds of real-world uses. Think about them and make a list. Consider one of them and, if you have time, try implementing it using your own tests.</li>
<li>I was going to do three primality tests today, but I think two will suffice for the majority of people as the time required to digest, write and test them will be significant. If you want to do another, you could try the AKS (very complicated but pretty much the most efficient deterministic test known today, as it runs in polynomial time.), Lucas-Lehmer (slightly less but not as useful as it only works for Mersenne numbers), Ward's test (requires a bit of terminological understanding but simple to implement), Solovay-Straasen (simple but generally pretty similar to the other two that we have covered), the dual-test referred to here https://stackoverflow.com/questions/7594307/simple-deterministic-small-primality-testing-for-numbers with reference to the PrimeQ Function.</li>
</ul>




<h3>Hints</h3>
I would probably do the first extension like this:
```
primesFile = FILE_OPEN("primes.txt","read")
primes = []
WHILE NOT END_OF_FILE(primesFile):#Depending on how your language handles reaching the end of the file and how carefully you program it, you could do this inside the second loop to save on looping, since we are only following a single prime at a time anyway
	ARRAY_APPEND(primes,STR_TO_INT(FILE_READ(primesFile))
ENDWHILE
currentPrimeIndex = 0
times = []
correctAnswers = []
algorithms = [*algorithm1,*algorithm2,*algorithm3]
FOR i<-1 TO 100,000:
	FOR j<-0 TO 2:
		a = GET_TIME()
		answer = algorithms[j](i)
		b = GET_TIME()
		times[j] += b-a
		IF (i==currentPrime)#i is prime
			IF (answer == TRUE): #Yay we got it right
				correctAnswers[j]++
			ENDIF
			currentPrimeIndex++;#On the next loop we will need to compare to the next prime
		ELSE #i is not prime
			IF (answer == FALSE) #Yay we got it right
				correctAnswers[j]++
			ENDIF
		ENDIF
	END_FOR
END_FOR
FOR j<-0 TO 2:
	OUTPUT("Algorithm " + j+1 + " accuracy: " +correctAnswers[j]/100000 + ", time taken to get through all 100,000 values: " + times[j])
END_FOR
OUTPUT

```

Public Key Cryptography and RSA encryption among many others.




  
Sources:
	Thanks to Wikipedia (https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test,https://en.wikipedia.org/wiki/Fermat_primality_test), Wolfram MathWorld (https://mathworld.wolfram.com/PrimalityTest.html), StackOverflow (https://stackoverflow.com/questions/7594307/simple-deterministic-primality-testing-for-small-numbers) for their sites informing this article. Also thanks to the UKMT and CJ Bradley's Introduction to Number Theory. 

