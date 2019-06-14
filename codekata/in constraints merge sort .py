x1=int(input())
y1=list(map(int,input().split()))
if(x1==len(y1)):
  y1.sort()
  for k in y1:
    print(k,end=" ")  
