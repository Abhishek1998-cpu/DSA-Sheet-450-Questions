// My Solution of the Kadane Algo's (Largest Contiguous Subarray Sum) in C Programming Language

#include <stdio.h>
int Const_arr(int arr[100], int size); // Function Declaration
int main()
{
    int arr[100], n, i;
    scanf("%d", &n);
    // printf("%d", n + 100);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("%d", Const_arr(arr, n));
    return 0;
} // Main Function
int Const_arr(int arr[100], int size)
{
    int max_so_far = 0;
    int max_ending_here = 0;
    int i;
    for (i = 0; i < size; i++)
    {
        max_ending_here = max_ending_here + arr[i];
        if (max_so_far < max_ending_here)
        {
            max_so_far = max_ending_here;
        }
        else if (max_ending_here < 0)
        {
            max_ending_here = 0;
        }
        else
        {
        }
    }
    return max_so_far;

} // Function Body