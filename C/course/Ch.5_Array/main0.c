#include <stdio.h>
#define LENGTH 10

int main(void) {
    int arr[LENGTH] = {0};
    int i;

    for(i = 0; i < LENGTH; i++) {
        printf("%d ", arr[i]);
    }
    putchar('\n');

    for(i = 0; i < LENGTH; i++) {
        arr[i] = i;
    }

    for(i = 0; i < LENGTH; i++) {
        printf("%d ", arr[i]);
    }

    putchar('\n');

    return 0;
} 
