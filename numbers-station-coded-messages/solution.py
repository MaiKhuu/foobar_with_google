def solution(l, t):
  starter = 0
  ender = 0
  current_sum = l[0]
  while starter < len(l) and ender < len(l):
    while current_sum < t and ender < len(l) - 1:
      ender +=1 
      current_sum += l[ender]
    if ender == len(l) - 1 and current_sum < t:
      return [-1, -1] 
    while current_sum > t and starter <= ender and starter < len(l):
      current_sum -= l[starter]
      starter += 1
    if current_sum == t:
      return [starter, ender]
  return [-1, -1]
    
print(solution([1, 2, 3, 4], 15))