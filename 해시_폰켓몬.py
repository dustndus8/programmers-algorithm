def solution(nums):
    answer = 0
    dict={}
    for n in nums:
        dict[n] = 1
    if len(nums) // 2 <= len(dict):
        return len(nums) // 2
    return len(dict)