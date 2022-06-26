# The value that occurs in more than half of the elements of A

def solution(A):

  if len(A) == 0:
    return -1 # -1 returned because array does not have a dominator.
  
  if len(A) == 1:
    return 0

  B = A.copy()
  B.sort()

  c = 1
  n = len(B)

  for i in range(1, n):
    
    if B[i] != B[i-1]:
      c = 1

    else: 
      c += 1

    if c > int(n/2):
      return A.index(B[i])

  return 1

  pass
