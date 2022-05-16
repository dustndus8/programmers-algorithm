def solution(array, commands):
    answer = []
    for i in commands:
        slice_list = array[i[0]-1:i[1]]
        slice_list.sort()
        idx = i[2]-1
        answer.append(slice_list[idx])
    return answer