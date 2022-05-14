def solution(priorities, location):
    answer = 0
    idx = []
    for i in range(len(priorities)):
        idx.append(i)
    printer = []
    while priorities:
        check = False
        for i in range(1, len(priorities)):
            if priorities[0] < priorities[i]:
                priorities.append(priorities.pop(0))
                idx.append(idx.pop(0))
                check = True
                break
        if check == False:
            priorities.pop(0)
            printer.append(idx.pop(0))
    for i in range(len(printer)):
        if printer[i] == location:
            return i+1

    return answer