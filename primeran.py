n1,n2=map(int,input().split())
for i in range(n1+1,n2):
  for j in range(2,i):
    if(i%j==0):
      break
  else:
     print(i,end=' ')
