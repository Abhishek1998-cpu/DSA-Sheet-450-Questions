# Find the Duplicate Number Leetcode
# Sheet -> find the duplicate of an array of N+1 Integers

class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        print(nums)
        nums.sort()
        print(nums)
        X = len(nums)
        for i in range(0, X):
            if(nums[X-i-1] == nums[X-i-2]):
                return(nums[X-i-1])
                break
            else:
                pass


X = Solution()
print(X.findDuplicate([1, 3, 4, 2, 2]))
