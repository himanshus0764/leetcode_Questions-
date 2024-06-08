#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 6, 2, 3, 4, 7, 8};
    int groupize = 3;
    int arrSize = sizeof(arr) / sizeof(arr[0]);

    if (arrSize%groupize == 0) {
        printf("%s", "true\n");
    } else {
        printf("%s", "false\n");
    }

    return 0;
}
