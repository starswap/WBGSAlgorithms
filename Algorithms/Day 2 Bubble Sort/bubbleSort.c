#include <stdio.h>//Include input/output library

int* bubbleSort (int* toSort,int upDown, int length) { // 1 = ascending, -1 = descending
        int changed = 1;//Flag to check if the list has suffered a change.
        int i;
        while (changed == 1) {
                changed = 0;
                for (i=0;i<length-1;i++) {
                        if (toSort[i] > upDown*toSort[i+1]) {
                                toSort[i] = toSort[i] ^ toSort[i+1]; //Use bitwise XOR to swap the vals without need for another variable - one of my favourite C tricks. 
                                toSort[i+1] = toSort[i] ^ toSort[i+1];
                                toSort[i] = toSort[i] ^ toSort[i+1];
                                changed = 1;
                        }
                }
        }
        return toSort;
}


