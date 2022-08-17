def solution(maps):
    answer=func(maps,0,0)
    return answer

def func(field,i,j):
    field[0][0]=-1
    stack=[]
    answer=[]
    cnt = 1
    mincnt=0
    stack.append((i,j,cnt))
    while stack:
        tmp = stack.pop(0)
        #print('stack',tmp,cnt,len(field[0]),len(field))
        if tmp[1] == len(field[0])-1 and tmp[0] == len(field)-1:
            answer.append(tmp[2])
        
        # 하
        if tmp[0]!=len(field)-1:
            if field[tmp[0]+1][tmp[1]] == 1:
                field[tmp[0]+1][tmp[1]] = -1
                stack.append((tmp[0]+1,tmp[1],tmp[2]+1))
        # 우
        if tmp[1]!=len(field[0])-1:
            if field[tmp[0]][tmp[1]+1] == 1:
                field[tmp[0]][tmp[1]+1] = -1
                stack.append((tmp[0],tmp[1]+1,tmp[2]+1))
        # 상
        if tmp[0]!=0:
            if field[tmp[0]-1][tmp[1]] == 1:
                field[tmp[0]-1][tmp[1]] = -1
                stack.append((tmp[0]-1,tmp[1],tmp[2]+1))
        # 좌
        if tmp[1]!=0:
            if field[tmp[0]][tmp[1]-1] == 1:
                field[tmp[0]][tmp[1]-1] = -1
                stack.append((tmp[0],tmp[1]-1,tmp[2]+1))
    if len(answer)==0:
        mincnt=-1
    else:
        mincnt=min(answer)
        
    return mincnt