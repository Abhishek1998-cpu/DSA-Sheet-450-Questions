// Minimum Number of Jumps to Reach the end of an Array

#include <bits/stdc++.h>
using namespace std;
int minJumps(int arr[], int n)
{

    // Base case: when source and
    // destination are same
    if (n == 1)
        return 0;

    // Traverse through all the points
    // reachable from arr[l]
    // Recursively, get the minimum number
    // of jumps needed to reach arr[h] from
    // these reachable points
    int res = INT_MAX;
    for (int i = n - 2; i >= 0; i--)
    {
        if (i + arr[i] >= n - 1)
        {
            int sub_res = minJumps(arr, i + 1);
            if (sub_res != INT_MAX)
                res = min(res, sub_res + 1);
        }
    }

    return res;
}

int main()
{
    int n, i, j;
    cin >> n;
    int arr[n]; // This way we can define the array of the required size
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    cout << minJumps(arr, n) << endl;
    return 0;
}

// Imp -> www.geeksforgeeks.org/int_max-int_min-cc-applications/