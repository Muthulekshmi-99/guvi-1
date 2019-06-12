x,y=input().split()
x=int(x)
y=int(y)
z=0
array=[int(k) for k in input().split()]
for x in range(0,y):
  z=z+array[x]
print(z)
