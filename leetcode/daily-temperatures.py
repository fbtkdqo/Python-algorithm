class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []

        for i , cur in enumerate(T):
            # 현재 온도가 스택 값보다 높다면 true
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i -last
            stack.append(i)
        
        return answer