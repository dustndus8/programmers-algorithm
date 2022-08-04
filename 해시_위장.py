from collections import defaultdict
def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    
    # dict 만들기
    for cloth in clothes:
        clothes_dict[cloth[1]].append(cloth[0])
    
    for value in clothes_dict.values():
        answer *= (len(value)+1)
    answer -= 1
    return answer