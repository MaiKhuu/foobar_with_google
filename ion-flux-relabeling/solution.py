def get_level_count(h):
  result = [1]
  for i in range(1, h):
    result.append(result[-1] + 2**i)
  return result

def get_up_node(num, level_count):
  level = len(level_count) - 1
  root = level_count[level]
  while True:
    right = root - 1
    left = right - level_count[level - 1]
    
    if num == right or num == left:
      return root
    
    level -= 1
    root = left if num < left else right

def solution(h, p):
  level_count = get_level_count(h)
  result = []
  for x in p:
    if x == level_count[-1]:
      result.append(-1)
    else:
      result.append(get_up_node(x, level_count))
  return result

print(solution(5, [19, 14, 28]))