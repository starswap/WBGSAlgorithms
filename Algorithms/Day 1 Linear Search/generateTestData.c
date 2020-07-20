//Doesn't quite work. Maybe you guys can help

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main () {
	FILE *myFile;
	char *fileName;
	time_t startTime;
	unsigned long numOfTestCases;
	int i;
	unsigned long max;
//	char separator[1];
	char separator = '\n';
	fileName = malloc(60);
	//separator = malloc(10);
	strcpy(fileName,"testData/sortTest");
	startTime = time(NULL);
	sprintf(fileName,"%s%d.txt",fileName,startTime);
	myFile = fopen(fileName,"w");
	printf("How many test cases to generate?");
	scanf("%ld",&numOfTestCases);
	printf("Maximum value?");
        scanf("%d",&max);
//	printf("Separator:");
//	separator[0] = fgetc(stdin);
	for (i=0;i<numOfTestCases;i++) {
		fprintf(myFile,"%d%s",(rand() % max) + 1,separator);
	}
	printf("%ld test cases generated and saved to file %s",numOfTestCases,fileName);
	fclose(myFile);
}
