<h1>Day 13</h1>
<h2>Base64 Encoding</h2>
Today we are taking a break from sorting and searching to look at one of the most widely used encoding schemes on the web, Base64. But first what is an encoding scheme, and how do these differ from encryption and hashing algorithms? Well, all of them convert a message into a different format such that by simply looking at it, it can no longer be read. 

However, in an encoding scheme, the recipient needs only to know which scheme was used to encode the data in order to decode and to read it. This is very easy to determine even if you are not told it. This is why encoding is not cryptographically secure. Encoding is mostly used to limit the character set used in certain cases, when full Unicode cannot be sent over a certain connection. This is indeed the case with Base64.

Next, we have encryption. Encrypting data requires a key and an encryption function or cipher. To decrypt the data, and read the original text, you need to know the encryption function so that you can use the corresponding decryption function. You also need the key. The idea with good encryption is that it is so secure that we can broadcast publicly the encryption algorithm in use (for example everybody knows that we are dealing with public key encryption when using HTTPS), but because an eavesdropper doesn't have the key, the message is completely useless to them.

Finally, a hashing algorithm is a one-way function, which acts more like an encoder as it has no key. It converts an arbitrary length string (which could be an entire file) into a fixed length block of seemingly random characters from a character set. These functions cannot be easily reversed, which means given a hash you cannot find out what the original data was. This makes them useful for password storage. Because they always produce the same result for the same input data, and they reduce the length of the data, they are also useful for verifying the integrity of files. You must only check that the hashes match to know that the files match, not the whole files.

In a sense, a hashing algorithm is the most secure out of these three, but it is so secure that it isn't useful for the transmission of messages, because even the intended recipient wouldn't be able to recover the original message. Encryption would be used for the secure transmission of messages, as encoding would not be secure <strong>enough</strong>

<h3>Algorithm</h3>

Base64 is used to transmit data in situations where data is transmitted character by character, rather than bit by bit, for example email systems. It is necessary because a lot of these systems only allow basic ASCII characters to be transmitted, while we want to be able to send unicode characters such as smiley faces, or even binary strings that do not equate to characters at all, such as when files are attatched in our emails. We also want to obfuscate some punctuation characters which could break the systems we are using, such as &,% or *.

To solve this problem, we need to use the Base64 encoding scheme, which increases the number of characters in the message, but reduces the range of the character set in use. 

The way this works is by taking the input text and converting it to a binary stream, using Unicode, ASCII or whatever system you like. ASCII will typically use 8 bits per character; Unicode will use 8, 16, 32 or more depending on whether you are using UTF-8 or UTF-16 for example. 

We then split the binary stream into blocks of only 6 bits. This is because 6 bits offers 2^6 = 64 combinations, so to represent these in a system that transmits by character, we only need 64 characters. For each block of 6 characters, we convert them to a character in the range a-z,A-Z,0-9+/, using <a href="https://en.wikipedia.org/wiki/Base64#Base64_table">this table.</a>

Here is an example, using ASCII to convert input characters to binary:

<table>
<tr><td>B</td><td>a</td><td>s</td><td>e</td><td>6</td><td>4</td></tr>
<tr><td>0100 0010</td><td>0110 0001</td><td>0111 0011</td><td>0110 0101</td><td>0011 0110</td><td>0011 0100</td></tr>
</table>

Our bit string is now 010000100110000101110011011001010011011000110100

Split this into blocks of 6:

010000 100110 000101 110011 011001 010011 011000 110100

Using the Base64 table, we convert this to:

QmFzZTY0

You can see that we have converted 6 characters into 8, but the range of characters is now much less, as we have gone from 256 possible characters as we had 8 bits per character to 64 as we have 6. We could apply this to any original encoding, such as a 16 bit per character Unicode one. Doing that would reduce the character range from 65536 to just 64. We can transmit all of these 64 characters by email, for example whereas basic email wouldn't support the transmission of all of the different characters represented by the 16 bit encoding.

