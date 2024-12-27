def solution(x):
    answer = True
    ls = list(str(x))
    n = 0
    for i in ls:
        n += int(i)
        
    if x%n == 0:
        answer = True
    else:
        answer = False
    return answer