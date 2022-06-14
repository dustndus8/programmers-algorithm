def solution(record):
    answer = []
    user_information = {}
    enter_state=[]
    id_state=[]
    for inform in record:
        tmp_record = inform.split(' ')
        enter_state.append(tmp_record[0])
        id_state.append(tmp_record[1])
        if len(tmp_record) == 3 :
            tmp_record_value = tmp_record[2]
            user_information[tmp_record[1]] = tmp_record_value
    
    for i in range(len(record)):
        tmp = ''
        tmp += str(user_information[id_state[i]]) + '님이 '
        if enter_state[i] == "Enter":
            tmp += '들어왔습니다.'
            answer.append(tmp)
        elif enter_state[i] == "Leave":
            tmp += '나갔습니다.'
            answer.append(tmp)
        else:
            tmp = ''
    
    return answer