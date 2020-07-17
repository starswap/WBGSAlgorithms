#include <stdio.h>//Include input/output module
#include <string.h>//Include string manipulation functions
#include <stdlib.h>//Include many standard library functions, specifically the atoi function which converts a str to an int.
#include <limits.h>//Include the Constants such as LONG_MAX that tell me the limits of the data types for my installation
int part1 (long toCheck);//Define function prototype for part 1 with type labelled return val and input.
int part2 (long toCheck);//Define function prototype for part 2 with type labelled return val and input.

int main() {
	long inputInt;// Declare the variable to store the input
	printf("The maximum input into this program is %d and the minimum is %d because it uses the long data type.\n",LONG_MAX,LONG_MIN); // We could add some input verification rather than relying on the user but where's the fun in that? Buffer Overflow FTW!
	printf("What is the number to check?");
	scanf("%ld",&inputInt); //Input the integer and store in inputInt
	printf("The function from Part 1 of the challenge returned: %s\n",(part1(inputInt)==1) ? "Yes the number is divisible by 7." : "No the number is not divisible by 7."); // Call the basic function that uses mod
	printf("The function from Part 2 of the challenge returned: %s\n",(part2(inputInt)==1) ? "Yes the number is divisible by 7." : "No the number is not divisible by 7."); // Call the complex function that uses the Maths. This: () ? : is called the ternary operator in C. It is basically a condensed if statement, which is useful if you want to make comparisons inline rather than before you output.
	return 0; //Return success as required by the function declaration
}

int part1 (long toCheck) {
	return (toCheck%7==0) ? 1 : 0; //Use the ternary and mod operators to find the remainder when dividing the input by 7. If 0, it divides exactly so return True or 1. If not, return False or 0.
}
int part2 (long toCheck) {
	long tens;
	int units;
	char *unitsChar;
	char stringed[20];
	sprintf(stringed,"%ld",toCheck);//Convert the input integer to a string so we can select different digits
	if (strlen(stringed) == 1 || (strlen(stringed)==2 && stringed[0] == '-')) { //Check if we have only a one digit number as then we can just run through all of the possibilities. 
		switch(toCheck) { //If we have 7,0, or -7, we know these are divisible by 7.
			case 0:
			case -7:
			case 7:return 1;break;
			default:return 0;//Else we have a single digit which isn't divisible by seven.
		}
	}
	unitsChar = malloc(1);//Allocate enough memory for 1 character to the character variable that will store the unit digit once separated from the number.
	*unitsChar = stringed[strlen(stringed)-1];//Assign the unitsChar variable with this digit.
	units = (stringed[0] == '-') ? -1*atoi(unitsChar) : atoi(unitsChar);//If the first character of the number is a -, then we have a negative number so adjust the final units integer accordingly to make sure that the 10M + R representation as described in the problem formulation is correct.
	tens = (toCheck - units)/10;//tens is M from the problem formulation, which is the number of tens in the original number.
	tens = tens - 2*units;//Do the final divisibility test by subtracting 2R from M. We know need to know if this result is divisible by 7 to know if the original number was divisible by 7. Hence, use recursion.
	return part2(tens); // Using a recursive function. The while loop method works too. We ask whether the result we just got is divisible by 7 or not by calling the same function. If it is, then the original number was, and if not then the original number was not. Thus the answer to the original division question is the same as that of the new one, which we can hence directly return from the function.
}
