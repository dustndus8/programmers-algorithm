import math
def solution(brown, yellow):
    divisor_list = divisor(brown+yellow)
    for j in range(len(divisor_list)):
        for i in range(len(divisor_list)):
            if (divisor_list[i]*2 + divisor_list[j]*2 - 4) == brown and divisor_list[i]*divisor_list[j] == (brown+yellow):
                answer=[divisor_list[i],divisor_list[j]]
                return answer

def divisor(n):
    tmp=[]
    for i in range(1,n//2):
        if n%i==0:
            tmp.append(i)
    tmp.append(n)
    return tmp