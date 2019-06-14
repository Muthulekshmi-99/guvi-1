n=input()
count=0
for m in range(len(n)):
  if(n[m].isnumeric() or n[m].isalpha() or n[m]==' '):
    continue
  else:
   count=count+1
print(count)