That seems simple enough, however there is one more thing to consider, which is the padding characters. Imagine that we added one more character to our string above, say a 3, which equals 0011 0011 in ASCII. We now have 7*8 = 56 bits to encode, but that doesn't divide by 6, which is imperative for the conversion back to characters for transmission. To fix this we add 4 zeros to fill up to the end of the next 6 bit block. 

We now have:

Base643 = 01000010011000010111001101100101001101100011010000110011[0000] = 010000 100110 000101 110011 011001 010011 011000 110100 001100 11[0000]

									     Q      m      F      z      Z      T      Y      0      M       w
When decoding this, we don't know which of these characters are padding zeros and which are not. If we know that we are looking for an original message which was chunked into blocks of 8 bits, we could go 8 bits at a time decoding the message until we got to 001100110000. We would take out the first 8 bits to get 00110011 and we would decode that to 3, which is right. We would then assume that the remaining 4 characters were padding as they don't make up a full byte. However, what if we wanted to encode something that started in binary and it was allowed to have single nibbles, or what if we were worried that 4 extra bits were lost in transit, and hence we were missing a whole character from the original message.

The way we solve this is with padding equals signs. We add equals signs at the end of the encoded message, one per 2 padding zeros that have been used. This sort of acts like a checksum to make sure that the message is intact. These equals signs do not decode to anything, they simply tell us how many of the bits we can discard before decoding. 

Because we are converting between 6 and 8 bit characters, we know that every 24 bits will fit exactly into 4 6 bit characters and 3 8 bit characters. This means that every message will be some integer * 24 bits in length, plus some extra bits. Either we start with a multiple of 24 plus 1 8 bit character or a multiple of 24 plus 2 8 bit characters, or a multiple of 24 plus 3 8 bit characters (which is just another 24). If we have 1 8 bit character extra we must add 4 bits of padding to make up to 12 (2 6 bit characters), but with 2 we must add 2 bits of padding to make 18 (3 6 bit characters) which requires 2 zeros of padding. If we have an exact multiple of 24 bits, we don't need any padding zeros. This means we only ever need zero, one or two equals signs at the end of a Base64 message to specify the amount of padding in use.

For example:

B --> 01000010 -> 010000 10 -> 010000 10[0000] -> Qg== (the two equals characters mean we have added four zeros of padding in order to make up the last character. This means that on decoding we go Qg== -> Qg including 2*2 padding bits -> 010000 100000 -> Discard the last 4 bits as we know they are padding -> 010000 10 -> Regroup into blocks of 8 01000010 -> B) 
B6 -> 01000010 00110110 -> 0100001000110110 -> 010000 100011 0110 -> 010000 100011 0110[00] -> QjY= (the equals character means we have added 2 bits of padding. This means that on decoding we go QjY= -> QjY including 2*1 padding bits -> 010000 100011 011000 -> Discard last two bits as we know that they are padding -> 010000 100011 0110 -> 01000010 00110110 -> B6 (ASCII) )
B64 -> 01000010 00110110 00110100 -> 010000100011011000110100 -> 010000 100011 011000 110100 -> QjY0 (there are no equals characters so decoding is simply the reverse process. QjY0 -> 010000 100011 011000 110100 -> 010000100011011000110100 -> 01000010 00110110 00110100 -> B64)

The equals characters can also be thought of as ensuring that Base64 strings are always a multiple of 4 characters in length. This means that these messages can then be decoded in blocks of 4 characters, checking each time at the end of the block for equals signs, which tell you how many characters you are looking to decode this block into. If there are no equals signs, you are looking to decode the block into 3 ASCII characters; if there are 1 equals sign 2 ASCII chars; with 2 equals signs one ASCII char. This is equivalent to understanding them as representing the number of padding zeros when we have 8 bit ASCII original encoding.

The question to ask then becomes - what if we aren't using an 8 bit ASCII character set? As long as the original characters are represented by a multiple of 8 bits, they can be converted to and from Base64 as normal, understanding the equals signs as representing the number of padding characters.

