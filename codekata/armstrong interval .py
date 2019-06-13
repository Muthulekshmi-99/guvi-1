ar,iv=map(int,input().split())
for n in range(ar+1,iv):
  sum1=0
  t=n
  while(t>0):
    digits=t%10
    sum1+=digits**3
    t//=10
  if(n==sum1):
      print(n,end=" ")
