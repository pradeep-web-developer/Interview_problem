l=["hello",10,20,40,20,60,40,30]
d=[]
for ele in l:
  if l.count(ele)>1 and ele not in d:
    d.append(ele)

print(d)