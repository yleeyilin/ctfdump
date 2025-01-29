#include <stdio.h>

// Install ghidra with: brew install --cask temurin && brew install --cask ghidra
// NOTE: Ghidra does not work w macos silicon ewjfbou
// TODO: try w macos intel next
int main(void) {
    size_t i, x, y;
    x = 11;
    y = 0;

    for (i = 0; i < 10; i++) {
        printf("%lu\n", i); 
    }

    while (x > 0) {
        printf("%lu\n", x);
        x--;
    }

    do {
        printf("%lu\n", y);
        y++; 
    } while (y < 12);
}