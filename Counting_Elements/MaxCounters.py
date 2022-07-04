# Medium: MaxCounters 
# Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.

def solution(N, A):

  R = [0] * N
  m = 0 
  b = 0 

  for i in range(0, len(A)):
    if A[i] <= N:
      R[A[i]-1] = max(b, R[A[i]-1]) + 1

      m = max(m, R[A[i] -1])

    else:
      b = m

  for i in range(0, len(R)):
    if(R[i] < b):
      R[i] = b

  return R