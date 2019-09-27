def solution(s):
    p_num = (s.lower()).count('p')
    y_num = (s.lower()).count('y')
    if(p_num == y_num):
        return True
    else:
        return False