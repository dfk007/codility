# Odd Occurrences in Array in Python

# Find value that occurs in odd number of elements.

# sort 
# test equality between two consecutive elements
# increment index by 2

def solution(A):
  A.sort()
  A.append(-1)

  for i in range(0, len(A), 2):
    if A[i] != A[i+1]:
      return A[i]

pass