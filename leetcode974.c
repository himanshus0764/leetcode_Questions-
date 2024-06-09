#include <stdio.h>
#include <stdlib.h>

int main() {
    int nums[] = {4, 5, 0, -2, -3, 1};
    int k = 5;
    int subarrays = 0;
    int prefixSum = 0;
    int remainderCount[k];
    for (int i = 0; i < k; i++) {
        remainderCount[i] = 0;
    }
    remainderCount[0] = 1;

    for (int i = 0; i < 6; i++) {
        prefixSum += nums[i];
        int remainder = prefixSum % k;
        if (remainder < 0) {
            remainder += k;
        }
        if (remainderCount[remainder] > 0) {
            subarrays += remainderCount[remainder];
            remainderCount[remainder]++;
        } else {
            remainderCount[remainder] = 1;
        }
    }

    printf("%d\n", subarrays);
    return 0;
}

