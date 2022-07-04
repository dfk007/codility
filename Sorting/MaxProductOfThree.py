# MaxProductOfThree 
# Maximize A[P] * A[Q] * A[R] for any triplet (P,Q, R).

def solution(A):
  A.sort()
  N = len(A)
  P1 = A[N-1]*A[0]*A[1]
  P2 = A[N-1]*A[N-2]*A[N-3]

  return max(P1, P2)

  pass