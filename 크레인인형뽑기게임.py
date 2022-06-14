def solution(board, moves):
    answer = 0
    blanket = []
    
    for move in moves:
        for line in board:
            if line[move-1] !=0:
                blanket.append(line[move-1])
                line[move-1] = 0
                if len(blanket)>1:
                    if blanket[-2] == blanket[-1]:
                        blanket.pop()
                        blanket.pop()
                        answer+=2
                break
    return answer