If we were to use basic 7 bit ASCII, for example, or any other character set that uses a number which is not a multiple of 8, it becomes more difficult to map this to Base64. However, since computers work with 8 bit bytes, each of these characters <strong>will</strong> still be represented in memory as an number of bytes, and so a binary string with a multiple of 8 bits as its length. This means that we can actually just use these representations when we convert to Base64 and it will work fine, as we will always start with a multiple of 8 bits. 

A quick note before we move onto pseudocode - a single character ASCII character has many different encodings depending on what characters it appears with and where it appears. This is why it makes more sense to think of Base64 as encoding bit strings rather than individual characters.

<h5>Pseudocode</h5>
Before we can produce a Base64 encoding function, we need to be able to get the binary representation of each character that is input into the program. Your programming language might already have this, especially if it is an LLL and so you can access the memory directly, but in case this isn't the case, here is a model function to convert from base10 to binary. You should be able to get the base10 character representations with a builtin subroutine such as ord() or CHAR_TO_INT() or maybe just by casting to int

Please note that because we want to operate bit by bit and take ranges, for example, the easiest way to write this function will be to store strings of bits as strings - of course this uses 8* more memory than just storing bits, but this is fine for our purposes, since we won't be converting much data, and the result achieved will be right.
```
FUNCTION to_binary(base10):
	answerString <- ""
	WHILE (base10 != 1):
		answerString <- STR_CONCAT(answerString,INT_TO_STR(base10 MOD 2))
		base10 <- base10 DIV 2
	END_WHILE
	answerString <- STR_CONCAT(answerString,"1")
	RETURN STR_REVERSE(answerString)
END_FUNCTION

FUNCTION to_decimal(base2,lengthMultiple):
	answer <- 0
	binaryString <- INT_TO_STR(base2)
	multiplier = 1
	FOR i <- 0 TO LENGTH(binaryString) -1:
		answer = multiplier * STR_TO_INT(binaryString[i])
		multiplier = multplier * 2
	END_FOR
        WHILE NOT(LENGTH(result) MOD lengthMultiple == 0):
		result <- STR_CONCAT("0",result)
        END_WHILE
	RETURN answer
END_FUNCTION

FUNCTION string_to_binary_string(inputString): #If you want to use a different starting encoding such as Unicode UTF16 for example, this is the function to change. The others should work fine.
	binaryString <- ""
	FOR i <- 0 TO LENGTH(inputString) -1:
		ASCIIBinary <- toBinary(CHAR_TO_INT(inputString[i]),8) #We need to make sure that this is of length that is a multiple of 8 for B64 to work
		binaryString <- STR_CONCAT(binaryString,ASCIIBinary)
	END_FOR
	RETURN binaryString
END_FUNCTION

FUNCTION binary_string_to_string(binaryString): #You will need to change this as well
	resultString <- ""
	i <- 0
	WHILE (i < LENGTH(binaryString)-8):
		result_string = STR_CONCAT(resultString,INT_TO_CHAR(to_decimal(binaryString[i:i+8])))
		i <- i+8
	ENDWHILE
	RETURN resultString
END_FUNCTION

FUNCTION base64_encode(binaryString): #Making these functions convert between base64 and binary strings rather than between base64 and text strings is good as it means non-text data such as images can easily be encoded
	i <- 0
	resultString <- ""
	mapping <- ["a","b","c","d"....,"A","B","C","D"....,"0","1","2","3"....,"+","/"] #You obviously need to actually fill in all of the values
	WHILE (i+6 < LENGTH(binaryString)-1):
		currentBinaryString <- binaryString[i:i+5] #Inclusive ranging! Select current block to convert. We then need to convert it back to a character. We could do this with a simple mapping dictionary/array/hashtable/object or by using the sequential properties of the table. 0-25 = A-Z, 26-51 = a-z, 52-61 = 0-9, 62,63 = +,/
		decimal <- to_decimal(currentBinaryString)
		resultString <- STR_CONCAT(resultString, mapping[decimal])
		i <- i+6
	ENDWHILE
	binaryString <- STR_CONCAT(binary_string,"000000")
	lastBlock <- binaryString[i:i+5] #Inclusive ranging again.
	resultString <- STR_CONCAT(resultString,mapping[to_decimal(lastBlock)])
	numberOfPaddingBits <- (LENGTH(binaryString)-6 - i) 
	numberOfEqualsRequired <- numberOfPaddingBits/2
	FOR i <-1 TO numberOfEqualsRequired:
		resultString <- STR_CONCAT(resultString,"=")
	ENDFOR
	RETURN resultString
END_FUNCTION

FUNCTION base64_decode(textString):
	mapping <- ["a","b","c","d"....,"A","B","C","D"....,"0","1","2","3"....,"+","/"]
	binary_string <- ""
	FOR i <- 0 TO LENGTH(textString) - 1:
		currentChar <- textString[i]
		currentCharIndex <- ARRAY_SEARCH(mapping,currentChar) #Any searching algorithm we have done or another - your language probably has one builtin.
		binary <- to_binary(currentCharIndex,6) #We need to be sure that we have converted this index to a six char length binary string for this to work. You could use a mapping hash table/dictionary instead of this but this method seems to be quicker.
		binaryString <- ARRAY_CONCAT(binaryString,binary)
	END_FOR
	i <- LENGTH(binaryString)-1
	numberOfEquals <- 0
	WHILE (binaryString[i] == '=':
		numberOfEquals++
		i--
	END_WHILE
	numberOfCharsToIgnore <- 2*numberOfEquals
	binaryString <- binaryString[0:LENGTH(binaryString)-numberOfEquals-1]
	RETURN binaryString
END_FUNCTION

```


