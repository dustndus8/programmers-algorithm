def solution(answers):
    cnt = [0, 0, 0]
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]

    for i in range(len(answers)):
        if a[i%len(a)] == answers[i]:
            cnt[0]+=1
        if b[i%len(b)] == answers[i]:
            cnt[1]+=1
        if c[i%len(c)] == answers[i]:
            cnt[2]+=1

    answer = []
    for idx, score in enumerate(cnt):
        if score == max(cnt):
            answer.append(idx+1)
    return answer