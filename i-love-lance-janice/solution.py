ALPHABETS_BACKWARD = 'zyxwvutsrqponmlkjihgfedcba'

def solution(s):
  result = ""
  for char in s:
    if 'a' <= char <= 'z':
      result += ALPHABETS_BACKWARD[ord(char) - 97]
    else:
      result += char
  return result
