import math


def canGetExactChange(targetMoney, denominations):
  flag = False
  if targetMoney in denominations:
    return True
  for i,j in enumerate(denominations):
      if (targetMoney - j) >= 0:
        flag = canGetExactChange(targetMoney - j, denominations)
  return flag


#########


def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  target_1 = 94
  arr_1 = [5, 10, 25, 100, 200]
  expected_1 = False
  output_1 = canGetExactChange(target_1, arr_1)
  check(expected_1, output_1)

  target_2 = 75
  arr_2 = [4, 17, 29]
  expected_2 = True
  output_2 = canGetExactChange(target_2, arr_2)
  check(expected_2, output_2)