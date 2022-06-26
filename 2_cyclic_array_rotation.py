# Cyclic Array Rotation in Python
# Rotate an array to the right by a given number of steps.

# (current_index + k) % size_of_array = new_index
 
  
# for each element of A 
#   move its index to 
#   new cyclic position

def solution(A, K):
  N = len(A)
  #B=A.copy()
  B = [None] * N
  for i in range(0, N):
    B[(i + K)%N] = A[i]
  return B
  pass