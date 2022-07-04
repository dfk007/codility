def solution(A):
    # write your code in Python 3.6

    sE = 0
    s = 0

    for i in range(0, len(A)):
        if A[i] == 0:
            sE += 1

        elif A[i] == 1:
            s += sE

    if s > 1000000000:
        return -1
        
    else:
        return s
    pass