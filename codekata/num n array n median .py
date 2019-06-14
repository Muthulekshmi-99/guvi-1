x1=int(input())
y1=list(map(int,input().split()))
if(x1==len(y1)):
  y1.sort()
  med=x1//2
print(y1[med])
