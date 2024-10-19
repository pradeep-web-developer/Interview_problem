# we are learn the problem two.
#Write the Python Program to count the frequency of words appearing in a string.
def freq_words():
  str=input("Enter the string: ")
  li=str.split()
  d={}
  
  for i in li:
    if i not in d.keys():
      d[i]=0
    d[i]=d[i]+1
  print(d)
freq_words()