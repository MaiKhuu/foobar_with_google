DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solve(map):
  h = len(map)
  w = len(map[0])

  steps = []
  for i in range(h):
    steps.append([])
    for j in range(w):
      steps[i].append(0)

  steps[0][0] = 1
  queue = [[0, 0]]

  while len(queue) > 0 and steps[h - 1][w - 1] == 0:
    i, j = queue.pop(0)
    for d in DIRECTIONS: 
      ii = i + d[0]
      jj = j + d[1]
      if 0 <= ii < h and 0 <= jj < w and map[ii][jj] == 0 and steps[ii][jj] == 0:
        queue.append([ii, jj])
        steps[ii][jj] = steps[i][j] + 1

  return steps[h - 1][w - 1]

def solution(map):
  result = solve(map)
  for i in range(len(map)):
    for j in range(len(map[0])):
      if map[i][j] == 1:
        map[i][j] = 0
        new_result = solve(map)
        if new_result > 0:
          if result == 0 or result > new_result:
            result = new_result
        map[i][j] = 1

  return result