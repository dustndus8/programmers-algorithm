def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    print('1단계:',new_id)
    # 2단계
    for char in range(len(new_id)):
        asci = ord(new_id[char])
        if ((asci >= 97 and asci <=122) or (asci >=48 and asci <=57) or (asci==45) or (asci == 95) or (asci == 46)):
            pass
        else:
            new_id=new_id.replace(new_id[char],'A')
    new_id = new_id.replace("A","")
    print('2단계:',new_id)
    # 3단계
    new_id_tmp='A'
    for i in range(len(new_id)):
        if new_id_tmp[-1] == '.' and new_id_tmp[-1] == new_id[i]:
            pass
        else:
            new_id_tmp+=new_id[i]
    new_id = new_id_tmp.replace('A','')
    print('3단계',new_id)
    #4단계
    new_id=new_id.strip('.')
    print('4단계',new_id)
    
    #5단계
    if new_id == '':
        new_id="a"
    print('5단계',new_id)
    
    #6단계
    if len(new_id)>=16:
        new_id=new_id[:15]
    if new_id[-1] == '.':
        new_id=new_id.rstrip('.')
    print('6단계',new_id) 
    
    #7단계
    if len(new_id)<=2:
        while(len(new_id)<3):
            new_id += new_id[-1]
    print('7단계',new_id)
    answer=new_id
    return answer