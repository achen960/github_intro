import math
def median(input):
  mid = math.floor(len(input)/2)
  input.sort()
  if len(input) % 2 == 0:
    return (input[mid] + input[mid - 1])/2
  else:
    return input[mid]
my_list = [0, 1, 2, 3, 4, 5]
print(median(my_list))