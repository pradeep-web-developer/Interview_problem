# find the First Non-Repeat Character in the string
# this type Question used to the count method.

input_str = "anssdansassadsssacvdcaaaaccc"
for char in input_str:
  print(char)
  if input_str.count(char)==1:
    print("char is",char)
    break
  