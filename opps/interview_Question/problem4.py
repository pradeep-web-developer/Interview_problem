# Find the missing Number in an Array(using summation and XOR operation)
def get_missing_summestion(a):
  n=a[-1]
  sum1=0
  total=n*(n+1)//2
  sum1=sum(a)
  print(total-sum1)
  
  
a=[1,2,4,5,6,7]
get_missing_summestion(a)


def get_missing_xor(a):
  n=len(a)
  xor_a=a[0]
  for index in range(1,n):
    xor_a=xor_a^a[index]
  for index in range(1,n+2):
    x2=x2^index
  print(xor_a^x2)
  