from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # YOUR ANSWER
    l = len(nums)
    for i in range(l):
        for j in range(l):
            if i == j:
                continue
            
            if nums[i] + nums[j] == target:
                return [i,j]
            
    return

#print(twoSum([3,2,4], 6))
