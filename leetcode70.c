#include <stdio.h>
int main(){
    int a=4;
    scanf("%d",&a);
    int arr[a];
    int b=0;
    for (int i=0;i<a;i++){
        if ((b+a)==a){
            arr[i]=1;
            b+=1;a-=1;
        }
    printf("%d",sizeof(arr)/sizeof(arr[0]));
    }
}