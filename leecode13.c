#include <stdio.h>
#include <string.h>

int main() {
    char n[100];
    scanf("%s", n);

    int store = 0;
    int arr[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    char ar[][3] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    int i = 0;

    while (strlen(n) > 0) {
        if (strncmp(n, ar[i], strlen(ar[i])) == 0) {
            store += arr[i];
            strcpy(n, n + strlen(ar[i]));
        } else {
            i++;
            if (i >= sizeof(arr) / sizeof(arr[0])) {
                break;
            }
        }
    }

    printf("%d\n", store);
    return 0;
}
