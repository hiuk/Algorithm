def solution(s):
    center_index = len(s) // 2
    if(len(s) % 2 == 0):
        return s[center_index-1:center_index+1]
    else:
        return s[center_index]

print(solution('abcd'))