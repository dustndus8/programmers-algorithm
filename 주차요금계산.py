import math
from collections import defaultdict


def solution(fees, records):
    answer = []
    record_dict = defaultdict(list)
    order=[]
    
    for record in records:
        record = record.split(' ')
        record[1] = int(record[1])
        
        if record[1] not in order:
            order.append(record[1])
        if len(record_dict[record[1]]) == 0 :
            record_dict[record[1]].append(0)
            record_dict[record[1]].append(0)
            record_dict[record[1]].append(0)
            
        if record[2] == "IN":
            record_dict[record[1]][0] = record[0]

        else:
            # OUT 시 OUT-IN 계산
            record_dict[record[1]][1] += convertMinute(record[0]) - convertMinute(record_dict[record[1]][0])
            record_dict[record[1]][0] = ''
        
    for key, value in record_dict.items():
        if len(value[0])!=0:
            record_dict[key][1] += convertMinute('23:59') - convertMinute(record_dict[key][0])
            
        record_dict[key][2] = calculateParkingFee(record_dict[key][1],fees)
    
    sorted_dict = sorted(record_dict.keys())

    for key in sorted_dict:
        answer.append(record_dict[key][2])
    
    return answer

def convertMinute(time):
    time = time.split(':')
    return int(time[0])*60 + int(time[1])

def calculateParkingFee(minute,fees):
    if (minute<=fees[0]):
        print('if',fees[1])
        return fees[1]
    else:
        return fees[1] + math.ceil((minute - fees[0])/fees[2])*fees[3]