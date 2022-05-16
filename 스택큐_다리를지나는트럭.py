def solution(bridge_length, weight, truck_weights):
    answer = 0
    s=0
    run_bridge = [0 for _ in range(bridge_length)]
    
    while (True):
        p_tmp = run_bridge.pop(0)
        s-= p_tmp
        if (len(truck_weights)!=0 and s+truck_weights[0]<=weight):
            p_tmp = truck_weights.pop(0)
            run_bridge.append(p_tmp)
            s+=p_tmp
        else:
            run_bridge.append(0)
        if len(truck_weights)==0 and s==0:
            break
        answer+=1

    answer +=1
    return answer