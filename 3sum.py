# Triplet Sum to Zero (medium)
# Problem Statement
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
# Explanation: There are four unique triplets whose sum is equal to zero. smallest sum.'
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

# **Constraints:**

# - `3 <= arr.length <= 3000`
# - `-105 <= arr[i] <= 105`

class Solution:
  def searchTriplets(self, arr):
    res=[]
    arr.sort()
    for i, a in enumerate(arr):
      if i>0 and a==arr[i-1]:
        continue
      l,r=i+1,len(arr)-1
      while l < r:
        threeSum= a + arr[l] + arr[r]
        if threeSum > 0:
          r-=1
        elif threeSum < 0:
          l+=1
        else:
          res.append([a,arr[l], arr[r]])
          l+=1
          while arr[l]==arr[l-1] and l<r:
            l+=1
    return res
