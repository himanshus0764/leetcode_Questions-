#include <stdio.h>
#include <string.h>

int main() {
    char *strs[] = {"flower", "flow", "flight"};
    int strs_size = sizeof(strs) / sizeof(strs[0]);
    char st[1000] = {0};
    char duplicate[1000] = {0};

    for (int i = 0; i < strs_size; i++) {
        for (int j = 0; strs[i][j] != '\0'; j++) {
            strncat(st, &strs[i][j], 1);
        }
    }

    for (int i = 0; st[i] != '\0'; i++) {
        int count = 0;
        for (int j = 0; st[j] != '\0'; j++) {
            if (st[i] == st[j]) {
                count++;
            }
        }
        if (count > 2 && strchr(duplicate, st[i]) == NULL) {
            strncat(duplicate, &st[i], 1);
        }
    }

    printf("%s\n", duplicate);
    return 0;
}

