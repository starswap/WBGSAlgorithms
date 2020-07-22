#include <stdio.h>

int main () {
	int a;
	int b;
	int r;
	int q;
	int original_a;
	int original_b;
	printf("\nThe Euclidean Algorithm to find the HCF.\n");
	printf("Enter the first number:");
	scanf("%d",&a);
	original_a = a;
	printf("Enter the second number:");
	scanf("%d",&b);
	original_b = b;
	while (a != 0 && b != 0) {
		if (a > b) {
			r = a % b;
			q = a / b;
		}
		else {
			r = b % a;
			q = b / a;
		} 
	//	printf("r: %d ; q: %d a: %d ; b: %d\n",r,q);
		a = b;
		b = r;
	}
	printf("The HCF of %d and %d is %d.\n",original_a,original_b,(a == 0) ? b : a);
	return 0;
}

