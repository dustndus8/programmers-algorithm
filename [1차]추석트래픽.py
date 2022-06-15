def solution(lines):
    answer = 1
    information = []
    ms_times=[]
    tmp = []
    max_cnt = [0]*len(lines)
    s_time=[]
    
    print(max_cnt)
    
    if len(lines)==1:
        return 1
       
    for i in range(len(lines)):
        tmp = lines[i].split()
        ms_times.append(calculateMS(str(tmp[1])))
        s_time.append(float(tmp[2][:-1]))
    
    for i in range(len(ms_times)+1):
        cnt=i+1
        while cnt<len(ms_times):
            if int(calculatePreviousTime(ms_times[cnt],s_time[cnt])) < int(ms_times[i])+1000:
                max_cnt[i]+=1
            cnt+=1
    answer += max(max_cnt)
            
    return answer

def calculateMS(time):
    return ( int(time[0:2])*3600 + int(time[3:5])*60 + int(time[6:8] )) * 1000 + int(time[9:12])

def calculatePreviousTime(s, t):
    return s - t*1000 + 1