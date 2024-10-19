# Write a  Python a program to convert two list into a dictionary.
def list_to_dict():
  keys =[1,2,3]
  values=['One','Two','Three']
  result=dict(zip(keys,values))
  print(result)
list_to_dict()

def dict_to_tuple():
  x={1: 'one',2:'two',3:'three'}
  for i in x.items():
    print(i)
dict_to_tuple()