In order to encode, we need to do this:

```
inputString <- USERINPUT()
binaryString <- string_to_binary_string(inputString)
result <- base64_encode(binaryString)
OUTPUT result
```
In order to decode, we need to do this:
```
base64String <- USERINPUT()
binaryString <- base64_decode(base64String)
finalString <- binary_string_to_string(binaryString)
OUTPUT finalString 
```

<h3>Task</h3>
<ol>
<li>Produce a function which converts from decimal to binary and vice versa, or work out a way to extract the binary representation of characters from memory. If your language supports it, you may find that you can use an appropriate format specifier.</li>
<li>Then, produce a function which can encode a plain text/binary string into Base64 and one which can decode Base64 to produce a binary string/plain text. If you are doing binary string, you will need another function to convert between plain text and binary strings, involving converting characters to their numeric ASCII codes. You might like to investigate optional arguments if you are using an HLL, which would allow you to have a two way function that encodes or decodes depending on which arguments are present. The same could be said for the binary string <----> text string function.</li> 
</ol>


<h3>Tests</h3>
For Base64 encoding, I'd like to recommend the wonderful CyberChef, produced by the GCHQ. You can select the "To Base64" or "From Base64" tiles from the favourites drawer and drag them into the "Recipe" in the centre. Type some input into the top right box and see the result in the bottom right one. Compare this to the result given by your program.

<a href="https://en.wikipedia.org/wiki/Base64">Wikipedia</a> offers some examples as well. 

In case you have downloaded this page or something, here are some examples:
<ul>
<li>Base 64 is amazingly enjoyable! ---- QmFzZSA2NCBpcyBhbWF6aW5nbHkgZW5qb3lhYmxlIQ==</li>
<li>WBGS ---- V0JHUw==</li>
<li>Isn't this fun? ----- SXNuJ3QgdGhpcyBmdW4=</li>
<li>Moi j'ai hâte pour la rentrée scolaire ----- TW9pIGonYWkgaOJ0ZSBwb3VyIGxhIHJlbnRy6WUgc2NvbGFpcmU (One use of Base64 is in encoding accents for old/xenophobic systems that don't support them</li>
</ul>

In Javascript, the builtins atob() and btoa() provide B64 encoding and decoding functionality, so you can compare your results against them.

