p,q=map(int,input().split())
for m in range(p+1,q):
  if(m>1):
    for n in range(2,m):
      if(m%n)==0:
        break
    else:
      print(m,end=" ")
