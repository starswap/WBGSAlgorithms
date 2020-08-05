TL;DR - MD5 is a hashing function. Hashing functions are one-way functions which convert an arbitrary length input into a fixed length output. They see use in verifying the integrity of data for downloads, court documents in digital forensics and digital signatures, as well as for the secure storage of passwords. MD5 was invented in 1991 and works by splitting the binary input into blocks of 512 bits. These blocks are operated on by various functions which change the values of registers A,B,C and D (each 32 bit) based on these blocks. At the end of the function, the hash value is the concatenation of A,B,C and D. You can calculate MD5 hashes of strings (for password hashing) using CyberChef for example or files (data integrity) using md5sum for example. MD5 is no longer cryptographically secure, because the hashes can be reversed so storing passwords like this is no better than storing them in plain text. Equally hash collisions can be created and manipulated so it is useless for data integrity purposes in the case of a MitM attack. Hence we should no longer be using it. Despite this, around 1/4 of web services created by CMS (like Wordpress) still use MD5 for password hashing which is very bad.  
<h1>Day 14</h1>
<h2>MD5, Message Digest 5</h2>
Previously on WBGS Algorithms we have looked at network algorithms, sorting algorithms, searching algorithms and yesterday an encoding system. Today we are going to look at a Hashing Function, in an aritcle which may become the first in a series on hashing.

As mentioned yesterday, a Hashing Function is a one-way cryptographic function which is easy to compute in one direction, but nearly impossible to reverse. It takes a variable length input and converts it to a fixed length output. For example a text file I have on my system has this hash value 5d02f7b29819ba5f42d91af6dd764ce5, and a much longer executable file has this hash value: cd5bcbbce49e0bf12344ed10091e807b. 

Unlike encryption, hashing does not use a key, and unlike encoding, the data should be irrecoverable once hashed.

A hashing algorithm must have integrity - this means that the same input data (whether that be a file or a text string) must always produce the same output hash. We can think of hashing as producing the digital "fingerprint" of a file or of a string of data/ 

The final requirement for a hashing function to be useful is that hash "collisions" cannot be found and manipulated.

What do we mean by a hash collsion? A hash collision is when two different values produce the same hash. Since there are infinitely many possible inputs and a finite number of outputs to a hash function, collisions are inevitable. However, we seek to choose such a long output string that there are so many possible combinations that the chance of a collision becomes very low. If a collision does occur, it will thus have to be between files that are extremely different to each other. This means that if someone tried to fool you by swapping the files over, you would know what they had done without having to rely on the hash function.

A hashing algorithm must by extension prevent manipulation of data to produce deliberate hash collisions. If someone could produce a malware file with the same hash as a normal program, someone might think that they had the real program when they actually had the malware file. They would run it, infecting their system. Real in-use hashing algorithms rely on the fact that if someone could find a collision between two hashes, it wouldn't be between two valid executables, for example, and even then they wouldn't be able to control what the colliding file did, since they wouldn't be able to construct hash collisions - only find them. Sadly for MD5 this is not the case: see <a href="https://crypto.stackexchange.com/questions/1434/are-there-two-known-strings-which-have-the-same-md5-hash-value">here</a>

Hashing Functions have three main uses:
<ul>
<li>Password storage - Because hashing cannot be reversed easily, online services should store password hashes in a database, rather than the passwords themselves. If someone obtains these hash values by hacking into the website's database it will be useless, because they won't have the original passwords, so they will have no way to steal any accounts. When you create an account with a service, they will hash your password and store that in the database, then every time you log in, your attempted password will be hashed and compared with the hash stored in the database. Since a good hash function has practically no collisions, only the right password will make the hashes match, so only authorised persons will be allowed to log in.</li>
<li>Download integrity - When you download a file, you have no idea whether the file you receive is the file that was sent to you from the server at the other end. The file may have been damaged in transit, or edited by a malicious actor in the middle of your conversation. Since the same data always produces the same hash and collisions should be unlikely, we can use hashing to verify that we have received the same file that was sent to us from the server. The server owner should hash the file and send you the hash, preferably via a different means to the way the file will be transferred (to avoid a malicious actor simply changing the hash). After downloading the file, you hash it yourself, and if the hashes match, the file is intact. Otherwise, you need to download it again.</li>
<li>Computer Forensics - In Law Enforcement it is imperative that forensic examiners do not modify data collected from systems. In the same way that a knife, say, found at a crime scene would be sealed in a bag so it couldn't have other fingerprints put on it, we need to ensure the integrity of digital evidence. The problem is that investigators need to look at the "knife" during their investigation, so it can't stay in a bag. To prove that they haven't "touched" it / tampered with the digital evidence, the person collecting the evidence will hash it, and write this hash down in a notebook. They will give the examiner the evidence, and once the investigation concludes, the hash of the investigator's file will be checked to make sure no changes have been made.</li>
</ul>

