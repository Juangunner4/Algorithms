def solution(n):
    if n == 0:
        return None
    elif n >= n-1:
        return n and n-1
    else:
        return n-1
print(solution(3))