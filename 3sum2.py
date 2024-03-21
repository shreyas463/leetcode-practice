# Triplets with Smaller Sum (medium)
# Problem Statement
# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

# Example 1:

# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:

# Input: [-1, 4, 2, 1, 3], target=5 
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: 
# [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
# Constraints:

# n == att.length
# 0 <= n <= 3500
# -100 <= arr[i] <= 100
# -100 <= target <= 100

class Solution: 
  def searchTriplets(self, arr, target):
    res=0
    arr.sort()
    for i in range(len(arr)-3):
      l=i+1
      r=len(arr)-1
      threesum=arr[i]+arr[l]+arr[r]
      if threesum<target:
        res+=r-l
        l+=1
      else:
        r-=1
    return res
    
