x1=int(input())
y1=list(map(int,input().split()))
y1.sort()
for k in range(0,len(y1)):
  print (y1[k], end=' ')
