#include <stdio.h>

int main() {
    int nums[] = {0};
    int k = 1;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    
    if (k == 0) {
        for (int i = 0; i < numsSize - 1; i++) {
            if (nums[i] == 0 && nums[i + 1] == 0) {
                printf("true\n");
                return 0;
            }
        }
        printf("false\n");
    } else {
        int remainderDict[numsSize + 1];
        int cumulativeSum = 0;

        for (int i = 0; i <= numsSize; i++) {
            remainderDict[i] = -1;
        }

        for (int i = 0; i < numsSize; i++) {
            cumulativeSum += nums[i];
            int remainder = cumulativeSum % k;

            if (remainderDict[remainder] != -1) {
                if (i - remainderDict[remainder] > 1) {
                    printf("true\n");
                    return 0;
                }
            } else {
                remainderDict[remainder] = i;
            }
        }
        printf("false\n");
    }

    return 0;
}
