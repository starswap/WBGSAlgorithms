#Simple translation of the pseudocode example in problemFormulation.md into python
#Note that you can run this as a library, importing into a python shell from here.
#Then you can run something like: Base64.base64_encode(Base64.string_to_binary_string("B64"))

def to_binary(base10,lengthMultiple):
	answerString = ""
	while (base10 != 1):
		answerString = answerString + str(base10 % 2)
		base10 = base10 // 2
	answerString = answerString + "1"
        while not(len(answerString) % lengthMultiple == 0):
		answerString =  answerString + "0"
	return ''.join(answerString[::-1])


def to_decimal(base2):
	answer = 0
	binaryString = str(base2)
	multiplier = 1
	for b in binaryString[::-1]:
		answer = answer + multiplier * int(b)
		multiplier = multiplier * 2
	return answer


def string_to_binary_string(inputString): #If you want to use a different starting encoding such as Unicode UTF16 for example, this is the function to change. The others should work fine.
	binaryString = ""
	for char in inputString:
		ASCIIBinary = to_binary(ord(char),8) #We need to make sure that this is of length that is a multiple of 8 for B64 to work
		binaryString = binaryString + ASCIIBinary
	
	return binaryString


def binary_string_to_string(binaryString): #You will need to change this as well
	resultString = ""
	i = 0
	while (i < len(binaryString)-7):
		resultString = resultString + chr(to_decimal(binaryString[i:i+8]))
		i = i+8
	return resultString


def base64_encode(binaryString): #Making these functions convert between base64 and binary strings rather than between base64 and text strings is good as it means non-text data such as images can easily be encoded
	i = 0
	resultString = ""
	mapping = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
	while (i+6 < len(binaryString)-1):
		currentBinaryString = binaryString[i:i+6] #Select current block to convert. We then need to convert it back to a character. We could do this with a simple mapping dictionary/array/hashtable/object or by using the sequential properties of the table. 0-25 = A-Z, 26-51 = a-z, 52-61 = 0-9, 62,63 = +,/
		decimal = to_decimal(currentBinaryString)
		resultString = resultString + mapping[decimal]
		i = i+6
	binaryString = binaryString + "000000"
	lastBlock = binaryString[i:i+6] 
	print(lastBlock)
	resultString = resultString + mapping[to_decimal(lastBlock)]
	numberOfPaddingBits = 6 - (len(binaryString)-6 - i) 
	numberOfEqualsRequired = numberOfPaddingBits/2
	for i in range(numberOfEqualsRequired):
		resultString = resultString + "="
	return resultString


def base64_decode(textString): #PSEUDO
	mapping = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
	i = len(textString)-1
	numberOfEquals = 0
	while (textString[i] == '='):
		numberOfEquals += 1
		i -= 1	
	textString = textString[0:len(textString)-numberOfEquals] #Remember to psedoadjust
	binaryString = ""
	for currentChar in textString:
		currentCharIndex = mapping.index(currentChar) #Any searching algorithm we have done or another - your language probably has one builtin.
		binary = to_binary(currentCharIndex,6) #We need to be sure that we have converted this index to a six char length binary string for this to work. You could use a mapping hash table/dictionary instead of this but this method seems to be quicker.
		binaryString = binaryString + binary
	
	numberOfBitsToIgnore = 2*numberOfEquals
	binaryString = binaryString[0:len(binaryString)-numberOfBitsToIgnore]
	return binaryString

def ascii_e(string): #Just an alias to shorten typing if you only want to use ascii not bit strings
	return base64_encode(string_to_binary_string(string))

def ascii_d(string):
	return binary_string_to_string(base64_decode(string))