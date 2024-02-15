def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    elif num % 2 == 1:
        answer = 'Odd'
    return answer

print(solution(3))
print(solution(4))
