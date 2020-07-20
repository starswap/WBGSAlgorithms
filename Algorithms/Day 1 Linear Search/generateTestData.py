#To generate random integer test data as specified by input and save to a file
import random
import time

amountOfData = int(input("How many examples to generate?"))
min = int(input("Minimum val:"))
max = int(input("Maximum val:"))
separator = raw_input("What to separate with (type newline for \\n)?")
fileName = "testData" + str(time.time()).replace(".","") + ".txt"
f = open(fileName,"w")
for i in range(amountOfData):
	f.write(str(random.randint(min,max)))
	if separator == "newline":
		f.write("\n") 
	else:	
		f.write(separator)
f.close()
print(str(amountOfData)+" examples from " + str(min) + " to " + str(max) + ", separated by " + separator + " generated and saved to file " + fileName)
