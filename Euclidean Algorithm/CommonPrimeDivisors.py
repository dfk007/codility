#Medium: CHECK WHETHER TWO NUMBERS HAVE THE SAME PRIME DIVISORS. 


def gcd(a, b):
  if a%b == 0:
    return b
  else:
    return gcd(b, a%b)

def solution(A,B):
  l = len(A)
  cnt = 0
  for i in range(0, l):
    a = A[i]
    b = B[i]
    D = gcd(a, b)
    while(gcd(a,D) != 1):
      a /= gcd(a, D)

    while(gcd(b,D) != 1):
      b /= gcd(b, D)

    if(a==1 and b==1):
      cnt += 1

  return cnt 
  pass 