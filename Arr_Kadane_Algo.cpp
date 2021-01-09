#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int Const_arr(int arr[100], int size); // Function Declaration

int main()
{
    int arr[100], n, i;
    cin >> n;
    for (i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    // for (i = 0; i < n; i++)
    // {
    //     cout << arr[i] << endl;
    // }
    cout << Const_arr(arr, n); // We cannot directly pass the array to the function, so we will use referencing or pass a pointer to an array by specifying the array's name without an index.
    // www.tutorialspoint.com/cplusplus/cpp_passing_arrays_to_functions.htm

    return 0;
}

int Const_arr(int arr[100], int size) // Function Definition
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
}