As mentioned above, the MD5 Algorithm, designed by Ronald Rivest in 1991, is no longer cryptographically secure. This is because hash collisions can be maliciously crafted for any two files, such that a genuine file could be swapped with a replacement and if someone used MD5 to check that the file was the same, they would think that it hadn't been changed. This means that MD5 is no longer useful in digital forensics or download verification to fight against deliberate manipulation, although it can be used to check for file corruption and as a unique identifier for files. In terms of password hashing, MD5 hashes can be broken in seconds with rainbow table attacks (since the majority of implementations don't support salting by default), brute forcing or dictionary attacks, or by trying to reverse engineer the function (https://en.wikipedia.org/wiki/MD5#Preimage_vulnerability). For this reason MD5 is no longer a secure way to store passwords.

However, despite its present flaws, MD5 was the standard algorithm for about 15 years, used in digital certificate and signature applications, and is the oldest hashing algorithm that we still find in use (1/4 of websites built through CMS - graphically designed without writing any code - use this algorithm according to Wikipedia). For this reason and because it is just about manageable to understand and to program, it is interesting to investigate. Contemporarily used hashing algorithms get increasingly complex very quickly, so if we are to look at those in the future, we want a solid base of understanding.

<h3>Algorithm</h3>
Please note that while hashing as a concept is relatively simple, producing an algorithm that does the job is challenging. There are many, many steps in the MD5 algorithm. Understanding why they work to shorten the message in a way that is challenging to reverse is extremely difficult. The best suggestion I can offer is that there are so many operations that reversing the whole process would be extremely confusing.

In order to implement the algorithm, we don't need to understand why it works, only how. You will also note that there are many obvious and not so obvious choices of arbitrary values, for example for initialisation, set up in the standard. Clearly these could have been any values, but the ones below are the ones chosen for the standard. (For example 01 23 45 67)

Also note that in the below I make statements such as "to avoid collisions" - this was the case at the time, and the rationale behind these decisions remains, although clearly we now know that they were unsuccesful.

Throughout this explanation we will have a concurrent example, which should help to make clear what is going on at each step. We are going to hash the message WBGS, which is 01010111 01000010 01000111 01010011.

<h4>Padding</h4>
The MD5 Algorithm produces a 128 bit hash from a message of an arbitrary length. This means the message can be made up of any number of bits, including a zero length message.

In order for this to work, we need to add some padding to the message, so that the actual MD5 function receives as input a message of a consistent format. This consistent format is a message with a length that is a multiple of 512 (2^9) bits. Henceforth we will refer to the message as being in binary. If you want to hash a text message, you need to convert it to binary first using a character encoding such as ASCII.

To do this while avoiding collisions, we do this in two separate steps:
<table>
<tr><th>Step</th><th>Example</th></tr>
<tr><td>1. Take the binary message and append a one, then enough zeros to make its length 64 bits fewer than a multiple of 512</td><td>01010111 01000010 01000111 01010011 10000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000  </td></tr>
<tr><td>2. Append the length of the original message expressed in binary. If the length is greater than 2^64 -1, it won't fit in the remaining bits (as we want a message that can be chunked into 512 bit blocks, so there are only 64 spaces left). This means that you have to take only the last 64 bits of the length, which is equivalent to taking the length of the message MOD 2^64 (since any more significant bits only add multiples of 2^64 to the length value.) To do this the length is converted to binary, then extended to make sure that it is of length 64. Then, we append the last 32 bits of the length first, then the first 32 bits. </td><td>The length of the original message was 32 bits, or 10000. We pad this with 59 zeros, appending the first 32 bits (all zero) to the message first, then appending the second 32 bits. 01010111 01000010 01000111 01010011 10000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 | 00000000 00000000 00000000 00000000 | 00010000 00000000 00000000 00000000</td></tr>
</table>

Please note that this padding always occurs, even if the binary value already has length that is 64 less than a multiple of 512. In this case, 512 bits are added. The least number of bits that can be added is 1 single 1 and 64 for the length, while the most that can be added is 512 + 64 for length.


<h4>Buffers</h4>
When creating a hash value with the MD5 function, we iterate over the 512 bit blocks of the message, performing a series of operations  on four 32 bit "buffer" variables (also called registers) using this data. These buffers are named A,B,C and D.

The final hash value output is a concatenation of A, B, C and D.

We start by initialising:
```
A to 01 23 45 67 
B to 89 AB CD EF
C to FE CD BA 98
D to 76 54 32 10 in hex.
```
But just to make things even more confusing, these hex values are expressed as the least significant byte first (this is called little endian). What this means is that to get a normal binary number, where on the left we have 2^x and on the right we have 2^0 and for each placeholder moving right we decrease the exponent by one, from these, we can't simply do a normal conversion.

At GCSE we learnt to convert from Hex to binary by splitting into nibbles. Doing that here would give 0000-0001 0010-0011 0100-0101 0110-0111 for A, for example. However because the least significant bytes are first, we have to flip the byte order to get  0110-0111 0100-0101 0010-0011 0000-0001. Note that the bit order within a byte stays the same. Now we have a normal binary number that we are used to, which could be simply converted to decimal by doing 1*2,0*2,0*4,0*8,0*16,0*32,0*64,0*128,1*256,1*512,0*1024 and so on, moving from right to left.

This means that as a normal (or big endian) binary value:

A = 0110-0111 0100-0101 0010-0011 0000-0001 = 01100111010001010010001100000001
B = 1110-1111 1100-1101 1010-1011 1000-1001 = 11101111110011011010101110001001
C = 1001-1000 1011-1010 1101-1100 1111-1110 = 10011000101110101101110011111110
D = 0001-0000 0011-0010 0101-0100 0111-0110 = 00010000001100100101010001110110

<h4>Logic Gate Functions Refresh</h4>
Before we can get to grips with the final algorithm, there are a few more aspects of the algorithm to define.

MD5 uses four main functions F,G,H and I, which are applied to the data. These are themselves made up of the bit-wise logic gate functions NOT, OR, AND and XOR. We learnt about the first three at GCSE (If you didn't see <a href="https://vimeo.com/106364318">this</a> it is well worth a watch.), and it isn't a strech to realise that eXclusive OR is only true when one or another input is true but not neither or both.

Here I reproduce the truth tables of the logic gate main functions as a reminder:

<table>
<tr>OR (Usually |)</tr>
<tr><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>1</td></tr>
</table>

<table>
<tr>AND (Usually &)</tr>
<tr><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td></tr>
</table>

<table>
<tr>NOT (Usually ~)</tr>
<tr><td>0</td><td>1</td></tr>
<tr><td>1</td><td>0</td></tr>
</table>

<table>
<tr>XOR (Usually ^)</tr>
<tr><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>0</td></tr>
</table>

These functions are all applied bitwise in the algorithm, which means that the inputs are compared bit by bit, not as a whole. 

We will also need to understand circular bitshifting to make MD5 work. This very simply takes an input register and shifts the bits left a number of times. Instead of simply discarding MSBs that have been pushed off of the top end of the register and putting zeros in at the LSB end, we move these bits to the beginning as follows:
```
10011100 shifted by 1 gives 00111001 
10011100 shifted by 2 gives 01110010
10011100 shifted by 3 gives 11100100
10011100 shifted by 4 gives 11001001
10011100 shifted by 5 gives 10010011
10011100 shifted by 6 gives 00100111
10011100 shifted by 7 gives 01001110
10011100 shifted by 8 gives 10011100
```
As you can see for an n bit binary string, there are n possible different shifts that can be applied to it, with the nth shift returning the string back to normal. Thus the 32 bit variables that we will use for MD5 can be shifted 31 time before on the 32nd shift they return to their original value

<h4>Functions used in MD5</h4>
The MD5 algorithm applies these logical functions in combination in 4 different compound functions used extensively in the algorithm. You will see that they all follow a similar template. These are defined by the standard as:
```
F(A,B,C) = (A and B) or (not(A) and C)
G(A,B,C) = (A and C) or (B and not(C))
H(A,B,C) = A xor B xor C
I(A,B,C) = C xor (B or not(D))
```
For each of the 512 bit blocks of the padded input that we operate on, we will see below that there are 4 "rounds", each of which uses a different one of the 4 functions 16 times with different inputs, using them to edit the values stored in our four registry variables.

<h4>Table of values</h4>
The MD5 function also adds a bit more complexity by using a table of precomputed values, one value of which is added into every calculation made. 

These values are generated as "the integer part of or floor() 4294967296 times abs(sin(i)), where i is in radians", and there are 64 of them from i = 1 to 64. Don't worry about the generation of these values as in any realistic implementation we would just read these values in from a file.

Note that 4294967296 is 2^32.

Here are all 64 values, expressed in Hexadecimal and reproduced from Wikipedia:

[0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf,
 0x4787c62a, 0xa8304613, 0xfd469501, 0x698098d8, 0x8b44f7af,
 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e,
 0x49b40821, 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8, 0x21e1cde6,
 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8,
 0x676f02d9, 0x8d2a4c8a, 0xfffa3942, 0x8771f681, 0x6d9d6122,
 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
 0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 0xd9d4d039,
 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 0xf4292244, 0x432aff97,
 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d,
 0x85845dd1,  0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]


<h4>Final Algorithm</h4>

Now we have learnt about all of the components of the MD5 algorithm, we have only to put it together into a step by step process:
```
Define Functions FGHI and circular_left_shift, circular_right_shift                          #As above
Define Table of values Sine_Table with the values above
Pad the message with a 1
Pad the message with 0s                                                                      #All padding described above
Pad the message with the message length
Initialise the registers/variables A,B,C and D as we described above.
FOR every 512 bit block in the padded message:
	Save the block as the variable current512, containing 16 * 32 bit chunks of the current 512 bit block
	Save the values of A, B, C, and D to A_old,B_old,C_old,D_old
	Conduct round 1 of the hashing with the function F:
		current_shift_value <- 7
		inputs <- [*A,*B,*C,*D] #Note that you need to point to these values so that the values in the registers actually change. It is no good just changing a copy in an array unless you set the registers equal to the copies again at the end		
		FOR operation_number FROM 1 TO 16:
			F <- function_F(*inputs[1],*inputs[2],*inputs[3]) 
			inputs[0] <- inputs[1] + circular_left_shift(inputs[0] + F + current512[operation_number-1] + Sine_Table[operation_number],current_shift_value)
			circular_right_shift(inputs,1)
			current_shift_value <- current_shift_value + 5
			IF (current_shift_value = 27): #We got to the highest shift we can do so reset to 7 - since 32 would be no change as these are 32 bit registers
				current_shift_value <- 7			
			ENDIF
	Conduct round 2 of the hashing with the function G:
		current_shift_value <- 5
		inputs <- [*A,*B,*C,*D] #Note that you need to point to these values so that the values in the registers actually change. It is no good just changing a copy in an array unless you set the registers equal to the copies again at the end		
		block_to_use <- -4		
		FOR operation_number FROM 1 TO 16:
			block_to_use <- (block_to_use + 5) MOD 16
			G <- function_G(*inputs[1],*inputs[2],*inputs[3]) 
			inputs[0] <- inputs[1] + circular_left_shift( (inputs[0] + G + current512[block_to_use] + Sine_Table[operation_number-1+16]) ,current_shift_value)
			circular_right_shift(inputs,1)
			current_shift_value <- current_shift_value + 4
			IF (current_shift_value = 24): #We got to the highest shift we can do so reset to 5
				current_shift_value <- 5			
			ENDIF

	Conduct round 3 of the hashing with the function H
		inputs <- [*A,*B,*C,*D] #Note that you need to point to these values so that the values in the registers actually change. It is no good just changing a copy in an array unless you set the registers equal to the copies again at the end		
		block_to_use <- 2
		shifts <- [4,11,16,23]		
		FOR operation_number FROM 1 TO 16:
			current_shift_value <- shifts[(operation_number MOD 4)]
			block_to_use <- (block_to_use + 3) MOD 16
			H <- function_H(*inputs[1],*inputs[2],*inputs[3]) 
			inputs[0] <- inputs[1] + circular_left_shift( (inputs[0] + H + current512[block_to_use] + Sine_Table[operation_number-1+32]) ,current_shift_value)
			circular_right_shift(inputs,1)

	Conduct round 4 of the hashing with the function I
		current_shift_value <- 5
		inputs <- [*A,*B,*C,*D] #Note that you need to point to these values so that the values in the registers actually change. It is no good just changing a copy in an array unless you set the registers equal to the copies again at the end		
		block_to_use <- 2
		shifts <- [6,10,15,21]		
		FOR operation_number FROM 1 TO 16:
			current_shift_value <- shifts[(operation_number-1) MOD 4]
			block_to_use <- (block_to_use + 7) MOD 16
			I <- function_I(*inputs[1],*inputs[2],*inputs[3]) 
			inputs[0] <- inputs[1] + circular_left_shift( (inputs[0] + I + current512[block_to_use] + Sine_Table[operation_number-1+48]) ,current_shift_value)
			circular_right_shift(inputs,1)
	
	A <- A + A_old
	B <- B + B_old
	C <- C + C_old
	D <- D + D_old
Once we get to here we have looped over all of the blocks.
The final hash is a concatenation of A,B,C and D BUT in little-endian encoding, which means that the first byte is the lowest value byte of A, and the last byte is the highest value byte of D, but the bits are still ordered normally within the bytes (as mentioned above). You may need to write a function to do this conversion and reordering. 
```

For a complete pseudocode example, see the page 4 of the <a href="https://tools.ietf.org/html/rfc1321">booklet</a> defining the standard. It is well worth a look, as it is quite clearly understandable (after a while of looking). Note that the order of the operations in each round is left to right then up to down.
Equally the <a href="https://en.wikipedia.org/wiki/MD5#Pseudocode">Wikipedia</a> example provides a nice understanding of how the seemingly arbitrary conventions of which 16 operations should be done on each round are generated, and the relationship between each of the 16 operations.

<h3>Task</h3>
<ol>
<li>Clearly this is not a simple algorithm to understand, so the first step is to simply go through it slowly, refering to this page and the resources linked until you undertand it.</li>
<li>Then, you will want to make sure that you have a function that can perform each of the basic logic gate functions on the registers. This should exist by default in your programming language, but if not you may have no choice but to implement it yourself, setting the registers as strings of bits.</li>
<li>You will now want to implement the circular_shift functions. There is a neat mathematical trick that can be used to shift the values if your programming language doesn't offer this function as a builtin. Because the first column in a 32 bit binary register represents 2^32 and the last one represensts 1, you can take the decimal representation of the number and:
<ul>
<li>if you are shifting towards the left, repeatedly check the size of the decimal number. If it is greater than or equal to 2^32 there must be a one in the leftmost postion. To do the shift, subtract 2^32 (as this is equivalent to removing the top bit), double the result(as this is equivalent to shifting all other bits left) and add 1(as this is equivalent to putting the bit on at the bottom.). If it is not greater than 2^32, there is a zero in the leftmost bit position, meaning all you need to do is double the number. Do this process repeatedly for multiple </li>
<li>if you are shifting towards the right, repeatedly check the parity of the decimal number. If it is odd, then you know that the lowest bit is a one. Subtract 1, halve the result and then add 2^32. If it is even, halve the decimal representation only. Do this repeatedly for shifts larger than 1 place.</li>
</ul>
</li>
<li>Now, use the functions you have just made and the builtin logic gate functions to make the functions FGH and I used in the MD5 Algorithm</li>
<li>Finally put all of this together with the table of values to make the main loop of the function, and hash some data</li>
</ol>

<h3>Tests</h3>

You can again use <a href="https://gchq.github.io/CyberChef/#recipe=MD5()">Cyber Chef</a> to test your function, but I will reproduce some possible tests here:
MD5 hash of a blank string: d41d8cd98f00b204e9800998ecf8427e (this happens because of padding)
MD5 hash of MD5!: 872405d602f3d57eba6d7ab3f640aa0d
MD5 hash of Lots of fun: ab1e923e3b36c8c8740a5329db072c37
MD5 hash of lots of fun: 980cf525a8b3945aa0fd81b49ee5a1e9 (one of the important characteristics of hashing is that similar inputs give diverse outputs - this prevents guessing of a password one character at a time for example)

<h3>Extensions</h3>
Since today's algorithm is quite challenging, there aren't too many extensions
<ul>
<li>You should start by making the MD5 function work on text input, then for hashing files. I believe this works simply by reading in from the file as a string of binary data, which you can do in some languages with a separate function, and in others with the b read mode. You can check the answers given by the file summing using md5sum for linux or a website.</li>
<li>Find out about the uses of MD5 in Certification of websites and digital signatures. It was used for a few years in the field, but recently found to be too insecure. Find out when and how it was broken as well as how it used to be used.</li>
<li>Find out about the Hash Table data structure - this is what powers Python dictionaries. The hash function used is not exactly the same as MD5, but it is of a similar type.</li>
<li>Build a (not very) secure log-in form using MD5 to hash the passwords. Write the passwords into a database or a file on disk to store them. Then use CrackStation or HashKiller to break the MD5 hashes and you will realise how easily breakable they are, and why we should no longer use them in web development.</li>
<li>Find out about salting and peppering in hash functions and implement them for your MD5 implementation even though most versions of MD5 don't use this, to improve the security offered. We will look at this in more detail if we look at other hashing functions later</li>
</ul>
<h3>Hints & Solutions</h3>
https://en.wikipedia.org/wiki/Hash_table
https://www.tutorialspoint.com/data_structures_algorithms/hash_data_structure.htm
Both salt and pepper are values added to a password before it is hashed in password hashing. This makes hashing more secure because it prevents the use of rainbow table attacks which are precomputed tables mapping hashes to their plaintext counterparts, which should be the same wherever the hashing is used. This means leaked password hashes can be looked up in rainbow tables and then the plaintext passwords are revealed. By adding a random value (salt) or a fixed value unique to the servie in question (pepper) to the password before hashing, such as by simple concatenation or through another input to the hash function, the developer ensures that an attacker cannot use precomputed tables of hash values to crack hashes stored by a site, as he won't know the salt/pepper values before to do this computation with, and it would take too long to compute for every possible secret value. In salting, the salt is stored next to the password in a database, and is a random value unique to each hash. In peppering, the same value is added to each password before hashing in every hash generated by a given website, but this secret is not stored with the passwords. Whenever a user wants to log in, the salt and pepper are added to his inputted password before the hashing takes place, such that if the password matches the correct one, the hashes will match as the same salt and pepper were used in the original sign up. Therefore, password hashing with salt and pepper works in the same way as normal hashing.   
<h3>Sources</h3>
To find out about how MD5 works from the author itself, check out the <a href="https://tools.ietf.org/html/rfc1321">page</a> that defines the standard. <a href="https://en.wikipedia.org/wiki/MD5">Wikipedia</a> is, I believe, less easily understandable for this algorithm than the original source, although its descriptions of the four functions FGH and I are clearer and so used here.

https://www.digital-detective.net/understanding-big-and-little-endian-byte-order/
