print("hello_world")
def mean(input):
  sum = 0
  for entry in input:
    sum += entry
  return sum / len(input)

my_list = [0, 1, 2, 3, 4, 5]
print(mean(my_list))
import math
def median(input):
  mid = math.floor(len(input)/2)
  input.sort()
  if len(input) % 2 == 0:
    return (input[mid] + input[mid - 1])/2
  else:
    return input[mid]
print(median(my_list))