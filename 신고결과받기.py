from collections import defaultdict
def solution(id_list, report, k):
    user_information = defaultdict(list)
    result = [0] * len(id_list)
    
    for report_inform in report:
        tmp_list = report_inform.split(' ')
        if tmp_list[0] not in user_information[tmp_list[1]]:
            user_information[tmp_list[1]].append(tmp_list[0])
    
    for i in id_list:
        if len(user_information[i]) >= k:
            for value in user_information[i]:
                result[id_list.index(value)] += 1
    return result