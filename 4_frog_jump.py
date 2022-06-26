# Frog Jump 
# Count minimal number of jumps from position X to Y.



def solution(x, y, d):
  v = (y - x) // d # number of jumps
  if x + v * d >= y:
    return v
  else:
    return v+1

  pass