<h3>Extensions</h3>
<ul>
<li>Estimate the time complexity of the Base64 algorithm and verify your result by running the algorithm with many different input sizes - I would suggest reading such a large amount of data in from a file.
<li>Base64 encoding is often used to encode public keys and certificates in encryption. Find out about <a href="https://www.comparitech.com/blog/information-security/rsa-encryption/">RSA</a> encryption, and try decoding a <a href="https://travistidwell.com/jsencrypt/demo/">key</a> with your function (you might not get a very nice result if trying to interpret as ASCII)them. We will likely do RSA in a future episode of WBGS Algorithms
<li>The real benefit of Base64 is being able to reduce expansive character sets to very small ones. Find out about Unicode UTF-8 and UTF-16, and implement a UTF-8 or UTF-16 --> binary stream converter, so that you can encode characters from unicode using Base64. Then, convert this unicode phrase to binary (note the values are in hex), and then encode it as Base64: \u2602\u0020\u0054\u004F\u004D\u004F\u0052\u0052\u004F\u0057
<li>Try using a different alphabet for your Base64 encoding (you can do this by replacing the mapping function above). This essentially equates to doing base64 and then using a substitution cipher. How would you break into this if you weren't given the alphabet - if this were the key and we converted to encryption where before we had encoding.</li>
<li>Adapt your functions so that they can convert between plain text and Base16, Base32 and Base64.</li>
<li>Find out about uses of Base64 in context, <a href="https://en.wikipedia.org/wiki/Base64#Other_applications">Wikipedia</a> offers some. As I say, it is one of the most widely used encoding schemes on the web.</li>
<li>Advanced: Write a file transfer program that can send binary files using sockets, web requests, or your choice of transmission mechanism for your language. Read in a file such as an image file as binary data, encode it using base64, transmit it as text across your local network and then receive it on a different PC. Decode the message and then save the file to disk</a>
</ul>

<h3>Hints & Solutions</h3>
<ol>
<li>Looks like there are no nested loops in the algorithm - it is just linear or O(n) complexity, which is a bit boring.</li>
<li></li>
<li>The binary conversion should give:  10011000000010 100000 1010100 1001111 1001101 1001111 1010010 1010010 1001111 1010111 <a href="https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Regex','string':'%25u'%7D,'%20',true,false,true,false)Fork('%20','%20',false)From_Base(16)To_Base(2)&input=MjYwMiV1MDAyMCV1MDA1NCV1MDA0RiV1MDA0RCV1MDA0RiV1MDA1MiV1MDA1MiV1MDA0RiV1MDA1Nw" >Recipe Here</a>. Then you should get mAoKk+bPpUp9cA== from the base64 encode - <a href="https://cryptii.com/pipes/binary-to-base64">check here</a></li>
<li>It would actually be quite difficult to do. Since Base64 normalises the distribution of letters, we wouldn't be able to rely on Chi2, Index of Coincidence or Frequency Analysis. It would also be challenging to compare different sections of cipher text, because strings do not have a consistent encoding in B64 - it depends on what surrounds them. Your best bet would be to have a crib word at the beginning of the message, encode it into Base64, then discard the last 2 characters (as these will have been affected by whatever letter comes next in the plaintext, and we have wrongly assumed that there is nothing). Check which swaps would be required to make the right conversion and make these swaps. Then try to build from there by substitution. This is genuinely quite a secure cipher, especially when we compare it to its simplicity. While with a supercomputer we could try all 64!(More than 1.2688693218588414*10^89) permutations (Any of the 64 characters in the scheme could represent 000000, 63 for 000001, 62 for 000010, and so on...). Simulated Anealing or Hill Climbing - both ML based approaches would struggle because they rely on the ability to compare the decoded text to the expected characteristics of English text. We can't do that, as we can't correctly decode the base64 until we have understood the entire scheme. This proves the importance of freely distributing the mapping table to produce a succesful encoding scheme.</li>
<li>These other two encodings are much less useful and so much less commonly used. They tend to use A-P and A-Z2-7= respectively.</li>
<li>The most interesting ones for me are embedding images inside other images (JPGs inside SVGs), and the possibility of using a data: URI in CSS, which means there is no need to refer to external file assets.</li>
<li>You will need to do this across your local network for it to work without having problems with port forwarding or NAT. You could open two separate ports on the same computer, running two separate programs from different folders - then do a network transfer between them.</li>
</ol>
