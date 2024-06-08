#include <stdio.h>
#include <string.h>

int main() {
    int n;
    scanf("%d", &n);

    char store[100] = "";
    int arr[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    const char *ar[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    int i = 0;

    while (n > 0) {
        if (n >= arr[i]) {
            n -= arr[i];
            strcat(store, ar[i]);
        } else {
            i++;
        }
    }

    printf("%s\n", store);

    return 0;
}
