# xor of 0 to n can be either n, 1, n+1, or 0 
def xor_zero_to(n):
  if n % 4 == 0:
    return n
  elif n % 4 == 1:
    return 1
  elif n % 4 == 2:
    return n + 1
  else:
    return 0

# xor of a to b is xor(0 to b) ^ xor(0 to a-1)
def xor_a_to_b(a, b):
  return xor_zero_to(b) ^ xor_zero_to(a - 1)

def solution(start, length):
  result = 0
  for i in range(length):
    start_of_line = start + length * i
    end_of_line = start_of_line + length - i - 1
    result = result ^ xor_a_to_b(start_of_line, end_of_line)
  return result

print(solution(17, 4))