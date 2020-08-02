def to_binary(base10):
	answerString <- ""
	while (base10 != 1):
		answerString <- STR_CONCAT(answerString,INT_TO_STR(base10 MOD 2))
		base10 <- base10 DIV 2
	END_WHILE
	answerString <- STR_CONCAT(answerString,"1")
	return STR_REVERSE(answerString)
END_FUNCTION

def to_decimal(base2,lengthMultiple):
	answer <- 0
	binaryString <- INT_TO_STR(base2)
	multiplier = 1
	for i <- 0 TO len(binaryString) -1:
		answer = multiplier * STR_TO_INT(binaryString[i])
		multiplier = multplier * 2
	
        while NOT(len(result) MOD lengthMultiple == 0):
		result <- STR_CONCAT("0",result)
        END_WHILE
	return answer
END_FUNCTION

def string_to_binary_string(inputString): #If you want to use a different starting encoding such as Unicode UTF16 for example, this is the function to change. The others should work fine.
	binaryString <- ""
	for i <- 0 TO len(inputString) -1:
		ASCIIBinary <- toBinary(CHAR_TO_INT(inputString[i]),8) #We need to make sure that this is of length that is a multiple of 8 for B64 to work
		binaryString <- STR_CONCAT(binaryString,ASCIIBinary)
	
	return binaryString
END_FUNCTION

def binary_string_to_string(binaryString): #You will need to change this as well
	resultString <- ""
	i <- 0
	while (i < len(binaryString)-8):
		result_string = STR_CONCAT(resultString,INT_TO_CHAR(to_decimal(binaryString[i:i+8])))
		i <- i+8
	ENDWHILE
	return resultString
END_FUNCTION

def base64_encode(binaryString): #Making these functions convert between base64 and binary strings rather than between base64 and text strings is good as it means non-text data such as images can easily be encoded
	i <- 0
	resultString <- ""
	mapping <- ["a","b","c","d"....,"A","B","C","D"....,"0","1","2","3"....,"+","/"] #You obviously need to actually fill in all of the values
	while (i+6 < len(binaryString)-1):
		currentBinaryString <- binaryString[i:i+5] #Inclusive ranging! Select current block to convert. We then need to convert it back to a character. We could do this with a simple mapping dictionary/array/hashtable/object or by using the sequential properties of the table. 0-25 = A-Z, 26-51 = a-z, 52-61 = 0-9, 62,63 = +,/
		decimal <- to_decimal(currentBinaryString)
		resultString <- STR_CONCAT(resultString, mapping[decimal])
		i <- i+6
	ENDWHILE
	binaryString <- STR_CONCAT(binary_string,"000000")
	lastBlock <- binaryString[i:i+5] #Inclusive ranging again.
	resultString <- STR_CONCAT(resultString,mapping[to_decimal(lastBlock)])
	numberOfPaddingBits <- (len(binaryString)-6 - i) 
	numberOfEqualsRequired <- numberOfPaddingBits/2
	for i <-1 TO numberOfEqualsRequired:
		resultString <- STR_CONCAT(resultString,"=")
	
	return resultString
END_FUNCTION

def base64_decode(textString):
	mapping <- ["a","b","c","d"....,"A","B","C","D"....,"0","1","2","3"....,"+","/"]
	binary_string <- ""
	for i <- 0 TO len(textString) - 1:
		currentChar <- textString[i]
		currentCharIndex <- ARRAY_SEARCH(mapping,currentChar) #Any searching algorithm we have done or another - your language probably has one builtin.
		binary <- to_binary(currentCharIndex,6) #We need to be sure that we have converted this index to a six char length binary string for this to work. You could use a mapping hash table/dictionary instead of this but this method seems to be quicker.
		binaryString <- ARRAY_CONCAT(binaryString,binary)
	
	i <- len(binaryString)-1
	numberOfEquals <- 0
	while (binaryString[i] == '=':
		numberOfEquals++
		i--
	END_WHILE
	numberOfCharsToIgnore <- 2*numberOfEquals
	binaryString <- binaryString[0:len(binaryString)-numberOfEquals-1]
	return binaryString
END_FUNCTION
