def solution(lottos, win_nums):
    answer = []
    cnt=0
    
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            win_nums.remove(lotto)
            cnt+=1
        elif lotto == 0:
            zero+=1
    max_number = cnt+zero
    min_number = cnt
    
    checkRank(max_number,answer)
    checkRank(min_number,answer)
                         
    return answer

def checkRank(number,answer):
    if number == 6:
        answer.append(1)
    elif number == 5:
        answer.append(2)
    elif number == 4:
        answer.append(3)
    elif number == 3:
        answer.append(4)
    elif number == 2:
        answer.append(5)
    else:
        answer.append(6)