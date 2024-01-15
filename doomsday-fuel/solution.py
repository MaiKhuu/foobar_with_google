from fractions import Fraction

def is_terminal_state(arr, idx):
  for num in arr[idx]:
    if num != 0:
      return False
  return True

def mark_self_returning_probability(arr):
  terminal_states = []
  for i in range(len(arr)):
    if is_terminal_state(arr, i):
      arr[i][i] = 1
      terminal_states.append(i)
  return terminal_states

def make_new_labels(arr, terminal_states):
  result = terminal_states[:]
  for i in range(len(arr)):
    if i not in terminal_states:
      result.append(i)
  return result

def make_new_arr(arr, labels):
  result = []

  for from_node in labels:
    row = []
    for to_node in labels:
      row.append(Fraction(arr[from_node][to_node], sum(arr[from_node])))
    result.append(row)
  
  return result

def get_R(arr, terminal_states):
  result = []
  for row in arr[len(terminal_states):]:
    result.append(row[0:len(terminal_states)])
  return result

def get_Q(arr, terminal_states):
  result = []
  for row in arr[len(terminal_states):]:
    result.append(row[len(terminal_states):])
  return result

def find_f(q):
  identity = []
  
  for i in range(len(q)):
    row = [0] * len(q)
    row[i] = Fraction(1, 1)
    identity.append(row)
  
  result = [row[:] for row in identity]
  
  for i in range(len(q)):
    for j in range(len(q)):
      result[i][j] -= q[i][j]
  
  for i in range(len(q)):
    factor = result[i][i]
    # get 1
    for j in range(len(q)):
      result[i][j] /= factor
      identity[i][j] /= factor

    #get 0
    for j in range(len(q)):
      if j == i:
        continue
      factor = result[j][i]
      for k in range(len(q)):
        result[j][k] = result[j][k] - factor * result[i][k]
        identity[j][k] = identity[j][k] - factor * identity[i][k]

  return identity

def get_probabilities(f, r):
  result = []
  
  for i in range(len(r[0])):
    total = 0
    for j in range(len(f)):
      total += f[0][j] * r[j][i]
    result.append(total)

  return result

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def lcm(a, b):
  return a * b // gcd(a, b)

def solution(arr):
  # if there is only 1 node, 100% ends up at that node
  if len(arr) == 1:
    return [1, 1]
  
  terminal_states = mark_self_returning_probability(arr)
  new_labels = make_new_labels(arr, terminal_states)
  new_arr = make_new_arr(arr, new_labels)
  
  r = get_R(new_arr, terminal_states)
  q = get_Q(new_arr, terminal_states)
  f = find_f(q)
  
  fractions_result = get_probabilities(f, r)
  common_denominator = 1 
  for fraction in fractions_result:
    common_denominator = lcm(common_denominator, fraction.denominator)
  result = []
  for num in fractions_result:
    result.append(int(common_denominator / num.denominator * num.numerator))
  result.append(common_denominator)
  return result

my_list = solution([[0]])
print(my_list)



