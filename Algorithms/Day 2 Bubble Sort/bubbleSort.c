#include <stdio.h>
#include <malloc.h>

int* bubbleSort (int* toSort,int upDown, int length) { // 1 = ascending, -1 = descending
        int changed = 1;
        int i;
        while (changed == 1) {
                changed = 0;
                for (i=0;i<length-1;i++) {
                        if (toSort[i] > upDown*toSort[i+1]) {
                                toSort[i] = toSort[i] ^ toSort[i+1];
                                toSort[i+1] = toSort[i] ^ toSort[i+1];
                                toSort[i] = toSort[i] ^ toSort[i+1];
                                changed = 1;
                        }
                }
        }
        return toSort;
}


