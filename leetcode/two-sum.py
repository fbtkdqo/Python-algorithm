from typing import List

#더하는데 사용할 값을 담을 List[int], 타겟이 되는 숫자 int
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)): #더할 1번째 숫자.
        for j in range(i+1, len(nums)): #더할 2번째 숫자.
            if nums[i] + nums[j] == target: #1번과 2번을 더 했을 때 타겟과 같을 때, 
                return [i,j] #1번 2번의 리스트의 위치값 반환