from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #newList = [i for i in nums  if i<=target]
        newList = nums
        print('Nueva Lista',newList)
        for i in range(0, len(newList)):
            for j in range(i+1, len(newList)):
                if newList[i] + newList[j] == target:
                    return i,j
        #return 0,0
                
sol = Solution()
result = sol.twoSum([2,7,11,15], 9)
print(list(result))
result = sol.twoSum([3,2,4], 6)
print(list(result))
result = sol.twoSum([3,3], 6)
print(list(result))
result = sol.twoSum([0,4,3,0], 0)
print(list(result))