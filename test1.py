def is_plalindrome(string):
  string = list(string)
  length = len(string)
  left = 0
  right = length - 1
  while left < right:
    if string[left] != string[right]:
      return False
    left += 1
    right -= 1
  return True