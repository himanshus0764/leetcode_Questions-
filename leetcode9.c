#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, a[100];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    if (a[n-1] == a[0]) {
        printf("true");
    } else {
        printf("false");
    }
    return 0;
}