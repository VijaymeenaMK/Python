num1,num2=map(int,input().split())
for i in range(num1+1,num2):
  temp=i
  sum=0
  while(temp>0):
    n=temp%10
    sum+=n**3
    temp//=10
  if(i==sum):
    print(i,end=' ')
