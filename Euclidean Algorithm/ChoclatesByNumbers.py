# Easy: There are N chocolates in a circle. Count the number of chocolates you will eat. 
 
def gcd(a,b):

  if a%b == 0:
    return b
    
  else:
    return gcd(b, a%b)

def solution(N,M):
  return int(N/gcd(N,M))
  pass 