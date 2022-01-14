def solution(numbers, target):
    n=len(numbers)
    answer = 0
    def dfs(i,s):
        if i==n:
            if s == target:
                nonlocal answer
                answer+=1
        else:
            dfs(i+1,s+numbers[i])
            dfs(i+1,s-numbers[i])
    dfs(0,0)
    return answer